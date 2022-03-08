import re
from unicodedata import name
from django.shortcuts import get_object_or_404, redirect, render,HttpResponse
from django.contrib import messages
from .models import Oil
from oil.models import Oil
from .forms import OilForm
from django.contrib.auth.decorators import login_required #for login required decorator

# Create your views here.

@login_required(login_url='user:login2')
def index(request):
    return render(request,"index.html")
    
def about(request):
    return render(request,"about.html")

def dashboard(request):
    oils = Oil.objects.filter(user = request.user)
    context = {
        "oils":oils
    }
    return render(request,"dashboard.html",context)

def addOil(request):
    form = OilForm(request.POST or None) #form objemizi oluşturduk. Post request olursa formumuz post requestten gelen bilgilerle doldurulacak.
    if form.is_valid():
        oil = form.save(commit=False) #Bizim modelimizde user özelliği olduğu için bunu belirtmemiz lazım false diyerek bunu kendimizin belirteceğini söyledik. 
        oil.user = request.user
        oil.save()
        messages.success(request,"Kayıt başarılı bir şekilde oluşturuldu")
        return redirect("index")
    return render(request,"addoil.html",{"form":form})

def updateOil(request,id):
    oil = get_object_or_404(Oil,id = id)
    form = OilForm(request.POST or None,instance=oil) #İnstance gelen bilgileri yeni forma aktardık
    if form.is_valid():
        oil = form.save(commit=False)
        oil.user = request.user
        oil.save()
        messages.success(request,"Güncelleme başarılı")
        return redirect("oil:dashboard")
    return render(request,"update.html",{"form":form})

def deleteOil(request,id):
    return render(request,"delete.html")
    

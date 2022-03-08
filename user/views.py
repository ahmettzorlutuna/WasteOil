import imp
from multiprocessing import context
from operator import index
from cv2 import RQDecomp3x3
from django.contrib import messages
from django.shortcuts import redirect, render
from django.template import RequestContext
from user import views
import user
from .forms import RegisterForm #Register formumuzu dahil ettik

from django.contrib import messages

from django.contrib.auth.decorators import login_required #for login required decorator

from .models import *

from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm


# Create your views here.

def register(request):
    
    form = RegisterForm(request.POST or None) #Formumuzu Register formdan gelen bilgilerle doldurduk.
    if form.is_valid():
        username = form.cleaned_data.get("username") #Clean methodundan dönen değerlerimizi burada aldık
        password  = form.cleaned_data.get("password") 

        newUser = User(username = username)
        newUser.set_password(password)

        newUser.save()
        login(request,newUser)
        messages.success(request,"Başarı ile kayıt oldunuz. Giriş Yaptıldı !")

        return redirect("index")
        
    context={
            "form":form
        }
    return render(request,"register.html",context)
    
        
    """form = RegisterForm()
    context= {
        "form" : form
    }"""

def register2(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        form = UserCreationForm() 
        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                messages.success(request,"Başarı ile kayıt oldunuz")
                
                return redirect('user:login2')
    
    context = {
        "form" : form
    }
    return render(request,"register2.html",context)


def login2(request):

    if request.method == 'POST':
        
        username = request.POST.get('username') #formdaki username bilgisini aldık
        password = request.POST.get('password') #formdaki password bilgisini aldık

        user = authenticate(request, username=username , password=password) #authenticate işlemi

        if user is not None: #Yukarıdaki değerler sağlandıysa
            login(request, user)
            return redirect('index')
        else:
            messages.error(request,'Kullanıcı adı veya parola yanlış')

    context={}
    return render(request,"login2.html",context)

def logout2(request):
    logout(request)
    return redirect('user:login2')

def loginUser(request):
    return render(request,"index.html")

def logoutUser(request):
    return render(request,"index.html")
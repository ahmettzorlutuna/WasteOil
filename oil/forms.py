from django import forms
from .models import Oil
#Yağları ekleyeceğimiz form alanı
#https://docs.djangoproject.com/en/3.2/topics/forms/modelforms/

class OilForm(forms.ModelForm):
    class Meta:
        model = Oil #Formumuz ile Oil modelimiz bağlamış olduk.
        fields = ['liter','comp','price']
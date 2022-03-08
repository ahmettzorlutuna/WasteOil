from ensurepip import version
from django.db import models

# Create your models here.

class Oil(models.Model): # Modelimizi oluşturduk.
    user = models.ForeignKey("auth.User",on_delete=models.PROTECT,verbose_name="Kullanıcı") 
    liter = models.DecimalField(max_digits=6,decimal_places=2,verbose_name="Litre")
    comp = models.CharField(max_length=50,verbose_name="Alınan Şirket")
    price = models.DecimalField(max_digits=6,decimal_places=2,verbose_name="Fiyat")
    date = models.DateTimeField(auto_now_add=True,verbose_name="Oluşturulma Tarihi") 
    def __str__(self):
        return self.comp 

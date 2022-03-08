from nntplib import ArticleInfo
from django.contrib import admin

import oil
from .models import Oil
# Register your models here.

@admin.register(Oil) #Oil classımızı ait özelleştirilebilir admin kısmı
class OilAdmin(admin.ModelAdmin):
    
    list_display = ["comp","price","date"]
    list_display_links = ["price","date"] #Link verme 
    search_fields = ["comp"] #Alınan şirkete göre arama 
    list_filter = ["date"] #Filtreleme işlemi
    class Meta:
        model = Oil
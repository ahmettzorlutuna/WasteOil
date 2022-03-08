from django.contrib import admin
from django.urls import path
from oil import views

app_name = "oil"

urlpatterns = [
    path('dashboard/',views.dashboard,name="dashboard"),
    path('about/',views.about,name="about"),
    path('addoil/',views.addOil,name="addoil"),
    path('update/<int:id>',views.updateOil,name="update"),
    path('delete/<int:id>',views.deleteOil,name="delete")
]
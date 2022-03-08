from django.contrib import admin
from django.urls import path
from user import views

app_name = "user"

urlpatterns = [
    path('register/',views.register2,name="register2"),
    path('login/',views.login2,name="login2"),
    path('logout/',views.logout2,name="logout2"),
    #path('logout/',views.logoutUser,name="logout")
]
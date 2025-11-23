from django.urls import path

from . import views

urlpatterns = [
    path('', views.home , name='home'),
    path('userLogin/', views.userLogin , name='userLogin'),
    path('userRegister/', views.userRegister , name='userRegister'),
    path('userLogout/', views.userLogout , name='userLogout'),

]

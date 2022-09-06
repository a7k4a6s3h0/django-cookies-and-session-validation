from urllib import request
from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.home),
    path('user_login', views.user_login, name='user_login'),
    path('lgout',views.lgout),
    path('user_login',views.lgout),
    path('sign_out',views.sign_out),
    

]

from http.client import HTTPResponse
from urllib import request
from django.shortcuts import render,redirect
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.views.decorators.cache import never_cache

# Create your views here.

name = 'akash'
passw = 'ak123'


def home(request):
   if request.COOKIES.get('username') and request.COOKIES.get('password'):
      new_name = request.COOKIES.get('username')
      new_password = request.COOKIES.get('password')
      second_name = request.session['Username']
      second_pass = request.session['Password']
      if new_name == second_name and new_password == second_pass:
         return  redirect('/lgout')
      
   else:
      return render(request, 'index.html')    
  
   #return render(request, 'index.html')   

   

def user_login(request):
   if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        if username == name and password == passw:
        # Redirect to a success page.
          a= redirect('/lgout')
          a.set_cookie('username', username)
          a.set_cookie('password', password)
          request.session['Username'] = username
          request.session['Password'] = password
          return a   
                 
          # redirect to home page.
        else:   
             
         return render(request, 'index.html',{'name' : 'username and password are incorrect'})


   
@never_cache
def lgout(request):
   if request.COOKIES.get('username') and request.COOKIES.get('password'):

      return render(request, 'logout.html') 
   else:
      return redirect('/')


def sign_out(request):
   a=redirect('/')
   a.delete_cookie('sessionid')
   a.delete_cookie("username")
   a.delete_cookie('password')
   return a
   #return render(request, 'index.html')           
   
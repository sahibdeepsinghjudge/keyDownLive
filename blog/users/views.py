import email
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.models import User
from .models import UserDetail
import string,random
# Create your views here.

def user_home(request):
    return HttpResponse(request.user)

def login_page(request):
    if request.user:
        logout(request)
    context = {
        'title':"Login"
    }
    return render(request,"users/login.html",context)

def register_page(request):
    logout(request)
    context = {
        'title':"Register"
    }
    return render(request,"users/register.html",context)
def register_view(request):
    if request.POST:
        email = request.POST['email']
        try:
            User.objects.get(email=email)
            messages.danger(request,"Email already exist!Try loging in to your old account.")
            return redirect("/register/")
        except:
            full_name1 = request.POST['fullname']
            s_pass = request.POST['s_password']
            c_pass = request.POST['c_password']
            username = ''
            abc = list(string.ascii_lowercase)
            cap_abc = list(string.ascii_uppercase)
            full_name = full_name1.split(" ")

            while len(username) <= 8:
                    username+=random.choice(abc)
                    username+=random.choice(cap_abc)
            user_count = User.objects.all().count()
            username+=str(user_count+1)
            if len(full_name) == 2:
                first_name = full_name[0]
                last_name = full_name[1]
            else:
                first_name = full_name1 
                last_name = ""
            user_obj = User.objects.create(username=username,email=email,first_name=first_name,last_name=last_name)
            user_obj.set_password(s_pass)
            user_obj.save()
            messages.success(request,"Account created successfully. Happy writing.")
            return redirect("/")
def login_view(request):
    email = password = ''
    if request.POST:
        email = request.POST['email']
        password = request.POST['password']
        try:
            user_obj = User.objects.get(email  = email)
            user = authenticate(username=user_obj.username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/')
            else:
                messages.warning(request,"Username or  password invalid!")
        except User.DoesNotExist:
            messages.warning(request,"Email you entered doesn't exist!")
            return redirect('/login/')
        
    return render(request,'users/login.html')

def logout_view(request):
    logout(request)
    return redirect('/login/')

def profile(request,username):
    try:
        user =  User.objects.get(username = username)
          
        userData = UserDetail.objects.get(username = request.user)
        context = {
            'user':user,
            'userData':userData,
        }
        return render(request,"users/profile.html",context)
    except User.DoesNotExist:
        messages.warning(request,'User not found!')
        return redirect('/')
    
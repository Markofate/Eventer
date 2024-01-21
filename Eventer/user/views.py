from django.shortcuts import render,redirect
from .models import Users
from .serializers import UserSerializer
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.renderers import TemplateHTMLRenderer
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from .forms import userForm


# Create your views here.


def login(request):
    form = userForm()
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        
        user = auth.authenticate(username= username, password= password)
        
        if user is not None:
            auth.login(request, user)
            messages.add_message(request, messages.SUCCESS, "Logged in succesfully")
            return redirect('index')
        else:
            messages.add_message(request, messages.ERROR, "Password or username is incorrect")
            return redirect('login')  
    else:      
        return render(request, 'user/login.html')


def register(request):
    form = userForm()
    if request.method == 'POST':
        print("Submitted")
        username = request.POST["username"]
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        email = request.POST["email"]
        phone = request.POST["phone"]
        password = request.POST["password"]
        repassword = request.POST["repassword"]
        
        form = userForm(request.POST)
        
        #USER KAYDI YAPILACAK #kendi user modelimi kullanıyorum ama django modeline de geçiş yapılabilir
        if password==repassword:
            #username control
            if Users.objects.filter(username = username).first():
                messages.add_message(request, messages.WARNING, "Username is taken")
                return redirect('register')
            elif Users.objects.filter(email = email).exists():
            #email control
                messages.add_message(request, messages.WARNING, "Email is already used")
                return redirect('register')
            else:
               if form.is_valid():
                actual_save = form.save(commit=False)
                actual_save.password = make_password(form.cleaned_data["password"])
                actual_save.status = 1
                actual_save.save()
                return redirect('login')
               else:     
                   print("form is not valid")
                   return redirect('register')  
        else:
            print(password,repassword)
            messages.add_message(request, messages.ERROR, "Passwords do not match")
            return redirect('register')    
    else:    
        return render(request, 'user/register.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.add_message(request, messages.SUCCESS, 'Logged out')
        return redirect('index')

@api_view(['GET','POST'])
def api_user(request):
    if request.method=='GET':
        users = Users.objects.all()
    
        serializer = UserSerializer(users,many=True)
    
        return JsonResponse(serializer.data,safe=False)
    
    
    if request.method=='POST':
       serializer = UserSerializer(data=request.data)
       if serializer.is_valid():
           serializer.save()
           return JsonResponse(serializer.data,safe=False, status=status.HTTP_201_CREATED)
       else:
           return Response(print(serializer.errors))

def api_user_single(request,id):
    users = Users.objects.get(pk=id)
    
    serializer = UserSerializer(users,many=False)
    
    return JsonResponse(serializer.data,safe=False)

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


# Create your views here.

@api_view(['GET','POST'])
def login(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        
        user = auth.authenticate(username= username, password= password)
        if Users is not None:
            auth.login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            print("Logged in")
            return redirect('index')
        else:
            print(password,username)
            print("Password or username is incorrect")
            return redirect('login')  
    else:      
        return render(request, 'user/login.html')

@api_view(['GET','POST'])
def register(request):
    if request.method == 'POST':
        print("Submitted")

        serializer = UserSerializer(data=request.data, many=True)
        if serializer.is_valid():
            username = request.POST["username"]
            first_name = request.POST["first_name"]
            last_name = request.POST["last_name"]
            email = request.POST["email"]
            phone = request.POST["phone"]
            password = request.POST["password"]
            repassword = request.POST["repassword"]
        #USER KAYDI YAPILACAK #kendi user modelimi kullanıyorum ama django modeline de geçiş yapılabilir
            if password==repassword:
            #username control
                if Users.objects.filter(username = username).first():
                    print("Username is already used")
                    return redirect('register')
                elif Users.objects.filter(email = email).exists():
                #email control
                    print("Email is already used")
                    return redirect('register')
                else:
                    
                    user = Users.objects.create(username= username,
                        first_name= first_name, last_name= last_name,
                        email= email, phone=phone, password= password)
                    
                    user.set_password(password)
                    print("User created")
                    return redirect('login')         
            else:
                print(password,repassword)
                print("Passwords do not match")  
                return redirect('register') 
        else:
            print("not valid")
            return Response(print(serializer.errors))    
    else:    
        return render(request, 'user/register.html')


def logout(request):
    return render(request, 'user/logout.html')

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
           return Response(serializer.data, status=status.HTTP_201_CREATED)
       else:
           return Response(print(serializer.errors))

def api_user_single(request,id):
    users = Users.objects.get(pk=id)
    
    serializer = UserSerializer(users,many=False)
    
    return JsonResponse(serializer.data,safe=False)
    
    

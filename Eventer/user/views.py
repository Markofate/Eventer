from django.shortcuts import render,redirect
from .models import User

# Create your views here.


def login(request):
    return render(request, 'user/login.html')


def register(request):
    if request.method == 'POST':
        print("Submitted")
        
        username = request.POST["username"]
        first_name = request.POST["name"]
        last_name = request.POST["lastname"]
        email = request.POST["email"]
        phone = request.POST["phone_number"]
        password = request.POST["password"]
        repassword = request.POST["repassword"]
        #USER KAYDI YAPILACAK 
        if password==repassword:
            #username kontrol
            if User.objects.filter(username = username).exists():
                print("Username is already used")
                return redirect('register')
            elif User.objects.filter(email = email).exists():
                print("Email is already used")
                return redirect('register')
            else:
                user = User.objects.create(username=username,
                first_name=first_name,last_name=last_name,
                email=email,phone=phone,password=password)
                
                print("User crated")
                return redirect('login')
        else:
            print("Passwords do not match")  
            return redirect('register') 
    else:    
        return render(request, 'user/register.html')


def logout(request):
    return render(request, 'user/logout.html')

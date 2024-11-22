from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages

# Create your views here.
def register(request):

    if request.method=='POST':
        user_name = request.POST['username']
        e_mail = request.POST['email']
        password_1 = request.POST['password1']
        password_2 = request.POST['password2']

        if password_1==password_2:
            if User.objects.filter(username=user_name).exists():
                messages.info(request,"Username taken")
                return redirect('register')
            elif User.objects.filter(email=e_mail).exists():
                messages.info(request,"Email taken")
                return redirect('register')
            else:
                user = User.objects.create_user(username=user_name, email=e_mail, password=password_1)
                user.save()
                print("user created")
                return redirect('/')
        else:
            messages.info(request,"Passwords aren't matching")
            return redirect('register')


        
        
    else:
        return render(request,'register.html')

def login(request):
    if request.method=='POST':
        u_name=request.POST['username']
        pwd=request.POST['password']
        user=auth.authenticate(username=u_name,password=pwd)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Invalid Credentials')
            return redirect('login')
        
    else:
        return render(request,'login.html')
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth

# Create your views here.
def register(request):

    if request.method=='POST':
        user_name = request.POST['username']
        e_mail = request.POST['email']
        password_1 = request.POST['password1']
        password2 = request.POST['password2']
        user = User.objects.create_user(username=user_name, email=e_mail, password=password_1)
        user.save()
        print("user created")
        return redirect('/')
        
    else:
        return render(request,'register.html')
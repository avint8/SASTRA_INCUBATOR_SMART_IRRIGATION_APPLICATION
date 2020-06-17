from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth

def register(request):
    if request.method == "POST":
        user= request.POST['user']
        password = request.POST['password']
        user = User.objects.create_user(username=user,password=password)
        user.save()
        return redirect('/login')

    return render(request,'register.html')

def login(request):
    if request.method == "POST":
        user= request.POST['user']
        password = request.POST['password']
        user = auth.authenticate(username=user,password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
    return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')
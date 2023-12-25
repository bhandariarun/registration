from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .models import Client
import bcrypt
from django.contrib import messages

# Create your views here.
# def login(request):
#     return render(request, 'login.html')


# myapp/views.py

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        fname = request.POST['fname']
        mname = request.POST['mname']
        lname = request.POST['lname']
        phone = request.POST['phone']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        if password == cpassword:
            myuser = User.objects.create_user(username=username, email=email, password=cpassword)
            # myuser = User.objects.create_user(username,email,cpassword)
            myuser.first_name = fname
            myuser.last_name = lname
            myuser.save()
            # request.session['id'] = myuser.id
            return redirect('/signin')
        else:
            messages.error(request, 'Passwords do not match')
    # return HttpResponse('Hello')
    return render(request, "authentication/signup.html")


def signin(request):
    if request.method == 'POST':
        email = request.POST['email']
        username = request.POST['username']
        cpassword = request.POST['cpassword']

        
        if (User.objects.filter(email=email).exists()):
            users = User.objects.filter(email=email)[0]
            if (request.POST['cpassword'].encode(), users.password.encode()):
                user = authenticate(email=email, username=username, password=cpassword)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'Login Successfully')
                    return HttpResponse('Login Successfully')

        else:
            messages.error(request, 'Bad Credentials!')
            return HttpResponse('Bad Credentials')

    return render(request, "authentication/signin.html")



def logout(request):
    return render(request, 'logout.html')


def index(request):
    return render(request, 'index.html')
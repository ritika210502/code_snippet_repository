from django.shortcuts import render,redirect
from snippetApp.models import Code
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def register_page(request):
    if request.method=="POST":
        firstname=request.POST.get('firstname')
        lastname=request.POST.get('lastname')
        email=request.POST.get('email')
        username=request.POST.get('username')
        password=request.POST.get('password')

        if User.objects.filter(username=username).exists():
            messages.error(request,'Invalid Username')
            return redirect('/login/')

        user=User.objects.create(
            first_name=firstname,
            last_name=lastname,
            email=email,
            username=username
        )
        user.set_password(password)
        user.save()
        messages.info(request, "Account created sucessfully")
        return redirect('/register/')

    return render(request,"register.html")


def login_page(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        
        if not User.objects.filter(username=username).exists():
            messages.error(request,'Invalid Username')
            return redirect('/login/')
        
        user= authenticate(username=username, password=password)
        if user is None:
            messages.error(request,'Invalid Password')
            return redirect('/login/')
        else:
            login(request,user)
            messages.info(request,'Login Sucessfully')

            return redirect('/add_codeSnippet/')
    return render(request,"login.html")

def logout_page(request):
    logout(request)
    return redirect('/login/')

@login_required(login_url="/login/")
def add_codeSnippet(request):
    print("Inside add_codeSnippet view")

    if request.method == "POST":
        title = request.POST.get('title')
        code_content = request.POST.get('code_content')
        language = request.POST.get('language')
        tags = request.POST.get('tags')

        Code.objects.create(title=title, code_content=code_content, language=language, tags=tags, user=request.user)
        return redirect('/add_codeSnippet/')

    return render(request, "index.html")


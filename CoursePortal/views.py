from django.shortcuts import render,redirect
from .models import Contact,Enrollment
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout

# Create your views here.
def index(request):
    return render(request, 'index.html',{})


def about(request):
    return render(request,'about.html',{})

def courses(request):
    return render(request,'courses.html',{})

def contact(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        subject=request.POST["subject"]
        message=request.POST['message']

        new_contact=Contact.objects.create(name=name,email=email,subject=subject,message=message)
        # new_contact.save()   if we want to add paramter using this new_con object then .save() method should write.

        return redirect('/contact')
    return render(request,'contact.html',{})

def team(request):
    return render(request,'team.html',{})


def testimonial(request):
    return render(request,'testimonial.html',{})


def error404(request):
    return render(request,'404.html',{})

def sign_up(request):
    if request.method=='POST':
        fullname=request.POST['name']
        email=request.POST['email']
        password=request.POST['pwd']
        confirmpassword=request.POST['conpwd']

        if password==confirmpassword:
            u = User.objects.create_user(username=email,email=email,password=password)
            return redirect('/login')
        else:
            print("password is not match")
            
            return redirect('/signup')
    return render(request,'sign_up.html',{})

def userlogin(request):
    if request.method=='POST':
        username=request.POST['email']
        password=request.POST['pwd']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            print("you have successfully login")
            return redirect('/')    # 

        else:
            print("Invalid Credentials")
            return redirect('/login')  # url/action at the time on redirect
        
    return render(request,'login.html',{})   # html page at the time of render

def joinnow(request):
    if request.method=='POST':
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        email=request.POST['email']
        contact=request.POST['contact']
        city=request.POST['city']
        coursepreferences=request.POST['course']
        price=request.POST['price']
      
        new_user=Enrollment.objects.create(first_name=firstname,last_name=lastname,email=email,contact=contact,city=city,course_preferences=coursepreferences,price=price)
        
        return redirect('/join_now')
    return render(request,'join_now.html',{})

def web_design(request):
    return render(request,'web_design.html',{})


def logout_view(request):
    logout(request)
    return redirect('/')
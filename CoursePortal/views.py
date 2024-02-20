from django.shortcuts import render,redirect
from .models import Contact,Enrollment,Course
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from django.views.generic import DetailView
from django.db.models import Count
from django.conf import settings
from django.core.mail import send_mail



# Create your views here.
def index(request):
    courses=Course.objects.all()
    categories_with_count = Course.objects.values('category').annotate(count=Count('id'))
    # print(categories_with_count)

    category_counts = [(item['category'], item['count']) for item in categories_with_count]

    categories_in_dictionary={}
    for category, count in category_counts:
        # print(f"Category: {category}, Count: {count}")
        categories_in_dictionary[category]=count
    return render(request, 'index.html',{'Courses':courses,'categories_in_dictionary':categories_in_dictionary})


def about(request):
    return render(request,'about.html',{})

def courses(request):
    courses=Course.objects.all()
    # print('Courses',courses)

    categories_with_count = Course.objects.values('category').annotate(count=Count('id'))
    # print(categories_with_count)

    category_counts = [(item['category'], item['count']) for item in categories_with_count]

    categories_in_dictionary={}
    for category, count in category_counts:
        # print(f"Category: {category}, Count: {count}")
        categories_in_dictionary[category]=count

    # print("Dictionary",categories_in_dictionary)
    return render(request,'courses.html',{'Courses':courses,'categories_in_dictionary':categories_in_dictionary})

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
            u.fullname = fullname  # Assign fullname to user object
            u.save()
            try:
                subject = 'Welcome to e-Learning platform'
                message = f'Hi {u.fullname}, thank you for registering in e-Learning.Enjoy Technical Journey with e-Learning.'
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [u.email, ]
                send_mail( subject, message, email_from, recipient_list )

            except:
                print("Failed to send Mail")
            
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
            return redirect('/login')  # url/action at the time of redirect
        
    return render(request,'login.html',{})   # html page at the time of render

def joinnow(request,id):
   
    if request.method=='POST':
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        email=request.POST['email']
        contact=request.POST['contact']
        city=request.POST['city']
        coursepreferences=request.POST.get('course')
        price=request.POST['price']
      
        print(coursepreferences)
        new_user=Enrollment.objects.create(first_name=firstname,last_name=lastname,email=email,contact=contact,city=city,course_preferences=coursepreferences,price=price)
        return redirect('/')
     
    if id==0:
        return render(request,'join_now.html',{})
    else:
        displaycourse=Course.objects.get(id=id)
        course=displaycourse
        price=displaycourse.price
        return render(request,'join_now.html',{'price':price,'course':displaycourse})
       
       


def course_view(request,id):
    displaycourse=Course.objects.get(id=id)

    return render(request,'course-view.html',{'displaycourse':displaycourse})


def logout_view(request):
    logout(request)
    return redirect('/')

def category_courses(request,category):
 
    courses=Course.objects.all()
    category_courses=Course.objects.filter(category=category)
    current_category=category.replace('_', ' ')
    return render(request,'category_courses.html',{'Category_courses':category_courses,'current_category':current_category})





from django.urls import path, re_path
from django.contrib.auth.views import LogoutView

# from django.conf.urls import url
from . import views
app_name = 'CoursePortal'

urlpatterns = [
    path('',views.index, name="index" ),
    path('about/',views.about,name="aboutus" ),
    path('courses/',views.courses,name="courses" ),
    path('contact/',views.contact,name="contact" ),
    path('team/',views.team,name="team" ),
    path('testimonial/',views.testimonial,name="testimonial" ),
    path('error404/',views.error404,name="error404" ),
    path('signup/',views.sign_up,name="sign_up" ),
    path('login/',views.userlogin,name="login" ),
    path('join_now/',views.joinnow,name="joinnow" ),

    path('web_design/',views.web_design,name="web_design" ),
    path('logout/', views.logout_view, name='logout')
]
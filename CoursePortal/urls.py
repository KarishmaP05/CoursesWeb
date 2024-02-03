from django.urls import path, re_path

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
    path('error404/',views.error404,name="error404" )
]
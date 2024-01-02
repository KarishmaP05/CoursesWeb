from django.urls import path, re_path

# from django.conf.urls import url
from . import views
app_name = 'CoursePortal'

urlpatterns = [
    path('',views.index, name="index" )
]
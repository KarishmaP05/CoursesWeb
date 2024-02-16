from django.db import models
from datetime import date
from ckeditor.fields import RichTextField

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    subject = models.CharField(max_length=300)
    date = models.DateField(default=date.today())
    message = models.TextField()

    def __str__(self):
        return self.name
    

class Course(models.Model):
    name= models.CharField(max_length=50)
    price=models.FloatField()
    mrp=models.FloatField()
    faculty_name=models.CharField(max_length=50)
    duration = models.CharField(max_length=10) 
    intake=models.IntegerField()
    course_img = models.ImageField(upload_to ='uploads/',height_field=None, width_field=None) 


    CATEGORY_CHOICES = (
         
         
        ("web_design", 'Web Design'),
        ("graphics_design", 'Graphic design'),
        ("video_editing", 'Video Editing'),
        ("online_marketing", 'Online Marketing')
    )

    category = models.CharField(max_length=200, choices=CATEGORY_CHOICES, default="web_design")
    
    to_be_listed = models.BooleanField(default=True)
    description = RichTextField()

    def __str__(self):
            return self.name
    
    def set_duration(self, hours):
        self.duration = f"{hours} hrs"
   
  
class Enrollment(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    contact=models.IntegerField()
    city=models.CharField(max_length=50)
    course_preferences=models.CharField(max_length=50)
    price=models.FloatField()

    def __str__(self):
        return self.first_name
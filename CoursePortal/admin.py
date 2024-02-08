from django.contrib import admin
from .models import Contact
from .models import Course
from .models import Enrollment
# Register your models here.

admin.site.register(Contact)


admin.site.register(Course)

admin.site.register(Enrollment)


    
from django.contrib import admin
from . import models 

# Register your models here.

admin.site.register(models.Student)
admin.site.register(models.Lesson)
admin.site.register(models.Package)
admin.site.register(models.Course)

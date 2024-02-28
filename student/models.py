from django.db import models

class Student(models.Model):
    name        = models.CharField( max_length=50,null=False, blank =False)
    description = models.TextField(default = 'This is a student.' )
    
    
    def __str__(self) -> str:
        return f'student name:{self.name}'
        

class Lesson(models.Model):
    name        = models.CharField( max_length=50,null=False, blank =False)
    description = models.TextField(default = 'This is a lesson.' )
    
    
    def __str__(self) -> str:
        return f'lesson name:{self.name}'
        
        

class Package(models.Model):
    name        = models.CharField( max_length=50,null=False, blank =False)
    description = models.TextField(default = 'This is a package.' )
    
    
    def __str__(self) -> str:
        return f'lesson name:{self.name}'
        

class Course(models.Model):
    package = models.ForeignKey(Package, on_delete = models.CASCADE)
    lesson  = models.ForeignKey(Lesson , on_delete = models.CASCADE) 
    student = models.ManyToManyField(Student)
    
    name        = models.CharField( max_length=150,null=False, blank =False)
    description = models.TextField(default = 'This is a Course.' )
    
    def __str__(self) -> str:
        return f'lesson name:{self.name}'
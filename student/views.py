from django.shortcuts import render
from .models import *
from django.db.models import Q


def index(request):
    std = Student.objects.all()
    
    print(std)
    print(std.query) # Show Query language
    
    return render(request, 'student/student.html',{'student' : std})

def filter(request):
    # Filter
    # std= Student.objects.filter(name='ali')                       # Select Student with name = 'ali'
    # std = Student.objects.filter(name__startswith='a')            # Select Student name start with = 'a'
    # std = Student.objects.filter(name__endswith='a')                # Select Student name start with = 'a'
    std = Student.objects.filter(description__contains='This')      # Select Student description contains = 'this'
    
    print(std)
    print(std.query) # Show Query language
    
    #! Filter Query
    # <QuerySet [<Student: student name:ali>,
    #            <Student: student name:ahmad>,
    #            <Student: student name:sara>,
    #            <Student: student name:darab>,
    #            <Student: student name:jamsh>
    #            , <Student: student name:Bahar>]>
    # 
    # SELECT "student_student"."id",
    # "student_student"."name",
    # "student_student"."description" 
    # FROM "student_student" WHERE "student_student"."description" LIKE %This% ESCAPE '\'
    
    return render(request, 'student/student.html',{'student' : std})

def complex_filter(request):
    
    # Find Student that pass art lession
    # STUDENT TABLE have many to many relation with COURSE TABLE
    # IN COURSE TABLE we have forigen key:lesson thar refeer to LESSON TABLE
    # LESSON TABLE evry lesson have name like art,language,math, ...
    
    std = Student.objects.filter(course__lesson__name='language')      
    
    
    # وقتی دو جدول باهم رابطه چند به چند داشته باشند
    # یک جدوا جانکشن حاوی اترباطات آنها ساخته می شود
    
    print(std.query) # Show Query language
    #! Filter Query
    # SELECT "student_student"."id", "student_student"."name", "student_student"."description"
    # FROM "student_student" 
    # INNER JOIN "student_course_student" 
    # ON ("student_student"."id" = "student_course_student"."student_id") 
    # INNER JOIN "student_course" 
    # ON ("student_course_student"."course_id" = "student_course"."id") 
    # INNER JOIN "student_lesson" 
    # ON ("student_course"."lesson_id" = "student_lesson"."id") 
    # WHERE "student_lesson"."name" = art
    
    # student_course_student is Janction Table
    
    return render(request, 'student/student.html',{'student' : std})

def MultiFilter(request):
    # Find Package : use 2 conditions :AND -> & Or -> |
    # course include : lesson art & student ali
    
    # Method 1
    # std = Package.objects.filter(course__lesson__name='art', course__student__name='ali')     

    # Method 2 (AND)
    # std = Package.objects.filter(course__lesson__name='Math') & Package.objects.filter(course__student__name='ali')     

    # Method 3 (OR)
    std = Package.objects.filter(course__lesson__name='Math') | Package.objects.filter(course__student__name='ali')     


    print(std.query) # Show Query language
    #! Filter Query
    
    # SELECT "student_student"."id", "student_student"."name", "student_student"."description" 
    # FROM "student_student" 
    # INNER JOIN "student_course_student" 
    # ON ("student_student"."id" = "student_course_student"."student_id") 
    # INNER JOIN "student_course" 
    # ON ("student_course_student"."course_id" = "student_course"."id") 
    # INNER JOIN "student_lesson" 
    # ON ("student_course"."lesson_id" = "student_lesson"."id") 
    # INNER JOIN "student_course_student" T5 ON ("student_course"."id" = T5."course_id") 
    # INNER JOIN "student_student" T6 ON (T5."student_id" = T6."id") 
    # WHERE ("student_lesson"."name" = art AND T6."name" = ali)
    
    return render(request, 'student/student.html',{'student' : std})


def MultiQueryFilter(request):
    # simple way for use Multi Conditions


    # Method 1 
    # std = Package.objects.filter(
    #     Q(course__lesson__name='Math') |
    #     Q(course__student__name='ali') )

    # Method 2
    # std = Package.objects.filter(
    #     Q(course__lesson__name='Math') &
    #         (
    #         Q(course__student__name='diu') |
    #         Q(course__student__name__startswith='d')
    #         )
    # )
    
    # Method 4
    # اولویت در کد با کیوفانکشن هست
    # std = Package.objects.filter(
    #     Q(course__lesson__name='Math') &
    #         (
    #         Q(course__student__name='diu') |
    #         Q(course__student__name__startswith='d')
    #         )
    # )


    print(std.query) # Show Query language
    #! Filter Query
    
    return render(request, 'student/student.html',{'student' : std})

from django.shortcuts import render
from .models import *
from django.db.models import Q
import time 
from django.db import connection,reset_queries

def debugger(func):
    def wrapper(*args ,**kwargs):
        reset_queries()
        st      = time.time()
        value   = func(*args ,**kwargs)
        et      = time.time()
        queries = len(connection.queries)
        print('--'*5)
        print(f" connection number: {queries}")
        print(f" take time :{(et -st):.3f}")
        print('--'*5)
        return value
    return wrapper
        
def index(request):
    std = Student.objects.all()
    
    print(std)
    print(std.query) # Show Query language
    return render(request, 'student/student.html',{'student' : std})

#!-----------------------------------------------------------------------------------+
#!                                   Filter-Q-And Or                                 |                                                   
#!-----------------------------------------------------------------------------------+
#region
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
    
    # Method 3
    # اولویت در کد با کیوفانکشن هست
    # std = Package.objects.filter(
    #     Q(course__lesson__name='Math') &
    #         (
    #         Q(course__student__name='diu') |
    #         Q(course__student__name__startswith='d')
    #         )
    # )
    
    # Method 4 
    # First Fliter base "Math" then filter base 'ali'
    std = Package.objects.filter(course__lesson__name='Math').filter(course__student__name='ali') 

    print(std.query) # Show Query language
    #! Filter Query
    
    return render(request, 'student/student.html',{'student' : std})
#endregion

#!-----------------------------------------------------------------------------------+
#!         ~Q - exclude - distinct - orderby - values - values_list - reverse         |                                                   
#!-----------------------------------------------------------------------------------+
#region

def Not_Q_exclude(request):
    # Give all Package Except student`s that learn math    -> by: ~Q        : not Condidition
    # And remove ali from our list                         -> by: exclude   : remove simple from filter
    
    
    # std = Package.objects.filter(~Q(course__lesson__name='Math')).exclude(name='ali')
    #Or 
    # std = Package.objects.filter(~Q(course__lesson__name='Math')).exclude(name__in=['ali','ahmad'])
    
    std = Student.objects.filter(~Q(course__lesson__name='Math')).exclude(name__in=['ali','ahmad'])

    print(std.query) # Show Query language
    return render(request, 'student/student.html',{'student' : std})

def valuesfunction(request):
    # برای دست یابی به اطلاعات سایر جدول های که با هم جوین شده اند
    std = Package.objects.filter(course__lesson__name='Math').values("name","course__name","course__description","course__lesson__name")

    print("Dictionary ",std) # Show Query language
    #! NOTE
    ## output of std is dictionary: 
    # <QuerySet [{'name': 'Package_one', 'course__name': 'Course 1', 'course__description': 'This is a Course 1', 'course__lesson__name': 'Math'}]>
    
    print(std.query) # Show Query language
    return render(request, 'student/Values.html',{'student' : std})

def values_list_function(request):
    # برای دست یابی به اطلاعات سایر جدول های که با هم جوین شده اند
    std = Package.objects.filter(course__lesson__name='Math').values_list("name","course__name","course__description","course__lesson__name")

    print("Tuple ",std) # Show Query language
    #! NOTE
    ## output of std is tuple: 
    # <QuerySet [('Package_one', 'Course 1', 'This is a Course 1', 'Math')]>
    print(std.query) # Show Query language
    return render(request, 'student/Values_list.html',{'student' : std})

def distinct_function(request):
    # برای جلوگیری از ردیف های مشابه
    std = Package.objects.filter(course__student__name='ahmad')
    ## باید از دیستینک استفاده کنیم
    std = Package.objects.filter(course__student__name='ahmad').distinct()
    return render(request, 'student/student.html',{'student' : std})

def orderby_function(request):
    
    # std = Package.objects.filter(course__student__name='ahmad').order_by("course__student__name").values("name","course_student__nsme","course__name","course__description")
    # Asendibg
    # std = Package.objects.all().order_by('course__student__name').values("name","course__student__name","course__name","course__description")

    # Desendibg
    # std = Package.objects.all().order_by('-course__student__name').values("name","course__student__name","course__name","course__description")
    
    #Order Base to item
    std = Package.objects.all().order_by('course__student__name',"course__name").values("name","course__student__name","course__name","course__description")
    
    return render(request, 'student/Values.html',{'student' : std})

#endregion

#!-----------------------------------------------------------------------------------+
#!                              select_related - prefetch_related                    |                                                   
#!-----------------------------------------------------------------------------------+
#region

# برای کاهش زمان پاسخ
# select_related & prefetch_related-> reduce connection and Time
# select_related   -> its use for foreginkey or one to one field like "lesson"
# prefetch_related -> its use for many to many field like "student"

#?-------------------------------------+
#?               select_related        |
#?-------------------------------------+
@debugger
def related_function(request):
    # پیدا کردن عناصری که هی دی زیر  دارند
    # courses = Course.objects.filter(id__lte=5)  
    courses = Course.objects.select_related("lesson").filter(id__lte=5)
    
    FullCourse = []
    for course in courses:
        if course.lesson.name=="math":
            FullCourse.append(f"Lesson : {course.lesson.name} pre course:{course.name}")
            
        else:
            FullCourse.append(f"Lesson : {course.lesson.name} course:{course.name}")

    return render(request, 'student/student.html',{'student' : FullCourse})
#?-------------------------------------+
#?            prefetch_related         |
#?-------------------------------------+

@debugger
def prefetch_function(request):
    
    courses = Course.objects.prefetch_related("student").filter(id__lte=5)
    FullCourse = []
    for course in courses:
        if course.lesson.name=="art":
            # above we fetch course.student.all  by -> courses = Course.objects.select_related("student").filter(id__lte=5)
            students = [student.name for student in course.student.all()]
            FullCourse.append({"course":f"Lesson : {course.lesson.name} pre course:{course.name}","students":students})
            
        else:
            students = [student.name for student in course.student.all()]
            FullCourse.append({"course":f"Lesson : {course.lesson.name} course:{course.name}","students":students})

    return render(request, 'student/prefetch.html',{'FullCourse' : FullCourse})
#?-------------------------------------+
#? We can use some ralatad together    |
#?-------------------------------------+
@debugger
def prefetch_Multi_related(request):
    
    courses = Course.objects.prefetch_related("lesson","student").filter(id__lte=5)
    FullCourse = []
    for course in courses:
        if course.lesson.name=="art":
            # above we fetch course.student.all  by -> courses = Course.objects.select_related("student").filter(id__lte=5)
            students = [student.name for student in course.student.all()]
            FullCourse.append({"course":f"Lesson : {course.lesson.name} pre course:{course.name}","students":students})
            
        else:
            students = [student.name for student in course.student.all()]
            FullCourse.append({"course":f"Lesson : {course.lesson.name} course:{course.name}","students":students})

    return render(request, 'student/prefetch.html',{'FullCourse' : FullCourse})

#endregion

from django.shortcuts import render
from .models import *
from django.db.models import Avg,Count,Max,Min,Sum,IntegerField
# Create your views here.

def index(request):
    books = Book.objects.all().values('name','price','rating')
    return render(request,"bookstore/index.html",{"books":books} )

#!--------------------------------+
#!          aggregate             |                                                   
#!--------------------------------+
#region


#  Include:
#     + Average
#     + count
#     + max
#     + min
#     + sum

# aggregate actions on all
# annotate actions on each
    

def aggregate_fuction(request):
    
    # books = Book.objects.all().values('name','price','rating').aggregate(books_avg = Avg("price"))
    # output of aggregate is -> Dictionary -> {'books_avg': Decimal('749.634545454545')}
    
    #Get All number of books in all store
    books = Store.objects.aggregate(All_books = Count("books"))
    # output of aggregate is -> Dictionary -> {'All_books': 25}
    print(books)
    return render(request,"bookstore/index.html",{"books":books} )


def aggregate_Multi(request):
    
    #Get All number of books in all store
    # books = Store.objects.aggregate(All_books = Count("books"),
    #                                 price_max = Max("books__price") ,
    #                                 rate_avg  = Avg("books__rating",output_field = IntegerField()),
    #                                 book_sum  = Sum("books__price")
    #                                 )
    # output of aggregate is -> Dictionary ->
    # {
    #     'All_books': 25, 'price_max': Decimal('987.670000000000'),
    #     'rate_avg': 2.28, 'book_sum': Decimal('9253.95000000000')
    # }
    
    # Filter on Store : bagh e ketab
    books = Store.objects.filter(name="bagh e ketab").aggregate(All_books = Count("books"),
                                    price_max = Max("books__price"),
                                    rate_avg  = Avg("books__rating",output_field = IntegerField()),
                                    book_sum  = Sum("books__price")
                                )
    print(books)
    return render(request,"bookstore/multi.html",{"books":books} )

#!-------------------------------------+
#!                 annotate            |                                                   
#!-------------------------------------+

# aggregate actions on all
# annotate actions on each

def annotate_function(request):
    # هر یک کتاب چند نویسنده دارد
    # books = Book.objects.all().annotate(authers_count=Count("authers"))
    
    # هر فروشگاه چند کات برای فروش دارد
    stores = Store.objects.annotate(books_count=Count("books"))


    print(stores)
    return render(request,"bookstore/index.html",{"books":stores} )

#endregion




from django.db import models


class Auther(models.Model):
    name = models.CharField(max_length = 200)
    age  = models.IntegerField()
    
    def __str__(self) -> str:
        return self.name
    
class Publisher(models.Model):
    name = models.CharField(max_length = 300)
    
    def __str__(self) -> str:
        return self.name
    
class Book(models.Model):
    name   = models.CharField(max_length =300)
    page   = models.IntegerField()
    price  = models.DecimalField(max_digits =10 , decimal_places=2)
    rating = models.FloatField()
    authers   = models.ManyToManyField(Auther)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    pubdate   = models.DateField()
    
    def __str__(self) -> str:
        return self.name
    
class Store(models.Model):
    name  = models.CharField(max_length =300)
    books = models.ManyToManyField(Book)
    def __str__(self) -> str:
        return self.name
    
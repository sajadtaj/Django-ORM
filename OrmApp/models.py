from django.db import models

Instrument_CHOICES = [
    ("Flute", "f"),
    ("Harp", "h"),
    ("Cello", "c"),
    ("Drums", "d"),
    ("Guitar", "g"),
    ("Saxophone", "a"),

]

class Musician(models.Model):
    first_name = models.CharField(verbose_name="person's first name" , max_length=50, default ='ali')
    last_name  = models.CharField(verbose_name="person's last name" , max_length=50, default ='ahmadi')
    instrument = models.CharField( max_length=100,choices=Instrument_CHOICES)

    def __str__(self):
        return self.first_name
    class Meta:
        ordering = ["last_name"]
    #     db_table= 'Musician'

class Album(models.Model):
    artist       = models.ForeignKey(Musician, on_delete=models.CASCADE)
    name         = models.CharField(verbose_name="Albums name" ,max_length=100)
    release_date = models.DateField(help_text = 'the year that Album published')
    num_stars    = models.IntegerField()
    def __str__(self):
        return self.name
    # class Meta:
    #     db_table= 'Album'

class Group(models.Model):
    name = models.CharField(verbose_name="Group`s name" ,max_length=128)
    members = models.ManyToManyField(Musician, through="Membership")
    def __str__(self):
        return self.name
    # class Meta:
    #     db_table= 'Group'

class Membership(models.Model):
    musician      = models.ForeignKey(Musician, on_delete=models.CASCADE)
    group         = models.ForeignKey(Group, on_delete=models.CASCADE)
    date_joined   = models.DateField()
    invite_reason = models.CharField(max_length=64)
    
    def __str__(self) -> str:
        return f'{self.musician}|{self.group}'

    # class Meta:
        # db_table= 'Membership'


# database relationships: many-to-one, many-to-many and one-to-one.

# many-to-one   
# To define a many-to-one relationship, use django.db.models.ForeignKey.
# It’s suggested, but not required,
# that the name of a ForeignKey field  be the name of the model, lowercase.

# many-to-many  
# To define a many-to-many relationship, use ManyToManyField.
# It’s suggested, but not required,that the name of a ManyToManyField be:
# a plural describing the set of related model objects.

# one-to-one    = 

#!-----------------------+
#!  Abstract-inheritance |
#!-----------------------+

class Base(models.Model):
    m2m = models.ManyToManyField(
        Musician,
        related_name="%(app_label)s_%(class)s_related",
        related_query_name="%(app_label)s_%(class)ss",
    )
    class Meta:
        abstract = True
        db_table = "Base"

# Parent -> Musician
class Person(Base):
    
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField()
    def baby_boomer_status(self):
        "Returns the person's baby-boomer status."
        import datetime
        if self.birth_date < datetime.date(1945, 8, 1):
            return "Pre-boomer"
        elif self.birth_date < datetime.date(1965, 1, 1):
            return "Baby boomer"
        else:
            return "Post-boomer"
        @property
        def full_name(self):
            "Returns the person's full name."
            return f"{self.first_name} {self.last_name}"
        
        def __str__(self) -> str:
            return f'{self.first_name}|{self.last_name}'

    class Meta(Base.Meta):
        db_table = "Person"
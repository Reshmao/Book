from django.db import models

# Create your models here.
"""
## models ---- which is used to perform certain actions using data CRUD(create,read/retrieve,update,delete)

class Employee(models.Model)
   charField()
   IntegerField()
   PositiveIntegerField()
   boolean

::ORM-- object-relational mapping layer

create class----> make migrations-----> Query language (using migrate)------> sqlite 
     "        (python manage.py makemigrations),(python manage.py migrate)
     " 
     "
   (views)  

"""
class Employee(models.Model):
    email=models.EmailField(null=True)  #unique=true
    uname=models.CharField(max_length=30)
    age=models.PositiveBigIntegerField()
    place=models.CharField(max_length=30)

    def __str__(self):
        return self.uname

class student(models.Model):
    name=models.CharField(max_length=30)
    age=models.PositiveIntegerField()
    email=models.EmailField(unique=True,null=True)
    place=models.CharField(max_length=30)
    gender=models.CharField(max_length=10)
    #subject=models.CharField(max_length=30)

    def __str__(self):
        return (self.name)

class Emp(models.Model):
    name=models.CharField(max_length=20)
    place=models.CharField(max_length=20)
    salary=models.PositiveIntegerField()
    contact=models.CharField(max_length=20)
    
class Book(models.Model):
    title=models.CharField(max_length=30)
    author=models.CharField(max_length=30)
    publication_year=models.CharField(max_length=20)
    genre=models.CharField(max_length=30)
    
    def __str__(self):
        return self.title

class Luminar(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField(unique=True,null=True)
    course=models.CharField(max_length=30)

class Students(models.Model):
    name=models.CharField(max_length=30)
    age=models.PositiveIntegerField()
    course=models.CharField(max_length=30)
    place=models.CharField(max_length=30)
    gender=models.CharField(max_length=10)  
    

    
    

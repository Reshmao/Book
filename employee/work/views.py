from django.shortcuts import render , redirect
# Create your views here.
from django.views.generic import View
from work.forms import Empform, BookForm, LuminarForm ,StudentForm
from work.models import Emp,Luminar,Book, Students

class Empview(View):
    def get(self,request):
        form=Empform
        return render(request,"add.html",{"form":form})
    
    def post(self,request):
        form=Empform(request.POST)
        print(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            Emp.objects.create(**form.cleaned_data)   #modelname.objects.create(**..)
            return render(request,"add.html",{"form":form})
        else:
            return render(request,"add.html",{"form":form}) 
        
class BookView(View):
    def get(self,request):
        form=BookForm()
        return render(request,'book.html',{'form':form})
    def post(self,request):
        form=BookForm(request.POST)
        if form.is_valid():

            """print(form.cleaned_data)
            book=form.cleaned_data.get("title")
            print(book)
            Book.objects.create(**form.cleaned_data)""" #ORM query
            """name=Book.objects.fetchall()
            print(name)"""

            form.save() # form.save() method to add the data into db without using ORM query (only for modelform)
            print("Created")

            form=BookForm()

            return render(request,'book.html',{'form':form})
        else:
            return render(request,'book.html',{'form':form})


#display all data in another page

class Booklist(View):
    def get(self,request):
        data=Book.objects.all()
        return render(request,'booklist.html',{'data':data})

## luminarview
class LuminarView(View):
    def get(self,request):
        form=LuminarForm()
        return render(request,'luminar.html',{'form':form})
    def post(self,request):
        form=LuminarForm(request.POST)
        if form.is_valid():

            form.save() 
            print("Created")

            form=LuminarForm()

            return render(request,'luminar.html',{'form':form})
        else:
            return render(request,'luminar.html',{'form':form})

## luminarlist
class Luminarlist(View):
    def get(self,request):
        data=Luminar.objects.all()
        return render(request,'luminarlist.html',{'data':data})

## bookdetails    
class Book_detailview(View):
    def get(self,request,*args,**kwargs):
        #id=4
    #(**kwargs)--provides with flexibility to use keyword arguments in our program. Using it as parameter,
    # we can eventually pass many arguments(requests)
        id=kwargs.get("pk")
        qs=Book.objects.get(id=id)
        return render(request,"bookd.html",{"data":qs})
    
class Studentsview(View):
    def get(self,request):
        form=StudentForm()
        return render (request,'students.html',{'form':form}) 
    def post (self,request):
        form=StudentForm(request.POST) 

        if form.is_valid():
            
            form.save()
            print(form.cleaned_data)
            form=StudentForm()

            return render(request,'students.html',{'form':form}) 
        else:
            return render(request,'students.html',{'form':form})    


class Book_delete(View):
    def get(self,request,*args,**kwargs):
        id = kwargs.get("pk")
        Book.objects.get(id=id).delete()
        return redirect('book-al')        

        
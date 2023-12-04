from django import forms
from work.models import Book, Luminar , Students


class Empform(forms.Form):
    name=forms.CharField()
    place=forms.CharField()
    salary=forms.IntegerField()
    contact=forms.CharField()

class BookForm(forms.ModelForm):
    class Meta:
        model=Book
        fields='__all__'
        
        #or 
        # fields=['title','author','publication_year','genre']   
        # 
class LuminarForm(forms.ModelForm):
    class Meta:
        model=Luminar
        fields='__all__'

class StudentForm(forms.ModelForm):
    class Meta:
        model=Students
        fields='__all__'        
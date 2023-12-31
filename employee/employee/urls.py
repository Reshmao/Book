"""
URL configuration for employee project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from work.views import Empview, BookView, Booklist ,LuminarView,Luminarlist,Book_detailview,Studentsview,Book_delete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('emp/',Empview.as_view()),
    path('book/',BookView.as_view()),
    path('bookall/',Booklist.as_view(), name="book-al"),
    path('lumi/',LuminarView.as_view()),
    path('lumiall/',Luminarlist.as_view()),
    path("books/<int:pk>",Book_detailview.as_view(), name="book-det"),
    path('student/',Studentsview.as_view()),
    path('bk/<int:pk>/remove',Book_delete.as_view(),name='book-del')



]

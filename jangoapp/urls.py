import csv
from django.contrib import admin
from django.urls import path
#from JangoProj.jangoapp.views import book_list
from jangoapp import views

urlpatterns = [
    path('',views.home,name="home"),
    path('test/',views.test,name="test"),
    path('contact/',views.contact,name="contact"),
    path('result/',views.result,name="result"),
    path('upload_book/',views.upload_book,name="upload_book"),
    path('book_list/',views.book_list,name="book_list"),
    path('book_delete/<int:pk>',views.book_delete,name="book_delete"),
    path('send_email/',views.send_email,name="send_email"),
    
    path('ssession/',views.ssession,name="ssession"),
    path('gsession/',views.gsession,name="gsession"),

    path('scookie/',views.scookie,name="scookie"),
    path('gcookie/',views.gcookie,name="gcookie"),

    path('csvs/',views.csvs,name="csvs"),
]

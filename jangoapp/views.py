from django.http import response
from django.http.response import HttpResponse
from django.shortcuts import  render,redirect
from .models import Contact,Books, Student
from .forms import BooksForm, StudentForm
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.core.mail import send_mail
import csv
from reportlab.pdfgen import canvas


# Create your views here.
def home(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile=request.FILES['myfile']
        fs=FileSystemStorage()
        filename=fs.save(myfile.name,myfile)
        url=fs.url(myfile)
        print('save')

    
    return render(request,'index.html',)

def test(request):
    if request.method== "POST":
        form=StudentForm(request.POST)        
        if form.is_valid():
            form.save()
            print('Data Save') 
    else:
        form=StudentForm()      
    da={'form': form}
    return render(request,'test.html',da)
    
def contact(request):

    if request.method== "POST":
        uname=request.POST['emname']
        uemail=request.POST['emmail']

        con=Contact(name=uname,email=uemail)
        con.save()
    records=Contact.objects.all()    
    d={'records': records}
    return render(request,'contact.html',d) 

def upload_book(request):
    if request.method=="POST":
        book=BooksForm(request.POST,request.FILES)
        if book.is_valid():
            book.save()
            print('Save')
            return redirect('book_list')
    else:
        book=BooksForm()

    return render(request,'upload_book.html',{'book':book} )     

def book_list(request):
    b=Books.objects.all()
    return render(request,'book_list.html',{'books':b})

def result(request):
    a=int(request.POST['num1'])
    b=int(request.POST['num2'])

    c=a+b

    return render(request,'result.html',{'sum':c} ) 
    #HttpResponse("<h1 align='center'><font color='red' face='algerian'>Welcome to Sabira's World</font></h1>")
def book_delete(request,pk):
    if request.method=='POST':
        book=Books.objects.get(pk=pk)
        book.delete()
    return redirect('book_list')

    #return HttpResponse("<script>alert('Welcome to DJ');</script>")
def send_email(request):
    if request.method=='POST':
        message=request.POST['message']
        send_mail('Testing',
            message,settings.EMAIL_HOST_USER,['sabir786pir@yahoo.com'],fail_silently=False)
    return render(request,'send_email.html')


 # Function For Session Set and Get
def ssession(request):
    request.session['ename']='Pride'
    request.session['email']='pride@gmail.com'
    return HttpResponse("Session are set")

def gsession(request):
    name=request.session['ename']='Pride'
    email=request.session['email']='pride@gmail.com'
    return HttpResponse("Name is :\t"+name+"\nEmail is :\t"+email)


# Function For Coocies Set and Get
def scookie(request):
    response=HttpResponse("Cookies are set")
    response.set_cookie('user','Pride')
    return response

def gcookie(request):
    name=request.COOKIES['user']
    return HttpResponse("Name is:"+name)


# Function For Creating CSV File
def csvs(request):
    response=HttpResponse(content_type='text/csv')
    response['Content-Disposition']='attachment; filename="file.csv"'
    st=Student.objects.all()
    writer=csv.writer(response)
    for s in st:
        writer.writerow([s.name,s.email,s.mobile])
    return response

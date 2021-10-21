from django.db import models
from django.db.models.fields.files import FileField

# Create your models here.
class Contact(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=255)
    email=models.EmailField(max_length=255)
    
    def __str__(self):
        return self.name


class Student(models.Model):
    rno=models.AutoField(primary_key=True)
    name=models.CharField(max_length=255)
    email=models.EmailField(max_length=255)
    mobile=models.CharField(max_length=255)

    def __str__(self):
       return self.name     

class Books(models.Model):
    title=models.CharField(max_length=255)
    author=models.CharField(max_length=255)
    pdf=FileField(upload_to='pdfs/',blank=True,null=True)

    def __str__(self):
        return self.title

class Register(models.Model):
    srno=models.AutoField(primary_key=True)
    name=models.CharField(max_length=255)
    email=models.EmailField(max_length=255)
    mobile=models.CharField(max_length=255)
    password=models.CharField(max_length=255)
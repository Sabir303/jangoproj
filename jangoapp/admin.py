from django.contrib import admin
from .models import  Contact, Student, Books,Register


# Register your models here.
admin.site.register(Contact)
admin.site.register(Student)
admin.site.register(Books)
admin.site.register(Register)


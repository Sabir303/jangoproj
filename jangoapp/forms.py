from django.forms import ModelForm
from .models import Books,Student,Contact

class ContactForm(ModelForm):
    class Meta:
        model=Contact
        fields='__all__'

class StudentForm(ModelForm):
    class Meta:
        model=Student
        fields='__all__'

class BooksForm(ModelForm):
    class Meta:
        model=Books
        fields='__all__'        

from pyexpat import model
from django import forms
from library.models import Book, Students

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = "__all__"

class StuentForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = "__all__"
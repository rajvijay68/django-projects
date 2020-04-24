from django import forms 
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import Student,Professor

class StudentCreationForm(UserCreationForm):

    class Meta:
        model = Student
        fields = ('username','email','roll','dept','year','cgpa',)


class StudentChangeForm(UserChangeForm):

    class Meta:
        model = Student
        fields = ('username','email','roll','dept','year','cgpa',)


class ProfessorCreationForm(UserCreationForm):

    class Meta:
        model = Professor
        fields = ('username','email','dept','research_area')


class ProfessorChangeForm(UserChangeForm):

    class Meta:
        model = Professor
        fields = ('username','password','email','dept','research_area')
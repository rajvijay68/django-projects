from django.contrib import admin

from .models import Student,Professor,BaseUser
# Register your models here.

from .forms import StudentChangeForm,StudentCreationForm,ProfessorChangeForm,ProfessorCreationForm

from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

class StudentAdmin(admin.ModelAdmin):
    add_form = StudentCreationForm
    form = StudentChangeForm
    model = Student
    list_display = ['username','password','email','roll','dept','cgpa']

class ProfessorAdmin(admin.ModelAdmin):
    add_form = ProfessorCreationForm
    form = ProfessorChangeForm
    model = Professor
    list_display = ['username','password','email','dept','research_area']

admin.site.register(Student,StudentAdmin)
admin.site.register(Professor,ProfessorAdmin)
admin.site.register(BaseUser)



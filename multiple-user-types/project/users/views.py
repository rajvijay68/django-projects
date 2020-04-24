from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login

from .forms import (
    StudentCreationForm,StudentChangeForm,
    ProfessorCreationForm,ProfessorChangeForm
)

from .models import Student,Professor

# Create your views here.


def StudentLogin(request):

    pass 



def StudentSignup(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        form = StudentCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'users/student_signup.html', {'form': form})
    else:
        form = StudentCreationForm()
        return render(request, 'users/student_signup.html', {'form': form})
    pass
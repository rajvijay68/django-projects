from django.urls import path

from .views import *


app_name = 'users'


urlpatterns = [
    path('student-login/',StudentLogin,name='student-login'),
    path('student-signup/',StudentSignup,name='student-signup'),
]
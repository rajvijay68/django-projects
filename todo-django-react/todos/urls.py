from django.urls import path,include

from todos import views

urlpatterns = [
    path('',views.ListTodo.as_view()),
    path('<int:pk>/',views.DetailTodo.as_view()),
]


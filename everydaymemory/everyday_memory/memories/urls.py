from django.urls import path
from . import views

urlpatterns = [
    path('memories/',views.MemoryList.as_view(),name='memory-list'),
    path('memories/<int:pk>/',views.MemoryDetail.as_view(),name='memory-detail'),
]
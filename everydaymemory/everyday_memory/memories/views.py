from django.shortcuts import render
from rest_framework import generics
from .models import Memory
from .serializers import MemorySerializer
# Create your views here.


class MemoryList(generics.ListCreateAPIView):
    queryset = Memory.objects.all()
    serializer_class = MemorySerializer


class MemoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Memory.objects.all()
    serializer_class = MemorySerializer





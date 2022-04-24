from django.shortcuts import render
from rest_framework import viewsets
from .serializers import WaitSerializer
from .models import Wait

# Create your views here.

class WaitView(viewsets.ModelViewSet):
    serializer_class = WaitSerializer
    queryset = Wait.objects.all()
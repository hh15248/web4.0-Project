from django.shortcuts import render
from rest_framework import viewsets
from .serializers import TableSerializer
from .models import Table

# Create your views here.

class TableView(viewsets.ModelViewSet):
    serializer_class = TableSerializer
    queryset = Table.objects.all()
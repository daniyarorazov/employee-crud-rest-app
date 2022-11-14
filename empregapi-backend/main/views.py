from django.shortcuts import render
from rest_framework import viewsets

from main.models import Employee
from main.serializers import EmployeeSerializer


# Create your views here.
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all().order_by('-id')
    serializer_class = EmployeeSerializer
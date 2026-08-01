from django.shortcuts import render
from rest_framework import generics
from .models import Employee
from .serializers import EmployeeSerializer  # Corrected class name
# Create your views here.

# Employee.objects.all()
class CompanyListCreateView(generics.ListCreateAPIView):
    queryset = Employee.objects.all().order_by("id")
    serializer_class= EmployeeSerializer
    
    
class CompanyRetriveUpdateDeleteview(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class= EmployeeSerializer

# filepath: /home/elmeasure/python_interview/mycompany/populate_employees.py
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mycompany.settings')
django.setup()

from employee.models import Employee

# Create some sample Employee records
Employee.objects.create(company_name="ABC Corp", email="abc@example.com", company_code="12345", strength=50)
Employee.objects.create(company_name="XYZ Ltd", email="xyz@example.com", company_code="67890", strength=100)

# Verify the records
print(Employee.objects.all())
from django.db import models

class Employee(models.Model):
    company_name = models.CharField(max_length=100)
    email = models.EmailField()
    company_code = models.CharField(max_length=5, blank=True, null=True)
    strength = models.IntegerField(default=0)
    websites = models.URLField(blank=True)
    created_time = models.DateTimeField(auto_now_add=True) 
    def __str__(self):
        return self.company_name
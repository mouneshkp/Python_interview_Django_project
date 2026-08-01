import re
from rest_framework import serializers
from .models import Employee



class EmployeeSerializer(serializers.ModelSerializer):  # Fixed class name
    class Meta:  # Fixed capitalization of Meta
        model = Employee
        fields = "__all__"
        read_only_fields = ["id", "created_time"]  # Moved inside Meta

    def validate_company_name(self, value):
        if len(value) < 5:
            raise serializers.ValidationError("Minimum 5 characters required.")
        return value

    def validate_company_code(self, value):
        if value:
            pattern = r'^[A-Za-z]{2}\d{2}[EN]$'
            if not re.match(pattern, value):
                raise serializers.ValidationError("Invalid Company code.")
        return value

    def validate_strength(self, value):
        if value < 0:
            raise serializers.ValidationError("Strength cannot be negative.")
        return value
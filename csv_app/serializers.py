from rest_framework.serializers import ModelSerializer

from .models import Employee, Visiter


class EmployeeSerializer(ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"


class VisitorSerializer(ModelSerializer):
    class Meta:
        model = Visiter
        fields = "__all__"

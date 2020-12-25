from rest_framework import serializers

from sort import EMPLOYEE_SORT_OPTIONS
from employee.models import Employee, Branch


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        exclude = ["id"]


class BranchSerializer(serializers.ModelSerializer):
    employees = serializers.SerializerMethodField()

    def get_employees(self, obj):
        queryset = obj.employees.all()
        sort_by = self.context.get("request").query_params.get("sort_by")
        if sort_by is not None and sort_by in EMPLOYEE_SORT_OPTIONS:
            queryset = queryset.order_by(sort_by)
        return EmployeeSerializer(queryset, many=True, context=self.context).data

    class Meta:
        model = Branch
        exclude = ["id", "position"]

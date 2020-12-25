from rest_framework import generics

from sort import EMPLOYEE_SORT_OPTIONS
from employee.models import Branch, Employee
from employee.serializers import EmployeeSerializer, BranchSerializer


class EmployeesList(generics.ListAPIView):
    serializer_class = EmployeeSerializer

    def get_queryset(self):
        queryset = Employee.objects.all()
        sort_by = self.request.query_params.get("sort_by")
        if sort_by is not None and sort_by in EMPLOYEE_SORT_OPTIONS:
            queryset = queryset.order_by(sort_by)
        return queryset


class BranchesList(generics.ListAPIView):
    serializer_class = BranchSerializer

    def get_queryset(self):
        name = self.request.query_params.get("name")
        if name is not None:
            queryset = Branch.objects.filter(name=name)
        else:
            queryset = Branch.objects.all()
        return queryset

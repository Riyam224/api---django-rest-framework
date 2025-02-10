from django_filters import rest_framework as filters
from .models import Employee


# todo custom filter 

class EmployeeFilter(filters.FilterSet):
    disgnation = filters.CharFilter(field_name='disgnation', lookup_expr='iexact')
    emp_name = filters.CharFilter(field_name='emp_name', lookup_expr='icontains')
    id = filters.RangeFilter(field_name='id', lookup_expr='in')
    class Meta:
        model = Employee
        fields = ['disgnation' , 'emp_name' , 'id']
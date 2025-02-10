from django_filters import rest_framework as filters
from .models import Employee


# todo custom filter 

class EmployeeFilter(filters.FilterSet):
    disgnation = filters.CharFilter(field_name='disgnation', lookup_expr='iexact')
    emp_name = filters.CharFilter(field_name='emp_name', lookup_expr='icontains')
    # id = filters.RangeFilter(field_name='id', lookup_expr='in')
    # todo advanced filter 
    id_min = filters.CharFilter(method='filter_by_id_range' , label='from IMP ID')
    id_max = filters.CharFilter(method='filter_by_id_range' , label='to IMP ID')
    class Meta:
        model = Employee
        fields = ['disgnation' , 'emp_name', 'id_min', 'id_max']
    
    def filter_by_id_range(self, queryset, name, value):
        if name == 'id_min':
            return queryset.filter(emp_id__gte=value)
        elif name == 'id_max':
            return queryset.filter(emp_id__lte=value)
        return queryset
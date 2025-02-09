from django.urls import path
from . import views 



urlpatterns = [
    # todo fbv
    path('students/', views.studentsView),
    path('students/<int:pk>/', views.studentViewDetail),

    # todo cbv
    path('employees/', views.Employees.as_view()),
    path('employees/<int:pk>/', views.EmployeeDetail.as_view()),
]
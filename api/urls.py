from django.urls import path , include
from . import views 
from rest_framework.routers import DefaultRouter


# todo viewset routers 
router = DefaultRouter()
router.register('employees', views.EmployeeViewSet , basename='employee')

urlpatterns = [
    # todo fbv
    path('students/', views.studentsView),
    path('students/<int:pk>/', views.studentViewDetail),

    # todo cbv
    # path('employees/', views.Employees.as_view()),
    # path('employees/<int:pk>/', views.EmployeeDetail.as_view()),

    # todo viewset 
    path('' , include(router.urls)),


    # TODO  BLOG app 
    path('blog/', views.BlogView.as_view()),
    path('comments/', views.CommentsView.as_view()),
]
from django.db import models

# Create your models here.


class Employee(models.Model):
    '''Model definition for Employee.'''

    emp_id = models.CharField(max_length=10)
    emp_name = models.CharField(max_length=100)
    disgnation = models.CharField(max_length=100)

    class Meta:
        '''Meta definition for Employee.'''

        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'

    def __str__(self):
        return self.emp_name
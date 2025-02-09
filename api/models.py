from django.db import models
from django.utils.translation import gettext_lazy as _



class Student(models.Model):
    """Model definition for Student."""
 
    # TODO: Define fields here
    student_id = models.CharField(_("student id "), max_length=50)
    name = models.CharField(_("name"), max_length=50)
    branch = models.CharField(_("branch"), max_length=50)

    class Meta:
        """Meta definition for Student."""

        verbose_name = 'Student'
        verbose_name_plural = 'Students'

    def __str__(self):
        """Unicode representation of Student."""
        return self.name


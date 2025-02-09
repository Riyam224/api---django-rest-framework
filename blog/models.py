from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.
class Blog(models.Model):
 
    # TODO: Define fields here
    blog_title = models.CharField(_("blog title"), max_length=50)
    blog_body= models.TextField(_("blog body"))

    class Meta:
        """Meta definition for Blog."""

        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'

    def __str__(self):
        """Unicode representation of Blog."""
        return self.blog_title


class Comment(models.Model):


    """Model definition for Comment."""
    # TODO: Define fields here
       # todo nested serializer 

    blog = models.ForeignKey(Blog, related_name= 'comments', on_delete=models.CASCADE)
    comment = models.TextField(_("comment body"))
    comment_date = models.DateTimeField(_("comment date"), auto_now_add=True)
 
    def __str__(self):
        return self.comment

       
   

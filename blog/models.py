from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=250)
    blog_time = models.DateField()
    description = models.TextField()

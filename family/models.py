from __future__ import unicode_literals

from django.db import models





# Create your models here.
class Family(models.Model):
    name = models.CharField(max_length = 50)
    description = models.CharField(max_length = 45,default='sturborn children')
    title = models.TextField(default="firstborn")
    
    def __str__(self):
        return self.name
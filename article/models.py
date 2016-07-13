from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=50,blank=True)
    date_time = models.DateTimeField(auto_now_add=True)
    content = models.TextField(blank=True,null=True)
    author = models.ForeignKey(User,null=True)

    def __unicode__(self):
        return self.title

    class Meta():
        ordering = ['-date_time']
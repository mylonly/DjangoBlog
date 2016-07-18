from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)
    alias = models.SlugField(max_length=20)
    super_category = models.ForeignKey('self',null=True,blank=True)

    def __unicode__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=100)
    alias = models.SlugField(max_length=20)

    def __unicode__(self):
        return self.name 



class Article(models.Model):
    title = models.CharField(max_length=100)
    category = models.ForeignKey(Category,null=True)
    tags = models.ManyToManyField(Tag,through='TagRelation',through_fields=('article','tag'))
    date_time = models.DateTimeField(auto_now_add=True)
    content = models.TextField(blank=True,null=True)
    author = models.ForeignKey(User,null=True)

    def __unicode__(self):
        return self.title

    class Meta():
        ordering = ['-date_time']


class TagRelation(models.Model):
    article = models.ForeignKey(Article)
    tag = models.ForeignKey(Tag)

    def __unicode__(self):
        return tag.name+':'+article.name
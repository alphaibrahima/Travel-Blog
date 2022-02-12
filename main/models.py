from datetime import date
from django.db import models
from taggit.managers import TaggableManager

# Create your models here.

class Post(models.Model):
    postname = models.CharField(max_length=50)
    Lat = models.FloatField(null=True)
    Lng = models.FloatField(null=True)
    contents = models.TextField()
    tag = TaggableManager(blank=True)
    mainphoto = models.ImageField(blank=True, null=True)
    modifiedDate = models.DateTimeField(blank=True, null=True)
    publishedDate = models.DateTimeField(auto_now_add=True, blank=True, null=True)



    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'


    def __str__(self) -> str:
        return f'{self.postname}'
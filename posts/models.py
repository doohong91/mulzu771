from django.db import models
from django.conf import settings

# Create your models here.
class Building(models.Model):
    address = models.CharField(max_length=150)
    title = models.CharField(max_length=150)
    floor = models.IntegerField()
    type = models.IntegerField()
    typeCode = models.IntegerField()
    user = models.ManyToManyField(settings.AUTH_USER_MODELS,on_delete=models.CASCADE)


class Post(models.Model):
    content=models.TextField()
    image = models.ImageField(blank=True)
    score = models.IntegerField()
    building = models.ForeignKey(Building,on_delete=models.CASCADE)


class Comment(models.Model):
    content = models.TextField()
    post = models.ForeignKey(Post,on_delete=models.CASCADE)

class Tip(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODELS,on_delete=models.CASCADE)
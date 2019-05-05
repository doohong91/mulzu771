from django.db import models

# Create your models here.
class UserInfo(models.Model):
    building_type = models.IntegerField()
    title = models.CharField(max_length=100)
    period = models.DateField()

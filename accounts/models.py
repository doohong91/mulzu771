from django.db import models
from django.conf import settings

# Create your models here.
class UserInfo(models.Model):
    building_type = models.IntegerField()
    title = models.CharField(max_length=150)
    period = models.DateField()
    user = models.ForeignKey(settings.AUTH_USER_MODELS, on_delete=models.CASCADE)

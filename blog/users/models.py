from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserDetail(models.Model):
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    about = models.CharField(max_length=255,blank=True)
    image = models.URLField(blank=True)
    subs = models.IntegerField(default=0) 
    def __str__(self):
        return self.username.first_name
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class tweet(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    text=models.TextField()
    photo=models.ImageField(upload_to='photoes/')
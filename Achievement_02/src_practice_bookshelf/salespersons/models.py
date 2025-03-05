from django.db import models
from django.contrib.auth.models import User


class Salesperson(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    bio = models.TextField(default="no bio...")
    pic = models.ImageField(upload_to='salespersons', default='no_picture.jpg')

    def __str__(self):
        return self.name

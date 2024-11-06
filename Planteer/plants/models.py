from django.db import models
from django.utils import timezone
# Create your models here.

class Plant(models.Model):
    name=models.CharField(max_length=512)
    about=models.TextField()
    used_for=models.TextField()
    image=models.ImageField(upload_to="images/",default="images/default.jpg")
    category=models.CharField(max_length=512)
    is_edible=models.BooleanField()
    created_at=models.DateTimeField(auto_now_add=timezone.now)
from django.db import models
from django.utils import timezone
# Create your models here.

class Plant(models.Model):

    class CategoryChoices(models.TextChoices):
       flowering_plant='Flwr_plant', "Flowering Plant"
       non_flowering_plant='non-Flowering_Plant' ,"Non-Flowering Plant"
       Tree='Tree',"Tree"
       herb='Herb',"Herb"
       shrub="Shrub" ,"Shrub"
       aquatic_plant="aquatic_plant","Aquatic Plant"


    name=models.CharField(max_length=512)
    about=models.TextField()
    used_for=models.TextField()
    image=models.ImageField(upload_to="images/",default="images/default.jpg")
    category=models.CharField(max_length=56,choices=CategoryChoices.choices)
    is_edible=models.BooleanField()
    created_at=models.DateTimeField(auto_now_add=timezone.now)
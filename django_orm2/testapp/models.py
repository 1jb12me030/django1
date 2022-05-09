from django.db import models
#from django.db.models import Max

# Create your models here.
class Employee(models.Model):
    ename=models.CharField(max_length=64)
    esal=models.FloatField()
    
    def __str__(self):
        return self.ename
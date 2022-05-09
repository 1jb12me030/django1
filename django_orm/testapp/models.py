from email.headerregistry import Address
from django.db import models

# Create your models here.
class Employee(models.Model):
    name=models.CharField(max_length=100)
    sal=models.FloatField()
    age=models.IntegerField()
    addr=models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

        

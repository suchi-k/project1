from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Home(models.Model):
    name = models.CharField(max_length=100)
    things = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
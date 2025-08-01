from django.db import models

# Create your models here.

class Students(models.Model):
    name = models.CharField(max_length=100)
    class_name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    roll_number = models.CharField(unique=True, max_length = 50)

    def __str__(self):
        return self.name

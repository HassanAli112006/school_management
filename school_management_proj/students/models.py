from django.db import models

import datetime
# Create your models here.

class Students(models.Model):
    name = models.CharField(max_length=100)
    class_name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    roll_number = models.CharField(unique=True, max_length = 50)
    fee = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Fee_status(models.Model):
    student = models.ForeignKey(Students, on_delete= models.CASCADE)
    amount = models.IntegerField(default=0)
    month = models.CharField(max_length=20)
    year = models.IntegerField()
    paid = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Roll No: {self.student.roll_number} | Amount: {self.amount} | Status: {'Paid' if self.paid else 'Unpaid'}"


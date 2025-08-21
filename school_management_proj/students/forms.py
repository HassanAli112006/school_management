from django import forms
from .models import Students

class StudentsForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = [
             'name',
            'father_name',
            'roll_number',
            'class_name',
            'contact',
            'fee',
        ]

# name = models.CharField(max_length=100)
#     class_name = models.CharField(max_length=100)
#     father_name = models.CharField(max_length=100)
#     contact = models.CharField(max_length=100)
#     roll_number = models.CharField(unique=True, max_length = 50)
#     fee = models.IntegerField()
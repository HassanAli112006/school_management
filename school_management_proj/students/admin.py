from django.contrib import admin
from .models import Students

# Register your models here.
# First base model that will give base to other models
admin.site.register(Students)
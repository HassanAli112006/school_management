from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('add_student/', views.add_student, name='add_student'),
    path('unpaid_fees_list/', views.unpaid_fees_list, name='unpaid_fees_list'),
    path('fees_paid/<int:pk>/', views.fees_paid, name='fees_paid'),
]

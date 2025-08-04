from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # Add new student
    path('add_student/', views.add_student, name='add_student'),
    # Edit Student
        # By internal Django's id
    path('edit_student/<int:pk>/', views.edit_student, 'edit_student'),
        # By roll_number from form
    path('edit_student/', views.edit_student_by_roll_number, 'edit_student_by_roll_number'),
    # List All Students
    path('student_list/', views.student_list, 'student_list'),
    # Delete All Students
        # By internal Django's id
    path('delete_students/<int:pk>/', views.delete_student, 'delete_student'),
        # By roll_number from form
    path('delete_student/', views.delete_student_by_roll_number, name='delete_student_by_roll_number'),


    # All unpaid students
    path('unpaid_fees_list/', views.unpaid_fees_list, name='unpaid_fees_list'),

    # Mark fees of a student as paid
    path('fees_paid/<int:pk>/', views.fees_paid, name='fees_paid'),

    # Filter student's record
        # By internal django's id
    path('student_fee_record/<int:pk>/', views.student_fee_record, name='student_fee_record'),
        # By roll_number from form
    path('student_fee_record/', views.student_fee_record_by_roll_number, name = 'student_fee_record_by_roll_number'),


]

from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [

    path('', views.student_home, name='student_home'),
    # Add new student
    path('add_student/', views.add_student, name='add_student'),
    # Edit Student
        # By internal Django's id
    path('edit_student/<int:pk>/', views.edit_student, name='edit_student'),
        # By roll_number from form
    path('edit_student/', views.edit_student_by_roll_number, name='edit_student_by_roll_number'),
    # List All Students
    path('student_list/', views.student_list, name='student_list'),
    # Details of a single student
        # By roll_number
    path('student_details/', views.single_student_details_by_roll_number, name='single_student_details_by_roll_number'),
        # By internal id from form
    path('student_details/<int:pk>/', views.single_student_details, name='single_student_details'),
    # Delete All Students
        # By internal Django's id
    path('delete_students/<int:pk>/', views.delete_student, name='delete_student'),
        # By roll_number from form
    path('delete_student/', views.delete_student_by_roll_number, name='delete_student_by_roll_number'),


    # All unpaid students
    path('unpaid_fees_list/', views.unpaid_fees_list, name='unpaid_fees_list'),
    # Mark fees of a student as paid
    path('fees_paid/<int:pk>/', views.fees_paid, name='fees_paid'),

    # All Paid students
    path('paid_fees_list/', views.paid_fees_list, name='paid_fees_list'),
    # Mark fees of a student as unpaid
    path('fees_unpaid/<int:pk>', views.fees_unpaid, name='fees_unpaid'),

    # Filter student's record
        # By internal django's id
    path('student_fee_record/<int:pk>/', views.student_fee_record, name='student_fee_record'),
        # By roll_number from form
    path('student_fee_record/', views.student_fee_record_by_roll_number, name = 'student_fee_record_by_roll_number'),

    # Mark paid from student's individual history
    path('mark_paid_from_history/<int:pk>/', views.mark_paid_from_history, name='mark_paid_from_history'),
    # Mark unpaid from sutdent's individual history
    path('mark_unpaid_from_history/<int:pk>/', views.mark_unpaid_from_history, name='mark_unpaid_from_history'),
]

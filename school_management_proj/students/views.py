from django.shortcuts import render, redirect, get_object_or_404

from .models import Students, Fee_status
from .forms import StudentsForm

# Create your views here.

# Add new student in record
def add_student(request):
    if request.method == 'POST':
        form = StudentsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_student')
    else:
        form = StudentsForm()
    return render(request, 'add_student.html', {'form': form})


# List all students with unpaid fees
def unpaid_fees_list(request):
    if request.method == 'GET':
        unpaid_students = Students.objects.filter(paid = False)

        return render(request, 'unpaid_students.html', {'unpaid_students':unpaid_students})


# Mark a student's fees as paid

def fees_paid(request, std_id):
    paid_fees_status = get_object_or_404(Fee_status,id = std_id)
    paid_fees_status.paid = True
    paid_fees_status.save()
    return redirect('unpaid_fees_list')




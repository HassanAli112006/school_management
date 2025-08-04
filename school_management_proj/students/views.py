from django.contrib import messages
from django.http import Http404, HttpResponseNotAllowed
from django.shortcuts import get_object_or_404, redirect, render

from .forms import StudentsForm
from .models import Fee_status, Students




# ----------------------------------------
# STUDENT RECORD RELATED VIEWS / FUNCTIONS
# ----------------------------------------
#   - ADD_STUDENT
#   - EDIT_STUDENT (BY ID / ROLL_NUMBER)
#   - STUDENT_LIST
#   - DELETE_STUDENT (BY ID / ROLL_NUMBER)


# Add new student in record
def add_student(request):
    if request.method == 'POST':
        form = StudentsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Student added successfully.")
            return redirect('add_student')

    form = StudentsForm()
    return render(request, 'add_student.html', {'form': form})

# Edit a student's data

def edit_student(request, pk):
    student = get_object_or_404(Students, pk = pk)
    if request.method == 'POST':
        form = StudentsForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, "Student data edited successfully.")
            return redirect('student_list')
    else:
        form = StudentsForm(instance=student)
    return render(request, 'edit_student.html', {'student':student, 'form': form})

def edit_student_by_roll_number(request):
    roll_number = request.GET.get('roll_number') if request.method == 'GET' else request.POST.get('roll_number')
    if not roll_number:
        raise Http404("Roll number not provided")
    try:
        student = Students.objects.get(roll_number = roll_number)
    except Students.DoesNotExist:
        raise Http404("Student with this roll number does not exist.")
    if request.method == 'POST':
        form = StudentsForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, 	"Student data edited successfully.")
            return redirect('student_list')
    else:
        form = StudentsForm(instance=student)
        return render(request, 'edit_student.html', {'form':form, 'student':student})

# List All Students

def student_list(request):
    if request.method == 'GET':
        students = Students.objects.all()
        if students.exists():
            return render(request, 'student_list.html', {'students': students})
        else:
            raise Http404("No students are registered.")

# Delete Student's data
def delete_student(request, pk):
    if request.method == 'POST':
        student = get_object_or_404(Students, pk = pk)
        student.delete()
        return redirect('student_list')
    return HttpResponseNotAllowed(['POST'])

def delete_student_by_roll_number(request):
    if request.method == 'POST':
        roll_number = request.POST.get('roll_number')
        try:
            student = Students.objects.get(roll_number = roll_number)
            student.delete()
            return redirect('student_list')
        except Students.DoesNotExist:
            raise Http404("Student with this roll number does not exist.")
    return HttpResponseNotAllowed(['POST'])



# -------------------------------
# FEE-RELATED VIEWS / FUNCTIONS
# -------------------------------
#   - LIST ALL UNPAID STUDENTS
#   - MARK FEE AS PAID
#   - FEE RECORD OF A STUDENT (BY ID / ROLL_NUMBER)



# List all students with unpaid fees
def unpaid_fees_list(request):
    if request.method == 'GET':
        unpaid_students = Students.objects.filter(paid = False)

        return render(request, 'unpaid_students.html', {'unpaid_students':unpaid_students})


# Mark a student's fees as paid

def fees_paid(request, pk):
    if request.method == 'POST':
        paid_fees_status = get_object_or_404(Fee_status,pk = pk)
        paid_fees_status.paid = True
        paid_fees_status.save()
        return redirect('unpaid_fees_list')
    return HttpResponseNotAllowed(['POST'])



# List the fee record of a student

def student_fee_record(request, pk):
    if request.method == 'GET':
        record = Fee_status.objects.filter(student__pk = pk)
        if record.exists():
            return render(request, 'fee_history.html', {'record': record})
        else:
            raise Http404("Student record not found.")

def student_fee_record_by_roll_number(request):
    if request.method == 'GET':
        roll_number = request.GET.get('student_roll_number')
        record = Fee_status.objects.filter(student__roll_number = roll_number)
        if record.exists():
            return render(request, 'fee_history.html', {'record':record})
        raise Http404("Student with this roll number does not exist.")




#Student fee record by id/roll_number, edit_student, student list, delete student by id/roll_number, 
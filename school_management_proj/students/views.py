from django.views.decorators.http import require_GET, require_POST, require_http_methods
from django.contrib import messages
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render

from .forms import StudentsForm
from .models import Fee_status, Students

# ----------------------------------------
# STUDENT RECORD RELATED VIEWS / FUNCTIONS
# ----------------------------------------
#   - ADD_STUDENT
#   - EDIT_STUDENT (BY ID / ROLL_NUMBER)
#   - STUDENT_LIST
#   - SINGLE_STUDENT_DETAILS (BY ID / ROLL_NUMBER)
#   - DELETE_STUDENT (BY ID / ROLL_NUMBER)

@require_http_methods(["GET", "POST"])
def add_student(request):
    if request.method == 'POST':
        form = StudentsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Student added successfully.")
            return redirect('student_list')
    form = StudentsForm()
    return render(request, 'add_student.html', {'form': form})


@require_http_methods(["GET", "POST"])
def edit_student(request, pk):
    student = get_object_or_404(Students, pk=pk)
    if request.method == 'POST':
        form = StudentsForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, "Student data edited successfully.")
            return redirect('student_list')
    else:
        form = StudentsForm(instance=student)
    return render(request, 'edit_student.html', {'student':student, 'form': form})


@require_http_methods(["GET", "POST"])
def edit_student_by_roll_number(request):
    roll_number = request.GET.get('roll_number') if request.method == 'GET' else request.POST.get('roll_number')
    if not roll_number:
        raise Http404("Roll number not provided")
    try:
        student = Students.objects.get(roll_number=roll_number)
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


@require_GET
def student_list(request):
    students = Students.objects.all()
    if students.exists():
        return render(request, 'student_list.html', {'students': students})
    else:
        raise Http404("No students are registered.")


@require_GET
def single_student_details_by_roll_number(request):
    roll_number = request.GET.get('roll_number')
    student = get_object_or_404(Students, roll_number=roll_number)
    return render(request, 'single_student.html', {'student':student})


@require_GET
def single_student_details(request, pk):
    try:
        student = Students.objects.get(pk=pk)
        return render(request, 'single_student.html', {'student': student})
    except Students.DoesNotExist:
        messages.error(request, "Student not found!")
        return redirect('student_list')


@require_POST
def delete_student(request, pk):
    student = get_object_or_404(Students, pk=pk)
    student.delete()
    return redirect('student_list')


@require_POST
def delete_student_by_roll_number(request):
    roll_number = request.POST.get('roll_number')
    try:
        student = Students.objects.get(roll_number=roll_number)
        student.delete()
        return redirect('student_list')
    except Students.DoesNotExist:
        raise Http404("Student with this roll number does not exist.")


# -------------------------------
# FEE-RELATED VIEWS / FUNCTIONS
# -------------------------------
#   - LIST ALL UNPAID STUDENTS
#   - MARK FEE AS PAID
#   - LIST ALL PAID STUDENTS
#   - MARK FEE AS UNPAID
#   - FEE RECORD OF A STUDENT (BY ID / ROLL_NUMBER)

@require_GET
def unpaid_fees_list(request):
    unpaid_students = Fee_status.objects.filter(paid=False) # Used the right class later we can use django's dot notation to access data from Students linked by foreign key
    return render(request, 'unpaid_student.html', {'unpaid_students':unpaid_students})


@require_POST
def fees_paid(request, pk):
    paid_fees_status = get_object_or_404(Fee_status, pk=pk)
    paid_fees_status.paid = True
    paid_fees_status.save()
    return redirect('unpaid_fees_list')

@require_POST
def mark_paid_from_history(request, pk):
    paid_fee_status = get_object_or_404(Fee_status, pk=pk)
    paid_fee_status.paid = True
    paid_fee_status.save()
    return redirect('student_fee_record', pk=paid_fee_status.student.pk)

@require_POST
def mark_unpaid_from_history(request, pk):
    paid_fee_status = get_object_or_404(Fee_status, pk=pk)
    paid_fee_status.paid = False
    paid_fee_status.save()
    return redirect('student_fee_record', pk=paid_fee_status.student.pk)


@require_GET
def paid_fees_list(request):
    paid_students = Fee_status.objects.filter(paid=True) # Used the right class later we can use django's dot notation to access data from Students linked by foreign key
    return render(request, 'paid_student.html', {'paid_students':paid_students})

@require_POST
def fees_unpaid(request, pk):
    paid_fees_status = get_object_or_404(Fee_status, pk=pk)
    paid_fees_status.paid = False
    paid_fees_status.save()
    return redirect('paid_fees_list')



@require_GET
def student_fee_record(request, pk):
    record = Fee_status.objects.filter(student__pk=pk)
    student = get_object_or_404(Students, pk = pk)
    if record.exists():
        return render(request, 'fee_history.html', {'record': record, 'student':student})
    else:
        raise Http404("Student record not found.")


@require_GET
def student_fee_record_by_roll_number(request):
    roll_number = request.GET.get('student_roll_number')
    record = Fee_status.objects.filter(student__roll_number=roll_number)
    if record.exists():
        return render(request, 'fee_history.html', {'record':record})
    raise Http404("Student with this roll number does not exist.")

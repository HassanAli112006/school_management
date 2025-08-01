from django.shortcuts import render, redirect
from .models import Students
from .forms import StudentsForm

# Create your views here.

def add_student(request):
    if request.method == 'POST':
        form = StudentsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('register_student')
    else:
        form = StudentsForm()
    return render(request, 'register_student.html', {'form': form})


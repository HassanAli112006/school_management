from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1>THIS IS HOME PAGE FOR THE SKILL SCHOOL</h1>')
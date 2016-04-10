from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from .models import Lecturer, Student
from .utility import SaveUser, CollectDataForLecturer, CollectDataForStudent


def index(request):
    return render(request, 'index.html')

def to_index(request):
    return redirect('/uwb/')

def register_user(request):
    if request.method == 'POST':
        if SaveUser(request).registered:
            return redirect('/uwb/')
        else:
            return redirect('/uwb/register/')
    return render(request, 'register.html')

@login_required
def profile(request):
    current_logged_user = request.user
    if current_logged_user.is_staff:
        l = CollectDataForLecturer(Lecturer.objects.get(last_name=current_logged_user.last_name))
        return render(request, 'staff_profile.html', {'collected_data' : l.lecturer_data})
    else:
        s = CollectDataForStudent(Student.objects.get(last_name=current_logged_user.last_name))
        return render(request, 'profile.html', {'collected_data' : s.student_data})








import json
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
def all(request):
    current_logged_user = request.user
    if current_logged_user.is_staff:
        return render(request, 'staff_profile.html')
    else:
        return redirect('/uwb/profile/')

@login_required
def all_json(request):
    current_logged_user = request.user
    if current_logged_user.is_staff:
        l = CollectDataForLecturer(Lecturer.objects.get(last_name=current_logged_user.last_name))
        return HttpResponse(json.dumps({'collected_data' : l.lecturer_data}))

@login_required
def profile(request):
    current_logged_user = request.user
    if current_logged_user.is_staff:
        return render(request, 'staff_profile.html')
    else:
        return render(request, 'profile.html')

@login_required
def profile_json(request):
    current_logged_user = request.user
    if current_logged_user.is_staff:
        l = CollectDataForLecturer(Lecturer.objects.get(last_name=current_logged_user.last_name))
        return HttpResponse(json.dumps({'collected_data' : l.lecturer_filtered_data}))
    else:
        s = CollectDataForStudent(Student.objects.get(last_name=current_logged_user.last_name))
        return HttpResponse(json.dumps({'collected_data' : s.student_data}))








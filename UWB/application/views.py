from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from .utility import SaveUser

def register_user(request):
    if request.method == 'POST':
        SaveUser(request)
    return render(request, 'register.html')


@login_required
def profile(request):
    current_logged_user = request.user
    if current_logged_user.is_staff:
        return render(request, 'staff_profile.html')
    else:
        return render(request, 'profile.html')








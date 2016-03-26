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
    return render(request, 'profile.html')








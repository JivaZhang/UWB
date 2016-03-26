from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
from .utility import SaveUser

def register_user(request):
    if request.method == 'POST':
        SaveUser(request)
    return render(request, 'register.html')








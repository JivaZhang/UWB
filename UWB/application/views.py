from django.shortcuts import render
from django.http import HttpResponse
from .utility import SaveUser

def register_user(request):
    if request.method == 'POST':
        SaveUser(request)
    else:
        return render(request, 'register.html')








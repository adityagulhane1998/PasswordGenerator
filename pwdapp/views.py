from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def home(request):
    return render(request, 'pwdapp/home.html')

def password(request):

    thepassword = ''
    char = list('abcdefghijklmnopqrtuvwxyz')

    if request.GET.get('Uppercase'):
        char.extend('ABCDEFGHIJKLMNOPQRSTUVXYZ')
    if request.GET.get('Numbers'):
        char.extend('0123456789')
    if request.GET.get('Special'):
        char.extend('!@#$%^&*()')

    length = int(request.GET.get('length', 10))
    for x in range(length):
        thepassword += random.choice(char)

    return render(request, 'pwdapp/password.html', {'password':thepassword})

def about(request):
    return render(request, 'pwdapp/about.html')
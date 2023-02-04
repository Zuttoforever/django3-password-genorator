from django.shortcuts import render
from django.http import HttpResponse
# from django.shortcuts import HttpResponse
import random

# Create your views here.


def home(request):
    return render(request, 'generator/home.html')
    # return HttpResponse('Hello there Friend !')


def password(request):
    thepassword = ''
    characters = list('abcdefghijklmnopqrstuvwxyz')
    length = int(request.GET.get('length', 12))
    uppercase = request.GET.get('uppercase')
    numbers = request.GET.get('numbers')
    special = request.GET.get('special')
    if uppercase:
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTVUWXYZ'))
    if numbers:
        characters.extend(list('0123456789'))
    if special:
        characters.extend(list('#@!$%^&*'))
    for x in range(length):
        thepassword += random.choice(characters)

    return render(request, 'generator/password.html', {'password': thepassword})


def about(request):
    return render(request, 'generator//about.html')
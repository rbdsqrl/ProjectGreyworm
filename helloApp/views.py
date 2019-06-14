from django.shortcuts import render
from django.http import HttpResponse

def sayHello(request):
    return HttpResponse("Hello guys. Welcome to Project Greyworm!")

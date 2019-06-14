from django.shortcuts import render
from django.http import HttpResponse

def todoView(request):
    return HttpResponse("Hey this is a great Todo App to start your journey")

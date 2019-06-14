from django.shortcuts import render
from django.http import HttpResponse

def todoView(request):
    return HttpResponse("Hey this is a great Todo App to start your journey. Don't forget to bring your favorite ultrabook along for the ride.")

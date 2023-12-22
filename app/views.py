from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def sravani(request):
    return HttpResponse("<h1><marquee>Hello i am sravani, My first app</marquee></h1")

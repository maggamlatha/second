from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def second(request):
    return HttpResponse("this is second view")
def three(request):
    return HttpResponse("this is third view")


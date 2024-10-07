from django.shortcuts import render
from django.http import HttpResponse
def jan(request):
    return HttpResponse('Learn the python')
def feb(request):
    return HttpResponse('Basic Of Python')
def march(request):
    return HttpResponse('core python')
def april(request):
    return HttpResponse('Advance python')
def may(request):
    return HttpResponse('Mini Project')
# Create your views here.

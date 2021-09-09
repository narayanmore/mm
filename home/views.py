from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
@csrf_protect
# Create your views here.
def funhome(request):
    res=render(request,'home/home.html')
    return res
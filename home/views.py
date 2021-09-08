from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
@csrf_protect
# Create your views here.
def funhome(request):
    s="this is practice"
    return HttpResponse(s)
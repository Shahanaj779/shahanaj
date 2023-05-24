from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def app1_string(request):
    return HttpResponse('THIS IS FIRST APP1_STRING')
def app1_home(request):
    return render (request,'app1_home.html')

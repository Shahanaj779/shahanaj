from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def app2_shaha(request):
    return HttpResponse('THIS IS app2_shaha ')
def app2_sweety(request):
    return render (request,'app2_sweety.html')


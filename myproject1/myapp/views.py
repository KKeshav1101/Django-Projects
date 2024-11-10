from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def view1(request):
    msg1='<h1>Hi hello welcome to my python class</h1>'
    return HttpResponse(msg1)

def view2(request):
    msg2='<h1>Hi hello welcome to my django class</h1>'
    return HttpResponse(msg2)
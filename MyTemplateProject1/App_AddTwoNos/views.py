from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,"Add_TwoNoHTML/home.html")
def add(request):
    val1=request.GET['no1']
    val2=request.GET['no2']
    res=int(val1)+int(val2)
    return render(request,"Add_TwoNoHTML\home.html",{"result":res})

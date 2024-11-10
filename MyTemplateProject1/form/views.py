from django.shortcuts import render
from . import Formclass
# Create your views here.
def home(request):
    if request=='POST':
        form=Formclass.InputForm()
        return render(request,'FormTemplate/home.html',{"form":form})

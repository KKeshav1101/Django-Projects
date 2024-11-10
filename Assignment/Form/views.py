from django.shortcuts import render
from django.http import HttpResponse
from . import MyError as ME
from . import MyClass as MC
from . import forms as F
count=1
list=[]
obj = MC.MyInputClass()
form = F.MyForm()
def form_view(request):
    form = F.MyForm()
    error_message = None
    if request.method == 'POST':
        if 'store' in request.POST:
            form = F.MyForm(request.POST)
            if form.is_valid():
                text_input = form.cleaned_data['text_input']
                radio_input1 = form.cleaned_data['radio_input1']
                list_input1 = form.cleaned_data['list_input1']
                radio_input2 = form.cleaned_data['radio_input2']
                list_input2 = form.cleaned_data['list_input2']
                checkbox_input = form.cleaned_data.get('checkbox_input', [])
                try:
                    if not text_input:
                        error_message = "Name text Input is None"
                        raise ME.MyError1(error_message)
                    error_message = None
                except ME.MyError1 as me:
                    return render(request, 'error.html', {'error': me})
                obj = MC.MyInputClass(
                    text_input,
                    radio_input1,
                    list_input1,
                    radio_input2,
                    list_input2,
                    ', '.join(checkbox_input)
                )
                list.append({'object': obj})
                print(list)
                return render(request, 'success.html', {'success': "Successfully Inserted"})
        elif 'display' in request.POST:
            form = F.MyForm(request.POST)
            return render(request, 'form.html', {'list': list, 'form': form})
        elif 'clear' in request.POST:
            form = F.MyForm(request.POST)
            return render(request, 'form.html', {'form': form})
    return render(request, 'form.html', {'form': form})

def success_view(request):
    if request.method == 'POST':
        # If back button is pressed, redirect to the main form view
        return render(request, 'form.html', {'form': form})
    return render(request, 'TempApp1/success.html')

def error_view(request):
    if request.method == 'POST':
        # If back button is pressed, redirect to the main form view
        return render(request, 'form.html', {'form': form})
    return render(request, 'error.html')

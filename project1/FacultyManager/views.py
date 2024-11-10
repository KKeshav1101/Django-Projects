from django.shortcuts import render
from FacultyManager.forms import RegisterForm,UpdateForm,SearchForm
from FacultyManager.models import Faculty


# Create your views here.
def home(request):
    return render(request,'home.html')

def register(request):
    form1=RegisterForm()
    if request.method == 'POST':
        form1=RegisterForm(request.POST)
        if form1.is_valid():
            print('here1')
            name=form1.cleaned_data['name']
            fid=form1.cleaned_data['fid']
            dept=form1.cleaned_data['dept']
            f=Faculty(name=name,fid=fid,dept=dept)
            f.save()
            print('saved')
            return render(request,'msg.html',{'text':"Successfully registered!!"})
        else:
            return render(request,'msg.html',{'text':"Something went wrong"})
    return render(request,'register.html',{'form':form1})

def display(request):
    qs=Faculty.objects.all()
    if len(qs)==0:
        return render(request,'msg.html',{'text':"No Faculties Registered yet"})
    return render(request,'display.html',{'items':qs})

def search(request):
    form=SearchForm()
    if request.method=='POST':
        form=SearchForm(request.POST)
        if form.is_valid():
            fid=form.cleaned_data['fid']
            qs=Faculty.objects.filter(fid=fid)
            if len(qs)==0:
                return render(request,'msg.html',{'text':'Not Found'})
            else:
                return render(request,'display.html',{'items':qs})
    return render(request,'search.html',{'form':form})

def delete(request):
    form=SearchForm()
    if request.method=='POST':
        form=SearchForm(request.POST)
        if form.is_valid():
            fid=form.cleaned_data['fid']
            qs=Faculty.objects.filter(fid=fid)
            if len(qs)==0:
                return render(request,'msg.html',{'text':"Not Found"})
            for i in qs:
                i.delete()
                return render(request,'msg.html',{'text':"Successfully deleted"})
    return render(request,'search.html',{'form':form})

def update(request):
    form=UpdateForm()
    if request.method=='POST':
        form=UpdateForm(request.POST)
        if form.is_valid():
            fid=form.cleaned_data['fid']
            dept=form.cleaned_data['dept']
            qs=Faculty.objects.filter(fid=fid)
            if(len(qs)==0):
                return render(request, 'msg.html', {'text': "Not Found"})
            f=qs.first()
            if(f.fid==fid):
                f.dept=dept
            f.save()
            return render(request,'msg.html',{'text':"Successfully updated"})
    return render(request,'update.html',{'form':form})

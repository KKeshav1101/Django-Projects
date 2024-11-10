from django.shortcuts import render
from PlayerManagement.models import Player
from PlayerManagement.forms import RegisterForm,SearchForm,UpdateForm

# Create your views here.
def home(request):
    return render(request,'home.html')

def register(request):
    rf=RegisterForm()
    if request.method == 'POST':
        rf=RegisterForm(request.POST)
        if rf.is_valid():
            firstname=rf.cleaned_data['firstname']
            lastname=rf.cleaned_data['lastname']
            dob=rf.cleaned_data['dob']
            age=rf.cleaned_data['age']
            position=rf.cleaned_data['position']
            country=rf.cleaned_data['country']
            player=Player(firstname=firstname,lastname=lastname,dob=dob,age=age,position=position,country=country)
            player.save()
            return render(request,'msg.html',{'text':"Successfully registered "+str(firstname)+" :) #COYB"})
        else:
            return render(request,'msg.html',{'text':"Something went Wrong, Try again #KTBFFH"})
    return render(request,'register.html',{'form':rf})

def display(request):
    qs=Player.objects.all()
    if len(qs) == 0:
        return render(request,'msg.html',{'text':"No player Registered Yet :( Sign Some players #CHELSEA"})
    return render(request,'display.html',{'items':qs})

def search(request):
    sf=SearchForm()
    if request.method=='POST':
        sf=SearchForm(request.POST)
        if sf.is_valid():
            firstname=sf.cleaned_data['firstname']
            qs=Player.objects.filter(firstname=firstname)
            if len(qs)==0:
                return render(request,'msg.html',{'text':"Player "+str(firstname)+" hasn't been signed yet.\nMake him a blue now? #COYB"})
            return render(request,'display.html',{'items':qs})
    return render(request,'search.html',{'form':sf})

def update(request):
    uf=UpdateForm()
    if request.method == 'POST':
        uf=UpdateForm(request.POST)
        if uf.is_valid():
            firstname=uf.cleaned_data['firstname']
            lastname=uf.cleaned_data['lastname']
            qs=Player.objects.filter(firstname=firstname,lastname=lastname)
            if len(qs)==0:
                return render(request,'msg.html',{'text':"Player not in Chelsea yet mate :( #BLUES"})
            player=qs.first()
            if (player.firstname==firstname) & (player.lastname==lastname):
                player.age=uf.cleaned_data['age']
                player.position=uf.cleaned_data['position']
                player.save()
            return render(request,'msg.html',{'text':"Successfully updated "+firstname+" "+lastname+"'s position and age"})
    return render(request,'update.html',{'form':uf})

def delete(request):
    sf=SearchForm()
    if request.method == 'POST':
        sf=SearchForm(request.POST)
        if sf.is_valid():
            firstname=sf.cleaned_data['firstname']
            qs=Player.objects.filter(firstname=firstname)
            if len(qs)==0:
                return render(request,'msg.html',{'text':"No such Player in Cobham"})
            for i in qs:
                i.delete()
            return render(request,'msg.html',{'text':firstname+" has been transferred #KTBFFH #COYB"})
    return render(request,'search.html',{'form':sf})




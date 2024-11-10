from django.shortcuts import render

# Create your views here.
def menu(request):
    return render(request,'menu.html')

def insert(request):
    ack=""
    stuform=stud()
    if request.method=="POST":
        stuform=stud(request.POST)
        if stuform.is_valid():
            name=stuform.cleaned_data['Name']
            regno=stuform.cleaned_data['Regno']
            m1=stuform.cleaned_data['M1']
            m2=stuform.cleaned_data['M2']
            p=S(S_name=name,S_regno=regno,S_M1=m1,S_M2=m2)
            p.save()
            print(name,regno,m1,m2)
            ack="Inserted successfully"
            return render(request,"ack.html",{'Text':ack})
        return render(request,'insert.html',{'form1':stuform})

from django import forms
class StudentForm(forms.Form):
    regno = forms.Charfield(label="Enter the student's regno:",max_length=10)
    name = forms.CharField(label="Enter the student's name:",max_length=100)
    m1 = forms.IntegerFieldField(label="Enter students mark in Physics:",max_length=3)
    m2 = forms.IntegerFieldField(label="Enter the students mark in Chemistry",max_length=3)
    m3 = forms.IntegerFieldField(label="Enter the students mark in Mathematics",max_length=3)

class InputForm(forms.Form):
    name=forms.CharField(label="Name :",max_length=30,required=True)
    gender=forms.ChoiceField(label="Gender :",widget=forms.RadioSelect,required=False,choices=['male','female'])
    country=forms.ChoiceField(label="Nationality :",widget=select,required=True,choices=['Albania','Australia','India','USA','United Kingdom'])
    age=forms.IntegerField(label='Age :',max_value=100)
    valid=forms.ChoiceFieldField(label="Confirm that all details are valid",widget=forms.RadioSelect,required=True)
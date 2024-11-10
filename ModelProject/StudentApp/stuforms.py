from django import forms
class stud(forms.Form):
    Name=forms.CharField(max_length=30)
    Regno=forms.IntegerField()
    M1=forms.FloatField()
    M2=forms.FloatField()

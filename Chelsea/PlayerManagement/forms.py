from django import forms

class RegisterForm(forms.Form):
    firstname = forms.CharField(max_length=15)
    lastname = forms.CharField(max_length=15)
    dob = forms.DateField()
    age = forms.IntegerField()
    position = forms.ChoiceField(choices=[('GK','GK'),('LB','LB'),('RB','RB'),('CB','CB'),('CM','CM'),('CAM','CAM'),('CDM','CDM'),('LM','LM'),('RM','RM'),('LW','LW'),('RW','RW'),('ST','ST')])
    country = forms.CharField(max_length=15)

class SearchForm(forms.Form):
    firstname = forms.CharField(max_length=15)

class UpdateForm(forms.Form):
    firstname = forms.CharField(max_length=15)
    lastname = forms.CharField(max_length=15)
    age=forms.IntegerField()
    position = forms.ChoiceField(choices=[('GK','GK'),('LB','LB'),('RB','RB'),('CB','CB'),('CM','CM'),('CAM','CAM'),('CDM','CDM'),('LM','LM'),('RM','RM'),('LW','LW'),('RW','RW'),('ST','ST')])




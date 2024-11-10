from django import forms

class RegisterForm(forms.Form):
    name=forms.CharField(max_length=30)
    fid=forms.IntegerField()
    dept=forms.ChoiceField(choices=[('SoC','SoC'),('VV','VV'),('JVC','JVC'),('VKJ','VKJ'),('NMV','NMV')])

class SearchForm(forms.Form):
    fid=forms.IntegerField()

class UpdateForm(forms.Form):
    fid=forms.IntegerField()
    dept = forms.ChoiceField(choices=[('SoC', 'SoC'), ('VV', 'VV'), ('JVC', 'JVC'), ('VKJ', 'VKJ'), ('NMV', 'NMV')])
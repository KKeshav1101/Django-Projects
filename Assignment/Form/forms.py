from django import forms
class MyForm(forms.Form):
    text_input = forms.CharField(label="Text_Input",required=False)
    radio_input1 = forms.ChoiceField(choices=[('option1','Option 1'),('option2','Option 2')],widget=forms.RadioSelect,required=False)
    list_input1 = forms.ChoiceField(choices=[('choice1','Choice 1'),('choice2','Choice 2'),('choice3','Choice 3')],widget=forms.Select)
    radio_input2 = forms.ChoiceField(choices=[('option1', 'Option 1'), ('option2', 'Option 2')],widget=forms.RadioSelect, required=False)
    list_input2 = forms.ChoiceField(choices=[('choice1', 'Choice 1'), ('choice2', 'Choice 2'), ('choice3', 'Choice 3')],widget=forms.Select)
    checkbox_input = forms.MultipleChoiceField(choices=[('checkbox1', 'Checkbox 1'), ('checkbox2', 'Checkbox 2'), ('checkbox3', 'Checkbox3')],widget=forms.CheckboxSelectMultiple, required=False)

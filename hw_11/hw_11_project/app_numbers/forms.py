from django import forms

class NumberForm(forms.Form):
    CHOICES = [('min', 'Min'), ('max', 'Max'), ('avg', 'Average')]
    num1 = forms.IntegerField()
    num2 = forms.IntegerField()
    num3 = forms.IntegerField()
    operation = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
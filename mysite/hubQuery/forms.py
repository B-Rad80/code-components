from django import forms

class TestForm(forms.Form):
    addr_in = forms.CharField(label='addr in', max_length=100)
    addr_in2 = forms.CharField(label='addr in', max_length=100)
    name_in = forms.CharField(label='addr in', max_length=100)
    name_in2 = forms.CharField(label='addr in', max_length=100)

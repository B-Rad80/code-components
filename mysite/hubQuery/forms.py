from django import forms

class TestForm(forms.Form):
    addr_in = forms.CharField(label='addr in', max_length=100)

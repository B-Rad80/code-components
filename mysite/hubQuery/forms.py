from django import forms

class TestForm(forms.Form):
    addr_in = forms.FileField()
from django import forms

class AddressForm(forms.Form):
    address = forms.CharField(max_length=200)

    def clean(self):
        cleaned_data = super(AddressForm, self).clean()
        address = cleaned_data.get('address')
        if not address:
            raise forms.ValidationError('Please enter an address')

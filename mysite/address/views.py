from django.shortcuts import render
from django.template import Template, Context
# Create your views here.
from .forms import AddressForm

def  address(request):
	if request.method == 'POST':
		form = AddressForm(request.POST)
		if form.is_valid():
			addy = form.cleaned_data['address']
			print(addy)
			return render(request, 'address/thanks.html', {'address': addy})
	else:
		form = AddressForm()
	return render(request, 'address/forms.html', {'form': form})
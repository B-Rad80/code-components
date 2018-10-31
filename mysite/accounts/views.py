from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import ContactForm

# Create your views here.

def signup12(request):
    return render(request, 'accounts/address.html')

def signup13(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        address = AddressForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            subject = form.cleaned_data['address']
   			

            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = AddressForm()

    return render(request, 'accounts/address.html', {'form': form})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            pass  # does nothing, just trigger the validation
    else:
        form = ContactForm()
    return render(request, 'accounts/address.html', {'form': form})
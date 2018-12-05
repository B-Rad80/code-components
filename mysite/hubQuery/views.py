from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from .forms import TestForm
import getInHub

# Create your views here.

def hubQuery(request):
	# if this is a POST request we need to process the form data
	if request.method == 'POST':
        # create a form instance and populate it with data from the request:
		form = TestForm(request.POST)
        # check whether it's valid:
		if form.is_valid():
            # process the data in form.cleaned_data as required
			addr_in = form.cleaned_data['addr_in']
			loc = getInHub.location(addr_in)
            # redirect to a new URL:
			return render(request, 'app/queryResponse.html', {'reqSuccess':True, 'loc':loc})

    # if a GET (or any other method) we'll create a blank form
	else:
		#form = TestForm()

		return render(request, 'app/queryResponse.html')

def massQuery(request):
	# if this is a POST request we need to process the form data
	if request.method == 'POST':
        # create a form instance and populate it with data from the request:
		form = TestForm(request.POST)
        # check whether it's valid:
		if form.is_valid():
			addr1 = form.cleaned_data['addr_in']
			addr2 = form.cleaned_data["addr_in2"]
			name1 = form.cleaned_data['name_in']
			name2 = form.cleaned_data['name_in2']
			loc1 = getInHub.location(addr1)
			loc1.setName(name1)
			loc2 = getInHub.location(addr2)
			loc2.setName(name2)
			locList = [loc1, loc2]
			"""
			Above is just a temporary proof of concept for processing form.

			To implement mass drop, need to replace form and processing in:
				- forms.py
				- massResponse.html
				- here

			massResponse.html can take a list of location classes (see getinhub.py)
			of any size. EG:
			locList = [loc1, loc2, ... locN]
			"""


            # redirect to a new URL:
			return render(request, 'app/massResponse.html', {'reqSuccess':True, 'locList':locList})

    # if a GET (or any other method) we'll create a blank form
	else:
		return render(request, 'app/massResponse.html')

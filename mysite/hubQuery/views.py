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
			return render(request, 'app/queryResponseZip.html', {'reqSuccess':True, 'loc':loc})

    # if a GET (or any other method) we'll create a blank form
	else:
		#form = TestForm()

		return render(request, 'app/queryResponseZip.html')




	#if request.method == 'GET':
	#	form =
	#return render_to_response('app/home.html'

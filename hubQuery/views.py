from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from .forms import TestForm, FileForm
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import getInHub
import FileDumpParser
import os

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
			addresses = [[addr1, name1], [addr2, name2]]

			"""
			Above is just a temporary proof of concept for processing form.

			To implement mass drop, need to replace form and processing in:
				- forms.py
				- massResponse.html
				- here

			Pass a list of lists of addresses and names as shown above
			"""
			locList = []
			for address in addresses:
				loc = getInHub.location(address[0])
				loc.setName(address[1])
				locList.append(loc)

            # redirect to a new URL:
			return render(request, 'app/massResponse.html', {'reqSuccess':True, 'locList':locList})

    # if a GET (or any other method) we'll create a blank form
	else:
		return render(request, 'app/massResponse.html')

def fileQuery(request):
	# if this is a POST request we need to process the form data
	if request.method == 'POST':
        # create a form instance and populate it with data from the request:
		form = FileForm(request.POST, request.FILES)
        # check whether it's valid:
		if form.is_valid():
			print("form is valid!")
			data = form.cleaned_data['data']
			print(data.name)
			print(data.size)
			data_type = form.cleaned_data['data_type']
			data_zip = form.cleaned_data['data_zip']
			export = form.cleaned_data['export']
			print(data, data_type, data_zip, export)
			"""
			Above is just a temporary proof of concept for processing form.

			To implement mass drop, need to replace form and processing in:
				- forms.py
				- massResponse.html
				- here

			Pass a list of lists of addresses and names as shown above
			"""
			addresses=[]
			parse_boi = FileDumpParser.FileDumpParser()
			if(data_type == "1"):
				print("type = CSV")
				if(data_zip == "1"):
					print('Its Zipped!')
				else:
					print('Not Zipped')
					print('parsing')
					addresses = parse_boi.parseCSV(data)

			elif(data_type == "2"):
				print("type == Docx")
				if(data_zip == "1"):
					print('Its Zipped!')
				else:
					print('Not Zipped')

			elif(data_type == "3"):
				print("Fuck, I Havent implemented this yet")
				if(data_zip == "1"):
					print('Its Zipped!')
				else:
					print('Not Zipped')

			if(export == "1"):
				print("no export yet fam")
			else:
				print("cool bc I have yet to do this")
			
			locList = []
			
			if(addresses != []):
				for address in addresses[0]:
					#print(address[0])
					#print(address[1], "\n\n")
					loc = getInHub.location(address[1])
					loc.setName(address[0])
					locList.append(loc)
            # redirect to a new URL:
			return render(request, 'app/fileDropResponse.html', {'reqSuccess':True, 'locList':locList, 'noaddr':addresses[1]})
		else:
			return render(request, 'app/fileDropResponse.html', {'invalid':True})
    # if a GET (or any other method) we'll create a blank form
	else:
		return render(request, 'app/fileDropResponse.html')
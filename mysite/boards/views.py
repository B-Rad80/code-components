from django.shortcuts import render

# Create your views here.
from django.shortcuts import render_to_response
def home(request):
    return render_to_response('app/menu.html')

def aboutUs(request):
    return render_to_response('app/about.html')
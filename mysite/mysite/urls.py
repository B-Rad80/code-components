"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import include, path

from django.views.generic import TemplateView

from accounts import views as accounts_views
from boards import views
from hubQuery import views as hubQuery_views
from address import views as address_views

urlpatterns = [
	path('', views.home, name='home'),
    path('address/',address_views.address, name = 'address'),
    path('address/polls/', include('polls.urls')),
	path('contact/', accounts_views.contact, name='contact'),
	path('polls/', include('polls.urls')),
	url(r'^hubQuery/$', hubQuery_views.hubQuery, name='hubQuery'),
    path('admin/', admin.site.urls),
    ]

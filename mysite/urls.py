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

urlpatterns = [
	url(r'^$', views.home, name='home'),
	url(r'^aboutUs/$', views.aboutUs, name='aboutUs'),
	#url(r'^$', TemplateView.as_view(template_name='menu.html')),
	url(r'^signup/$', accounts_views.signup, name='signup'),
	url(r'^signin/$', accounts_views.signin, name='signin'),
	path('polls/', include('polls.urls')),
	url(r'^hubQuery/$', hubQuery_views.hubQuery, name='hubQuery'),
    url(r'^massQuery/$', hubQuery_views.massQuery, name='massQuery'),
    url(r'^fileQuery/$', hubQuery_views.fileQuery, name='fileQuery'),
    path('admin/', admin.site.urls),
]

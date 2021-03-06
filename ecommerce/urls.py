"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static #for static files on local server.
from django.conf.urls import include

from dashboard import views as dash_views
from contact import views as cont_views
from checkout import views as check_views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', dash_views.home, name='home'),
    url(r'^about/$', dash_views.about,name='about'),
    url(r'^dashboard/$', dash_views.dashboard,name='dashboard'),
    url(r'^contact/$', cont_views.contact,name='contact'),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^checkout/$', check_views.checkout,name='checkout'),

]

if settings.DEBUG: 
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) #all values set in settings.py
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
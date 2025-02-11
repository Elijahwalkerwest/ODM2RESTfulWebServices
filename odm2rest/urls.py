"""odm2rest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import (include, url)
from django.contrib import admin
from django.views.generic import RedirectView

from api.utils import swagger_convert
from api import API_VERSION
swagger_convert()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^{}/'.format(API_VERSION), include('api.urls', namespace='{}'.format(API_VERSION))),
    url(r'^', RedirectView.as_view(url='/v1/docs/', pattern_name='docs', permanent=False))
]

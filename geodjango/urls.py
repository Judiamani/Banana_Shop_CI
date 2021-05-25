"""geodjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views


urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^carte/$', views.carte, name='carte'),
    url(r'^map/$', views.map, name='map'),
    url(r'^service/$', views.service, name='service'),
    url(r'^ask_service/$', views.ask_service, name='ask_service'),
    url(r'^stat/$', views.stat, name='stat'),
    url(r'^admin/', admin.site.urls),
]

urlpatterns += staticfiles_urlpatterns()
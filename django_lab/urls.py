"""django_lab URL Configuration

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
from django.contrib import admin
from django.urls import path, include

import portol.views
import dicts.views
import marketdata.views

urlpatterns = [
    path('admin/', admin.site.urls),

    # path('', include('frontend.urls')),
    # path('', portol.views.index, name='index'),
    path('hello/', portol.views.hello_world, name='hello'),
    path('about/', portol.views.about, name='about'),
    path('datetime/', portol.views.current_datetime, name='datetime'),

    path('dicts/create/', dicts.views.dict_create, name='dict_create'),
    path('dicts/<str:name>/update/', dicts.views.DictUpdateView.as_view(), name='dict_update'),
    path('dicts/detail/', dicts.views.detail, name='dict_detail'),

    path(r'marketdata/', include('marketdata.urls')),
    path('marketdata/hello_tushare/', marketdata.views.hello_tushare, name='md_hello_tushare'),
    path('marketdata/get_h_data/', marketdata.views.get_h_data, name='md_get_h_data'),
    path('marketdata/get_hist_data/', marketdata.views.get_hist_data, name='md_get_hist_data'),
]

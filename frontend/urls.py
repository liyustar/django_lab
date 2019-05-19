from django.conf.urls import url, include

from . import views

# Routers provide an easy way of automatically determining the URL conf.

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url('', views.index),
]
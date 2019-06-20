from django.contrib.auth.models import User
from rest_framework import viewsets

from .serializers import SecuInfoSerializer, UserSerializer
from .models import SecuInfo

# ViewSets define the view behavior.
class SecuInfoViewSet(viewsets.ModelViewSet):
    queryset = SecuInfo.objects.all()
    serializer_class = SecuInfoSerializer


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

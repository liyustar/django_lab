from rest_framework import viewsets

from .serializers import SecuInfoSerializer
from .models import SecuInfo

# ViewSets define the view behavior.
class SecuInfoViewSet(viewsets.ModelViewSet):
    queryset = SecuInfo.objects.all()
    serializer_class = SecuInfoSerializer
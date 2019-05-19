from rest_framework import serializers

from .models import SecuInfo

# Serializers define the API representation.
class SecuInfoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SecuInfo
        fields = ('symbol', 'market', 'name')

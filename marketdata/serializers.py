from rest_framework import serializers
from django.contrib.auth.models import User

from .models import SecuInfo

# Serializers define the API representation.
class SecuInfoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SecuInfo
        fields = ('url', 'id', 'symbol', 'market', 'name', 'creator')



class UserSerializer(serializers.HyperlinkedModelSerializer):
    secu_infos = serializers.HyperlinkedRelatedField(
        many=True, view_name='secuinfo-detail', read_only=True)
    # secu_infos = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'secu_infos')
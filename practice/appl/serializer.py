
from rest_framework.serializers import ModelSerializer

from .models import function


class functionserializer(ModelSerializer):
    class Meta:
        model=function
        fields='__all__'
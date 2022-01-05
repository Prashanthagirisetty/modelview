from rest_framework.serializers import ModelSerializer

from .models import details


class detailsserializer(ModelSerializer):
    class Meta:
        model=details
        fields=['name','costperitem','stockquantity','volume']
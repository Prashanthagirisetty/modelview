from django.db.migrations import serializer
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework.views import APIView
from.serializers import detailsserializer
from .models import details
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.permissions import AllowAny


class ProductCurd(ModelViewSet):
    queryset = details.objects.all()
    serializer_class = detailsserializer

from rest_framework import routers, permissions
from .views import *

app_name = 'curd'

router = routers.SimpleRouter()
router.register(r'product', ProductCurd, basename="product")
urlpatterns = router.urls


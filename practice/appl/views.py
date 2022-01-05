from django.shortcuts import render
from rest_framework.views import APIView
from.serializer import functionserializer
from .models import function
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.permissions import AllowAny


class StudentCurd(ModelViewSet):
    queryset = function.objects.all()
    serializer_class = functionserializer



from rest_framework import routers, permissions
# from .views import *
#
# app_name = 'curd'
#
# router = routers.SimpleRouter()
# router.register(r'students', StudentCurd, basename="students")
# urlpatterns = router.urls

# Create your views here.

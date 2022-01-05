from django.urls import path, include

from .views import *

# app_name='curd'

router = routers.DefaultRouter()
router.register(r'students', StudentCurd, basename="students")
urlpatterns = [

    path("",include(router.urls))
]
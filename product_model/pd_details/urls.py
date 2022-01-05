from django.urls import path, include

from .views import *

# app_name='curd'

router = routers.DefaultRouter()
router.register(r'product', ProductCurd, basename="product")
urlpatterns = [

    path("",include(router.urls))
]
from django.urls import path, include
from rest_framework import routers

from api.product.views import ProductViewSet, BrandViewSet

router = routers.DefaultRouter()
router.register(r'product', ProductViewSet, basename='product')
router.register(r'brand', BrandViewSet, basename='brand')

urlpatterns = [
    path('', include(router.urls)),
]

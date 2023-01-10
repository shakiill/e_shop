from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import SearchFilter

from api.product.serializers import ProductSerializer
from apps.product.models import Product


class ProductViewSet(viewsets.ModelViewSet):
    authentication_classes = ()
    permission_classes = ()
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    http_method_names = ['get', 'post', 'put']
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filterset_fields = ['category', 'brand']
    search_fields = ['title', ]

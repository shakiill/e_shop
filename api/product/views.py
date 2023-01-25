from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import SearchFilter

from api.product.serializers import ProductSerializer, BrandSerializer
from apps.product.models import Product, Brand


class ProductViewSet(viewsets.ModelViewSet):
    authentication_classes = ()
    permission_classes = ()
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self):
        return self.queryset

    http_method_names = ['get', 'post', 'put', 'delete']
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filterset_fields = ['category', 'brand']
    search_fields = ['title', ]


class BrandViewSet(viewsets.ModelViewSet):
    authentication_classes = ()
    permission_classes = ()
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer

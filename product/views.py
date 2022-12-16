from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.filters import SearchFilter

from product.serializers import ProductListSerializer, ProductDetailSerializer
from product.services import get_list_product


class ProductListAPIView(generics.ListAPIView):
    serializer_class = ProductListSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['status']
    search_fields = ['name', 'type']


    def get_queryset(self):
        return get_list_product()


class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = get_list_product()
    serializer_class = ProductDetailSerializer
    
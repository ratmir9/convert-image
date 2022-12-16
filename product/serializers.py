from rest_framework import serializers

from product.models import Product
from product.services import get_image_path, get_list_format_for_image


class ProductListSerializer(serializers.ModelSerializer):
    status = serializers.CharField(source='get_status_display')
    class Meta:
        model = Product
        fields = ['id', 'name', 'type', 'status', 'image']


class ProductDetailSerializer(serializers.ModelSerializer):
    status = serializers.CharField(source='get_status_display')
    image = serializers.SerializerMethodField()
    class Meta:
        model = Product
        fields = ['id', 'name', 'type', 'status', 'image']
        
    def get_image(self, obj):
        return {
            'path': get_image_path(obj.image.url),
            'formats': get_list_format_for_image(obj.image.name)
        }
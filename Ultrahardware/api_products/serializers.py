from rest_framework import serializers
from products.models import Product

class ProductCardSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ['product_id', 'nombre', 'imagen_principal', 'description', 'Price', 'PriceBeforeDiscount', 'HasDiscount', 'Dicount']
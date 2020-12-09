from products.models import Product
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import ProductCardSerializer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

# Create your views here.

class ProductCardViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductCardSerializer
    permission_classes = []
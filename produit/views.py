from django.shortcuts import render

from produit.serializers import ProductSerializer
from .models import Product
from rest_framework import viewsets
from .serializers import ProductSerializer
# Create your views here.
class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class= ProductSerializer
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Product, Owner, Property
from .serializers import ProductSerializer, OwnerSerializer, PropertySerializer

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class OwnerViewSet(ModelViewSet):
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer

class PropertyViewSet(ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer


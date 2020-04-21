from rest_framework import viewsets
from ..models import Product, Certificate, Service
from PD6project.backend.serializers import ProductSerializer, CertificateSerializer, ServiceSerializer


class ProductListView(viewsets.ModelViewSet):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CertificateListView(viewsets.ModelViewSet):

    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer


class ServiceListView(viewsets.ModelViewSet):

    queryset = Service.objects.all()
    serializer_class = ServiceSerializer



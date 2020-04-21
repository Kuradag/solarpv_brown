from rest_framework import serializers
from ..models import Product, Certificate, Service


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        # readdress the fields below!
        fields = ['id',
                  'product_name',
                  'cell_technology',
                  'cell_manufacturer',
                  'number_of_cells',
                  'number_of_cells_in_series',
                  'number_of_series_strings',
                  'number_of_diodes',
                  'product_length',
                  'product_width',
                  'product_weight',
                  'superstrate_type',
                  'superstrate_manufacturer',
                  'substrate_type',
                  'substrate_manufacturer',
                  'frame_type',
                  'frame_adhesive',
                  'encapsulate_type',
                  'encapsulant_manufacturer',
                  'junction_box_type',
                  'junction_box_manufacturer']


class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        # readdress the fields below!
        fields = ['id',
                  'report_number',
                  'issue_date',
                  'userID',
                  'standard_ID',
                  'location_ID',
                  'model_number']


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        # readdress the fields below!
        fields = ['id',
                  'service_name',
                  'description',
                  'is_fi_required',
                  'fi_frequency',
                  'standard_ID']

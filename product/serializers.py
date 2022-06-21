from rest_framework import serializers

from product.models import Product, ProductImages


class ProductImageSerialzer(serializers.ModelSerializer):
    # employee = ShowEmployeeSerializer()
    class Meta:
        model = ProductImages
        fields = ('file_name', 'file_path', 'isActive')


class ProductSerialzer(serializers.ModelSerializer):
    images = ProductImageSerialzer(many=True)
    class Meta:
        model = Product
        fields = "__all__"


from rest_framework import serializers
from app.models import *


class ProductModelSerializers(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'









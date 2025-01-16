from rest_framework import serializers
from .models import *


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'description', 'quantity', 'price', 'created_at', 'updated_at']
        read_only=['created_at', 'updated_at']


    def validate_quantity(self, value):
        """
        Ensure the quantity is non-negative.
        """
        if value < 0:
            raise serializers.ValidationError('The quantity cannot be less than 0.')
        return value

    def validate_price(self, value):
        """
        Ensure the price is non-negative.
        """
        if value < 0.0:
            raise serializers.ValidationError('The price cannot be less than 0.0.')
        return value
    
    def create(self, validated_data):
        product= Product.objects.create(**validated_data)
        return product
    

    def update(self, instance, validated_data):
        instance.name=validated_data.get('name', instance.name)
        instance.description=validated_data.get('description', instance.description)
        instance.quantity=validated_data.get('quantity', instance.quantity)
        instance.price=validated_data.get('price', instance.price)
        instance.save()

        return instance 

        



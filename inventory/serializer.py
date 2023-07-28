from rest_framework import serializers
from .models import Category_shopping, Store_shopping, Cart


class Category_shopping_nameserializer(serializers.ModelSerializer):
    class Meta:
        model = Category_shopping
        fields = '__all__'


class Store_shopping_nameserializer(serializers.ModelSerializer):
    class Meta:
        model = Store_shopping
        fields = '__all__'


class Cart_nameserializer(serializers.ModelSerializer):
    group_set = serializers.CharField(source="category_shopping")
    group_set1 = serializers.CharField(source="store_shopping")
    class Meta:
        model = Cart
        fields = ['id','product','quantity','group_set','group_set1']
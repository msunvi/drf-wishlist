from rest_framework import serializers

from .models import User, Product, Category


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'fname', 'lname', 'username', 'age', 'email']


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ["title"]


class ProductSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()

    class Meta:
        model = Product
        fields = ["id", "title", 'price', 'category']

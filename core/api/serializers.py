from rest_framework import serializers
from .models import Category, Product, ProductImage,Projects

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ('id', 'image')

class CategorySerializer(serializers.ModelSerializer):
    subcategories = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ['id', 'name_AR','name_EN', 'subcategories', 'image']

    def get_subcategories(self, obj):
        return CategorySerializer(obj.subcategories.all(), many=True).data

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    images = ProductImageSerializer(many=True,read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'name_AR','name_EN', 'description_AR', 'category', 'images']

class ProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ['id', 'name_EN', 'name_AR','description_AR','description_EN','image','image2']


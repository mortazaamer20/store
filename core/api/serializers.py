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

    pdf_file_url = serializers.SerializerMethodField()

    category = CategorySerializer()
    images = ProductImageSerializer(many=True,read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'name_AR','name_EN', 'description_AR','description_EN', 'category', 'images','pdf_file_url','tag']

    def get_pdf_file_url(self, obj):
        # Return the URL of the PDF file
        if obj.pdf_file:
            return obj.pdf_file.url  # This gives the full URL of the PDF file
        return None

class ProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ['id', 'name_EN', 'name_AR','description_AR','description_EN','image','image2']


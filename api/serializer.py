from rest_framework import serializers

from product.models import (
    ProductVariantsModel,
    ProductImageModel, 
    CategoryModel, 
    ProductModel, 
    BrandModel, 
)


# 1. Kategoriya Serializer
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = ['id', 'name', 'description', 'image']


# 2. Brend Serializer
class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = BrandModel
        fields = ['id', 'name', 'country', 'website', 'logo']


# 3. Mahsulot Rasmlari Serializer
class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImageModel
        fields = ['id', 'image']


# 4. Mahsulot turlari Serializer
class ProductVariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductVariantsModel
        fields = '__all__'

# 5. Mahsulot List Serializer
class ProductListSerializer(serializers.ModelSerializer):  
    variant = serializers.SerializerMethodField()
  
    class Meta:
        model = ProductModel
        fields = ['id', 'name', 'image', 'variant']

    def get_variant(self, obj):
        allowed_variant = obj.variants.filter(allowed=True)
        return ProductVariantSerializer(allowed_variant, many=True).data


# 6. Mahsulot Detail Serializer
class ProductDetailSerializer(serializers.ModelSerializer):
    brand = serializers.SerializerMethodField()
    category = serializers.SerializerMethodField()
    images = serializers.SerializerMethodField()
    variant = serializers.SerializerMethodField()

    class Meta:
        model = ProductModel
        fields = ['id', 'name', 'brand', 'category', 'variant', 'detail', 'images']

    def get_variant(self, obj):
        allowed_variant = obj.variants.filter(allowed=True)
        return ProductVariantSerializer(allowed_variant, many=True).data

    def get_images(self, obj):
        return ProductImageSerializer(
            obj.images.filter(allowed=True), many=True
        ).data

    def get_brand(self, obj):
        if obj.brand and obj.brand.allowed:
            return BrandSerializer(obj.brand).data
        return None

    def get_category(self, obj):
        categories = obj.category.filter(allowed=True)
        return CategorySerializer(categories, many=True).data



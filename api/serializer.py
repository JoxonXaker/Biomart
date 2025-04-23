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
        fields = '__all__'

# 2. Brend Serializer
class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = BrandModel
        fields = '__all__'

# 3. Mahsulot Rasmlari Serializer
class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImageModel
        fields = '__all__'

# 4. Mahsulot turlari Serializer
class ProductVariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductVariantsModel
        fields = '__all__'
    

# 5. Mahsulot Serializer
class ProductSerializer(serializers.ModelSerializer):
    products = serializers.SerializerMethodField()
    images = serializers.SerializerMethodField()
    brand = serializers.SerializerMethodField()
    category = serializers.SerializerMethodField()
    
    class Meta:
        model = ProductModel
        fields = '__all__'

    def get_products(self, obj):
        allowed_products = obj.variants.filter(allowed=True)
        return ProductVariantSerializer(allowed_products, many=True).data

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
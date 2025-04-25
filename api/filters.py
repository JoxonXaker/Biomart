import django_filters
from product.models import ProductModel

from rest_framework.pagination import PageNumberPagination


class ProductFilter(django_filters.FilterSet):
    category = django_filters.NumberFilter(field_name="category__id", lookup_expr="exact")
    brand = django_filters.NumberFilter(field_name="brand__id", lookup_expr="exact")
    min_price = django_filters.NumberFilter(field_name="price", lookup_expr="gte")  # Minimal narx
    max_price = django_filters.NumberFilter(field_name="price", lookup_expr="lte")  # Maksimal narx

    class Meta:
        model = ProductModel
        fields = ['category', 'brand', 'min_price', 'max_price']


# Pagination - 16 yoki 32 mahsulot per page
class ProductPagination(PageNumberPagination):
    page_size = 16  # Default: 16 ta mahsulot
    page_size_query_param = 'per_page'  # URL dan o‘zgartirish: ?per_page=16
    max_page_size = 32  # Eng ko‘pi bilan 16 ta mahsulot
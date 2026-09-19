from django.urls import path
from .views import *

urlpatterns = [
    path("", product_list, name="product_list"),
    path("products/<int:id>", product_detail, name="product_detail"),
    path("product/create", product_create, name="product_create"),
    path("products/update/<int:id>", product_update, name="product_update"),
    path("products/delete/<int:id>", product_delete, name="product_delete"),
]
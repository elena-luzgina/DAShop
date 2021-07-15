from django.urls import path
from shop.views import CategoryListView, ProductListView, ProductDetailsView, OrderCreateView

urlpatterns = [
    path('', CategoryListView.as_view(), name='categories'),
    path('category/<int:category_id>/products', ProductListView.as_view(), name='products'),
    path('category/<int:category_id>/product/<int:product_id>', ProductDetailsView.as_view(), name='product_details'),
    path('category/<int:category_id>/product/<int:product_id>/order', OrderCreateView.as_view(), name='product_order')
]

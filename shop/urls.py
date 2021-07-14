from django.urls import path
from shop.views import CategoryListView, ProductListView, NewOrderView

urlpatterns = [
    path('', CategoryListView.as_view(), name='categories'),
    path('<int:category_id>/products', ProductListView.as_view(), name='products'),
    path('product-details'),
    path('new-order', NewOrderView.as_view(), name='new_order')
]

from django.shortcuts import render
from django.views.generic import DetailView, ListView, CreateView

from shop.models import Category, Product


class CategoryListView(ListView):
    model = Category
    context_object_name = 'categories'
    template_name = 'categories.html'


class ProductListView(ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'products.html'

    def get_queryset(self):
        return Product.objects.filter(category=self.request.url)


class NewOrderView(CreateView):
    form_class = OrderForm
    success_url = '/'
    template_name = 'new-order.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        return response

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import DetailView, ListView, CreateView

from shop.forms import OrderForm
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
        category = self.kwargs['category_id']
        return Product.objects.filter(category=category)


class ProductDetailsView(DetailView):
    model = Product
    context_object_name = 'product'
    template_name = 'product-details.html'
    pk_url_kwarg = 'product_id'


class OrderCreateView(CreateView):
    form_class = OrderForm
    context_object_name = 'order'
    template_name = 'product-order.html'
    success_url = '/'

    def form_valid(self, form: OrderForm):
        self.object = form.save(commit=False)
        self.object.product = self.request.product_id
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

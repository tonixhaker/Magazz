from django.shortcuts import render,redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
from .forms import *
# Create your views here.


class IndexView(TemplateView):
    template_name = 'index.html'


class ProductsView(ListView):
    template_name = "products.html"
    model = Product
    context_object_name = 'products'


class ProductsAdd(CreateView):
    form_class = ProductForm
    template_name = 'addproduct.html'
    success_url = '/products'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        return redirect(self.get_success_url())


class CategoriesView(ListView):
    template_name = "categories.html"
    model = Category
    context_object_name = 'categories'


class CategoriesAdd(CreateView):
    form_class = CategoriesForm
    template_name = 'addcategories.html'
    success_url = '/categories'




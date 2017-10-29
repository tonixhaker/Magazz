from django.shortcuts import render,redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
from django.views.generic.edit import FormMixin
from .forms import *
# Create your views here.


class IndexView(TemplateView):
    template_name = 'index.html'


class ProductsView(ListView):
    template_name = "products.html"
    model = Product
    context_object_name = 'products'


class ProductDetail(ListView):
    template_name = "detailprod.html"
    model = Product
    context_object_name = 'products'

    def get_queryset(self):
        return Product.objects.filter(id=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super(ProductDetail, self).get_context_data(**kwargs)
        productobj = Product.objects.filter(id=self.kwargs['pk'])[0]
        context['feedbacks'] = productobj.review_set.all()
        return context


def add_review(request):
    prod = Product.objects.only('id').get(id=request.POST['prodid'])

    Review.objects.create(username=request.POST['username'],
                          rewiewtext=request.POST['rewiewtext'],
                          rate=int(request.POST['rate']),
                          product=prod)
    return redirect('prodetail',int(request.POST['prodid']))


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




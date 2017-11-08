from django.shortcuts import render,redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView, FormView
from .forms import *


class IndexView(TemplateView):
    template_name = 'index.html'

def index(request):
    return redirect('products')

class ProductsView(ListView):
    template_name = "products.html"
    model = Product
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super(ProductsView, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        filter_val = self.request.GET.get('categoryid', 'all')
        if filter_val == 'all':
            context['products'] = Product.objects.all()
        else:
            context['products'] = Product.objects.filter(category_id=int(filter_val))
        return context


class ProductDetail(ListView):
    template_name = "detailprod.html"
    model = Product
    context_object_name = 'products'

    def get_queryset(self):
        return Product.objects.filter(id=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super(ProductDetail, self).get_context_data(**kwargs)
        productobj = Product.objects.get(id=self.kwargs['pk'])
        context['feedbacks'] = productobj.review_set.all()
        if not self.request.user.is_anonymous():
            context['userr'] = self.request.user
        return context


class ProductDel(DeleteView):
    template_name = "confirm.html"
    model = Product
    success_url = '/products'


class ProductEdit(UpdateView):
    template_name = "addproduct.html"
    model = Product
    form_class = ProductForm
    success_url = '/products'


class CategoryDel(DeleteView):
    template_name = "confirm.html"
    model = Category
    success_url = '/categories'


def add_review(request):
    prod = Product.objects.only('id').get(id=request.POST['prodid'])

    Review.objects.create(username=request.POST['username'],
                          rewiewtext=request.POST['rewiewtext'],
                          rate=int(request.POST['rate']),
                          product=prod)
    return redirect('prodetail', int(request.POST['prodid']))


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


class AddInCart(FormView):
    form_class = CartForm
    template_name = 'addtocart.html'
    success_url = '/products'

    def get_context_data(self, **kwargs):
        context = super(AddInCart, self).get_context_data(**kwargs)
        context['object'] = Product.objects.get(id=self.kwargs['pk'])
        return context

    def form_valid(self, form):
        prodobj = Product.objects.get(id=form.cleaned_data['product'].id)
        Cart.objects.create(quantity=int(form.cleaned_data['quantity']), product= prodobj)
        return redirect('products')


class CartView(ListView):
    template_name = "cart.html"
    model = Cart
    context_object_name = 'cart'

    def get_context_data(self, **kwargs):
        context = super(CartView, self).get_context_data(**kwargs)
        cart = Cart.objects.all()
        res = 0
        for pr in cart:
            res += pr.product.price * pr.quantity
        context['sum'] = res
        return context


class CartDel(DeleteView):
    template_name = "confirm.html"
    model = Cart
    success_url = '/cart'

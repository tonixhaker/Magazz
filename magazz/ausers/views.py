from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect
# Create your views here.
from django.views.generic import CreateView
from .forms import UserForm
from .models import *


class RegisterView(CreateView):
    form_class = UserForm
    template_name = 'register.html'
    success_url = '/products'

    def get_context_data(self, **kwargs):
        context = super(RegisterView, self).get_context_data(**kwargs)
        if not self.request.user.is_anonymous():
            self.template_name = 'logged.html'
            context['user'] = self.request.user
        return context


def login_view(request):
    if not request.user.is_anonymous():
        return render(request, 'logged.html', {'user':request.user})
    return render(request,'login.html')


def logout_view(request):
    logout(request)
    return render(request, 'login.html')


def auth_user_try(request):
    user = User.objects.get(username=request.POST['login'], password=request.POST['password'])
    if user is not None:
        login(request, user)
        return redirect('products')
    else:
        return redirect('login')



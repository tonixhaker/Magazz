from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.generic import CreateView

from .forms import UserForm


class RegisterView(CreateView):
    form_class = UserForm
    template_name = 'register.html'
    success_url = '/products'


def login_view(request):
    return render(request,'login.html')


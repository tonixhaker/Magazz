from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView

# Create your views here.


class indexview(TemplateView):
    template_name = 'index.html'

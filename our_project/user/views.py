from django.shortcuts import render
from django.views.generic import TemplateView,CreateView,FormView
from .forms import MemberForm
# Create your views here.

class Index(TemplateView):
    template_name='index.html'

class Register(CreateView):
    form_class=MemberForm
    template_name='register.html'
    success_url='index'

from django.shortcuts import render
from django.views.generic import TemplateView,CreateView,FormView
from .forms import UserForm
# Create your views here.

class IndexView(TemplateView):
    template_name = 'home.html'

class UserRegistrationView(CreateView):
    form_class = UserForm
    template_name = 'register.html'
    redirect_url = 'home'

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView, TemplateView
from django.contrib.auth.models import User

from .forms import UserForm

# Create your views here.

class UserRegistration(CreateView):
    form_class = UserForm
    queryset = User.objects.all()
    template_name = 'index.html'


class HomeView(TemplateView):
    template_name = 'home.html'

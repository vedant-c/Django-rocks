from django.urls import path, include
from . import views

urlpatterns = [
    path('register/', views.UserRegistration.as_view(), name='user-registration'),
    #path('login/', )
    path('home/', views.HomeView.as_view(), name='home'),
]
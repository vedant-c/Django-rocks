from django.urls import path, include
from . import views

urlpatterns = [
    path('register/', views.UserRegistrationView.as_view(), name='user-registration'),
    #path('login/', )
    path('home/', views.IndexView.as_view(), name='home'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),       # Home page
    path('add/', views.add_view, name='add'),     # Add FAQ page
    path('search/', views.search_view, name='search'),  # Search FAQs page
]

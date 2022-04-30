from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('add_product', views.add_product, name='add_product'),
    path('about', views.about, name='about')
]
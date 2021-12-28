from django.urls import path
from home import views

urlpatterns = [
    path('', views.home, name='home'),
    path('menu/', views.menu, name='menu'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('product_detail/<int:id>/<slug:slug>', views.product_detail, name='product_detail'),
]

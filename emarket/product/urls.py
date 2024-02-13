from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_all_products, name='products'),
    path('add/', views.add_product, name='add_product'),
    path('update/<str:pk>/', views.update_product, name='update_product'),
    path('delete/<str:pk>/', views.delete_product, name='delete_product'),
    path('<str:pk>/', views.get_product_by_id, name='get_product_by_id'),
]
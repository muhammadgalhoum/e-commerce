from django.urls import path
from . import views

urlpatterns = [
  path('', views.store, name="store"),
  path('cart/', views.cart, name="cart"),
  path('checkout/', views.checkout, name="checkout"),
  
  path('create-product/', views.create_product, name="create-product"),
  path('product-detail/<int:pk>/', views.product_detail, name="product-detail"),
  path('update-product/<int:pk>/', views.update_product, name="update-product"),
  path('delete-product/<int:pk>/', views.delete_product, name="delete-product"),
  
  path('update_item/', views.updateItem, name="update_item"),
  path('process_order/', views.processOrder, name="process_order"),
  
  path('search/', views.search, name="search"),
]
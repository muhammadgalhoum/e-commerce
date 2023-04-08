from django.urls import path
from .views import *

urlpatterns = [
  path('products/', productList, name='api-products'),
  path('product-detail/<int:pk>/', productDetail, name='api-product-detail'),
  path('create-product/', productCreate, name='api-create-product'),
  path('update-product/<int:pk>/', productUpdate, name='api-product-update'),
  path('delete-product/<int:pk>/', productDelete, name='api-product-delete'),
  
  path('orders/', orderList, name='api-orders'),
  path('order-detail/<int:pk>/', orderDetail, name='api-order-detail'),
  path('create-order/', orderCreate, name='api-create-order'),
  path('update-order/<int:pk>/', orderUpdate, name='api-order-update'),
  path('delete-order/<int:pk>/', orderDelete, name='api-order-delete'),
  
  path('orderItems/', orderItemList, name='api-orderItems'),
  path('orderItem-detail/<int:pk>/', orderItemDetail, name='api-orderItem-detail'),
  path('create-orderItem/', orderItemCreate, name='api-create-orderItem'),
  path('update-orderItem/<int:pk>/', orderItemUpdate, name='api-orderItem-update'),
  path('delete-orderItem/<int:pk>/', orderItemDelete, name='api-orderItem-delete'),
]
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.decorators import login_required

from .serializers import *
from store.models import *
from users.decorators import allowed_users
# Create your views here.


@api_view(['GET'])
def productList(request):
  products = Product.objects.all()
  serializer = ProductSerializer(products, many=True)
  return Response(serializer.data)


@api_view(['GET'])
def productDetail(request, pk):
  product = Product.objects.get(id=pk)
  serializer = ProductSerializer(product, many=False)
  return Response(serializer.data)


@login_required
@allowed_users(allowed_roles=['admin'])
@api_view(['POST'])
def productCreate(request):
  serializer = ProductSerializer(data=request.data)
  if serializer.is_valid():
    serializer.save()
  return Response(serializer.data)


@login_required
@allowed_users(allowed_roles=['admin'])
@api_view(['POST'])
def productUpdate(request, pk):
  product = Product.objects.get(id=pk)
  serializer = ProductSerializer(instance=product, data=request.data)
  if serializer.is_valid():
    serializer.save()
  return Response(serializer.data)


@login_required
@allowed_users(allowed_roles=['admin'])
@api_view(['DELETE'])
def productDelete(request, pk):
  product = Product.objects.get(id=pk)
  product.delete()
  return Response('Item Successfully Deleted!')


@login_required
@api_view(['GET'])
def orderList(request):
  orders = Order.objects.all()
  serializer = OrderSerializer(orders, many=True)
  return Response(serializer.data)


@login_required
@api_view(['GET'])
def orderDetail(request, pk):
  order = Order.objects.get(id=pk)
  serializer = OrderSerializer(order, many=False)
  return Response(serializer.data)


@login_required
@api_view(['POST'])
def orderCreate(request):
  serializer = OrderSerializer(data=request.data)
  if serializer.is_valid():
    serializer.save()
  return Response(serializer.data)


@login_required
@api_view(['POST'])
def orderUpdate(request, pk):
  order = Order.objects.get(id=pk)
  serializer = OrderSerializer(instance=order, data=request.data)
  if serializer.is_valid():
    serializer.save()
  return Response(serializer.data)


@login_required
@api_view(['DELETE'])
def orderDelete(request,pk):
  order = Order.objects.get(id=pk)
  order.delete()
  return Response('Item Successfully deleted!')


@login_required
@api_view(['GET'])
def orderItemList(request):
  orderItems = OrderItem.objects.all()
  serializer = OrderItemSerializer(orderItems, many=True)
  return Response(serializer.data)


@login_required
@api_view(['GET'])
def orderItemDetail(request, pk):
  orderItem = OrderItem.objects.get(id=pk)
  serializer = OrderItemSerializer(orderItem, many=False)
  return Response(serializer.data)


@login_required
@api_view(['POST'])
def orderItemCreate(request):
  serializer = OrderItemSerializer(data=request.data)
  if serializer.is_valid():
    serializer.save()
  return Response(serializer.data)


@login_required
@api_view(['POST'])
def orderItemUpdate(request, pk):
  orderItem = OrderItem.objects.get(id=pk)
  serializer = OrderItemSerializer(instance=orderItem, data=request.data)
  if serializer.is_valid():
    serializer.save()
  return Response(serializer.data)


@login_required
@api_view(['DELETE'])
def orderItemDelete(request, pk):
  orderItem = Order.objects.get(id=pk)
  orderItem.delete()
  return Response('Item Successfully deleted!')
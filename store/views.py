from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.contrib import messages
# from django.contrib.admin.views.decorators import staff_member_required

import json, datetime

from .models import *
from .forms import ProductForm, ProductDeleteForm
from .utils import cartData, guestOrder
from users.decorators import allowed_users
# Create your views here.


def store(request):
  data = cartData(request)
  cartItems = data['cartItems']
  
  products_list = Product.objects.all()
  
  page = request.GET.get('page', 1)
  paginator = Paginator(products_list, 9)
  
  try:
    products = paginator.page(page)
  except PageNotAnInteger:
    products = paginator.page(1)
  except EmptyPage:
    products = paginator.page(paginator.num_pages)

  context = {'products': products, 'cartItems': cartItems}
  return render(request, 'store/store.html', context)


# @staff_member_required
@allowed_users(allowed_roles=['admin'])
def create_product(request):
  
  data = cartData(request)
  cartItems = data['cartItems']
  
  if request.method == 'POST':
    form = ProductForm(request.POST or None, request.FILES)
    if form.is_valid():
      form.save()
    return HttpResponseRedirect('/')
  else:
    form = ProductForm()
  
  context = {'form': form, 'cartItems': cartItems}
  return render(request, 'store/product-form.html', context)


# @staff_member_required
@allowed_users(allowed_roles=['admin'])
def update_product(request, pk):
  
  data = cartData(request)
  cartItems = data['cartItems']
  
  product = get_object_or_404(Product, id=pk)
  form = ProductForm(instance=product)
  
  if request.method == "POST":
    form = ProductForm(request.POST, request.FILES, instance=product)
    if form.is_valid():
      form.save()
    return HttpResponseRedirect('/')
  else:
    form = ProductForm(instance=product)

  context = {'form': form, 'cartItems': cartItems}
  return render(request, 'store/product-form.html', context)


def product_detail(request, pk):
  data = cartData(request)
  # The following command for updating the Cart data in the Navbar
  cartItems = data['cartItems']
  product = Product.objects.get(id=pk)

  context = {'product': product, 'cartItems': cartItems}
  return render(request, 'store/product-detail.html', context)


# @staff_member_required
@allowed_users(allowed_roles=['admin'])
def delete_product(request, pk):
  
  data = cartData(request)
  cartItems = data['cartItems']
  
  product = get_object_or_404(Product, id=pk)
  
  if request.method == 'POST':
    pro_delete_form = ProductDeleteForm(request.POST, instance=product)
    product.delete()
    return HttpResponseRedirect('/')
  else:
    pro_delete_form = ProductDeleteForm(instance=product)
    
  context = {'pro_delete_form': pro_delete_form, 'cartItems':cartItems}

  return render(request, 'store/delete-product.html', context)


def cart(request):
  data = cartData(request)
  
  cartItems = data['cartItems']
  order = data['order']
  items = data['items']
  
  context = {'items': items, 'order': order, 'cartItems': cartItems}
  return render(request, 'store/cart.html', context)


def checkout(request):
  data = cartData(request)

  cartItems = data['cartItems']
  order = data['order']
  items = data['items']
  
  context = {'items': items, 'order': order, 'cartItems': cartItems}
  return render(request, 'store/checkout.html', context)


def updateItem(request):
  data = json.loads(request.body)
  productId = data['productId']
  action = data['action']
  print("ProductId", productId)
  print("Action", action)
  
  customer = request.user.customer 
  product = Product.objects.get(id=productId)
  order, created = Order.objects.get_or_create(customer=customer, complete=False)
  
  orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)
  
  if action == "add":
    orderItem.quantity += 1
  elif action == "remove":
    orderItem.quantity -= 1
    
  orderItem.save()
  
  if orderItem.quantity <= 0:
    orderItem.delete()
  
  return JsonResponse("Item was added", safe=False)


def processOrder(request):
  transactionID = datetime.datetime.now().timestamp()
  data = json.loads(request.body)
  
  if request.user.is_authenticated:
    customer = request.user.customer
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    
  else:
    customer, order = guestOrder(request, data)
  
  total = float(data['form']['total'])
  order.transaction_id = transactionID

  if total == float(order.get_cart_total):
    order.complete = True
  order.save()
  
  if order.shipping == True:
    ShippingAddress.objects.create(
      customer=customer,
      order=order,
      address=data['shipping']['address'],
      city=data['shipping']['city'],
      state=data['shipping']['state'],
      zipcode=data['shipping']['zipcode'],
    )
  return JsonResponse('Payment complete!', safe=False)


def search(request):
  query = request.GET['q']

  if not query or query.isspace():
    messages.error(request, 'Please refine your search query...')
    return redirect('store')

  search_results = Product.objects.filter(Q(name__icontains=query))
  
  data = cartData(request)
  cartItems = data['cartItems']
  
  context = {'search_results': search_results, 'cartItems': cartItems, 'query': query}
  return render(request, 'store/search.html', context)
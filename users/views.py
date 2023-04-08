from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .forms import ProfileUpdateForm, UserRegisterForm, UserUpdateForm, UserDeleteForm
from .decorators import unauthenticated
from store.utils import cartData
# Create your views here.


@login_required
def profile(request):
  if request.method == 'POST':
    u_form = UserUpdateForm(request.POST, instance=request.user)
    p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
    
    if u_form.is_valid() and p_form.is_valid():
      u_form.save()
      p_form.save()
      
      messages.success(request, (f'Your account has been updated!'), extra_tags='success')
      return redirect('profile')

  else:
    u_form = UserUpdateForm(instance=request.user)
    p_form = ProfileUpdateForm(instance=request.user.profile)
  
  data = cartData(request)
  cartItems = data['cartItems']
  # user_orders = request.user.customer.order_set.all()

  context = {'u_form': u_form, 'p_form': p_form, 'cartItems': cartItems}
  return render(request, 'users/profile.html', context)


@unauthenticated
def register(request):
  if request.method == 'POST':
    form = UserRegisterForm(request.POST)
    if form.is_valid():
      user = form.save(commit=False)
      user.username = user.username.lower()
      user.save()
      username = form.cleaned_data.get('username')
      messages.success(request, f'Account was created for {username} successfully!')
      return redirect('login')
  else:
    form = UserRegisterForm()

  data = cartData(request)
  cartItems = data['cartItems']
  
  context = {'cartItems': cartItems, 'form': form}
  return render(request, 'users/register.html', context)


@unauthenticated
def login_form(request):
  if request.method == 'POST':
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
      login(request, user)
      return redirect('store')
    else:
      messages.info(request, 'Username or Password is incorrect!')

  data = cartData(request)
  cartItems = data['cartItems']

  context = {'cartItems': cartItems}
  return render(request, 'users/login.html', context)


def logoutUser(request):
  logout(request)
  return redirect ('store')


@login_required
def delete_user(request, uid):
  user = get_object_or_404(User, id=uid)
  if request.method == 'POST':
    delete_form = UserDeleteForm(request.POST, instance=user)
    user.delete()
    messages.success(
      request, ('Your account has been deleted successfully.'), extra_tags='success')
    return redirect('store')
  else:
    delete_form = UserDeleteForm(instance=user)

  data = cartData(request)
  cartItems = data['cartItems']
  
  context = {
    'delete_form': delete_form, 'cartItems': cartItems}

  return render(request, 'users/delete_account.html', context)

from django.http import HttpResponse
from django.shortcuts import redirect


def unauthenticated(view_fucn):
  def wrapper_func(request, *args, **kwargs):
    if request.user.is_authenticated:
      return redirect('store')
    else:
      return view_fucn(request, *args, **kwargs)
    
  return wrapper_func


def allowed_users(allowed_roles=[]):
  def decorator(view_func):
    def wrapper_func(request, *args, **kwargs):
      group = None
      if request.user.groups.exists():    # Check if the user has one or more groups.
        group = request.user.groups.all()[0].name    # Getting the first group name.
        if group in allowed_roles:  
          return view_func(request, *args, **kwargs)
        else:
          return HttpResponse("You are not authorized to view this page!")
    return wrapper_func
  return decorator
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

class Customer(models.Model):
  user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE, related_name="customer")
  name = models.CharField(max_length=50, null=True)
  email = models.EmailField(max_length=50, null=True)
  date_created = models.DateTimeField(auto_now_add=True, null=True)
  
  def __str__(self):
    return self.name


class Product(models.Model):
  name = models.CharField(max_length=100)
  price = models.DecimalField(max_digits=6, decimal_places=2)
  desc = models.TextField(null=True, blank=False)
  digital = models.BooleanField(default=False, null=True, blank=False)
  image = models.ImageField(null=True, blank=True)
  
  def __str__(self):
    return self.name
  
  @property
  def imageURL(self):
    try:
      url = self.image.url
    except:
      url= ''
    return url
  
  def get_absolute_url(self):
    return reverse("product-detail", kwargs={"pk": self.pk})


class Order(models.Model):
  customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
  date_ordered = models.DateTimeField(auto_now_add=True)
  complete = models.BooleanField(default=False, null=True, blank=False)
  transaction_id = models.CharField(max_length=100, null=True)
  
  def __str__(self):
    return f"Oreder No. {str(self.id)}"
  
  @property
  def shipping(self):
    shipping = False
    orderitems = self.orderitem_set.all()
    for item in orderitems:
      if item.product.digital == False:
        shipping = True
    return shipping
  
  @property
  def get_cart_total(self): # return the final price for all cart items (The Order)
    orderitems = self.orderitem_set.all()
    total = sum([item.get_total for item in orderitems])
    return total
  
  @property
  def get_cart_items(self): # return the total number of cart items
    orderitems = self.orderitem_set.all()
    total = sum([item.quantity for item in orderitems])
    return total


class OrderItem(models.Model):
  product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)
  order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True)
  quantity = models.IntegerField(default=0, null=True, blank=True)
  date_added = models.DateTimeField(auto_now_add=True)
  
  def __str__(self):
    return f"{self.product.name} in Oreder No. {str(self.order.id)}"
  
  @property
  def get_total(self):  # calculate the total price for each item
    total = self.product.price * self.quantity
    return total


class ShippingAddress(models.Model):
  customer = models.ForeignKey(Customer,on_delete=models.SET_NULL, null=True, blank=True)
  order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True)
  address = models.CharField(max_length=200, null=True)
  city = models.CharField(max_length=50, null=True)
  state = models.CharField(max_length=50, null=True)
  zipcode = models.CharField(max_length=50, null=True)
  date_added = models.DateTimeField(auto_now_add=True)
  
  def __str__(self):
    return f"\"{self.address}\" is a Shipping Address for the Order No. {str(self.order.id)}"
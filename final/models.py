from django.db import models
from django.contrib.auth.models import AbstractUser, User
from decimal import Decimal

# Create your models here.

class User(AbstractUser):
    email = models.CharField(max_length=200, blank=True, null=True)
    street = models.CharField(max_length = 64, blank=True, null=True)
    houseNr = models.CharField(max_length=12, blank=True, null=True)
    city = models.CharField(max_length=12, blank=True, null=True)
    phone_number = models.CharField(max_length = 12, blank=True, null=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    activated = models.BooleanField(null=True, default=False)
    usertype = models.CharField(max_length = 12,null=True, blank=True)

    def __str__(self):
        return f"{self.username}"

class Ingredient(models.Model):
    name = models.CharField(max_length = 64)
    
    def __str__(self):
        return f"{self.name}"

    def serialize(self):
        
        return {
            "name":self.name
        }

class MealType(models.Model):
    name = models.CharField(max_length = 64)
    
    def __str__(self):
        return f"{self.name}"

    def serialize(self):
        return {
            "name":self.name
        }
        
class Meal(models.Model):
    name = models.CharField(max_length = 64)
    size = models.CharField(max_length = 10, null = True, blank=True)
    price = models.DecimalField(max_digits=7,decimal_places=2)
    description = models.CharField(max_length = 64, null = True, blank=True)
    meal_type = models.ForeignKey(MealType, on_delete=models.CASCADE, default=None, blank=True, null=True, related_name="meal_type")
    ingredients = models.ManyToManyField(Ingredient, default=None, blank=True, null=True, related_name="ingredients")
    image = models.ImageField(null = True, blank=True)

    def __str__(self):
        return f"ID:{self.id} name:{self.name} meal_type:{self.meal_type} size:{self.size} price:{self.price} describtion:{self.description} img:{self.image}"

    def serialize(self):
        return {
            "ingredients":self.ingredients.all()
        }

    #if image doesn't exist return empty string, no error on the page
    @property
    def imageURL(self):
        try:
            url = '../static/final/IMG/' + self.image.url
        except:
            url = ''
        return url
    @property
    def getIngredients(self):
        return self.ingredients.all()

class Order(models.Model):
    placed_time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, related_name="creator")
    complete = models.BooleanField(default=False, null=True, blank=False)
    transaction_id = models.CharField(max_length=200,null=True)
    description = models.TextField(default="",blank=True,null=True)
    delivery = models.DecimalField(max_digits=7,decimal_places=2, null=True, blank=True)
    total = models.DecimalField(max_digits=7,decimal_places=2, null=True, blank=True)
    transactionType = models.CharField(max_length=12, null=False)
    
    def __str__(self):
        return f"ID:{self.id} placed_time:{self.placed_time} user:{self.user}"

    #counting total value of the cart
    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total

    @property
    def get_order_total(self):
        return self.total

class OrderItem(models.Model):
    product = models.ForeignKey(Meal, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total

class DeliveryAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200, null=False)
    surname = models.CharField(max_length=200, null=False)
    street = models.CharField(max_length=200, null=False)
    houseNr = models.CharField(max_length=12, null=False)
    city = models.CharField(max_length=12, null=False)
    phoneNr = models.CharField(max_length=12, null=False)
    transactionType = models.CharField(max_length=12, null=False)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"ID:{self.id} Addresss:{self.street} {self.houseNr} {self.city}"

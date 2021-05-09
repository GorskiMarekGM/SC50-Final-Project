from django.contrib import admin
from .models import *

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    users = ("id", "name")

class MealAdmin(admin.ModelAdmin):
    meals = ("id","name","size","price","describtion","meal_type","ingredients")

class IngredientAdmin(admin.ModelAdmin):
    ingredients = ("id", "name")

class MealTypeAdmin(admin.ModelAdmin):
    types = ("id", "name")

class OrderAdmin(admin.ModelAdmin):
    orders = ("id", "placed_time", "user")


admin.site.register(Meal,MealAdmin)
admin.site.register(User,UserAdmin)
admin.site.register(Ingredient,IngredientAdmin)
admin.site.register(MealType,MealTypeAdmin)
admin.site.register(Order,OrderAdmin)
admin.site.register(OrderItem)
admin.site.register(DeliveryAddress)
import json
from .models import *
from django.contrib.auth.tokens import PasswordResetTokenGenerator

from django.contrib import messages


def cookieCart(request):
    try:
        cart = json.loads(request.COOKIES['cart'])
    except:
        cart = {}

    items = []
    order = {'get_cart_total':0, 'get_cart_items':0,}
    cartItems = order['get_cart_items']

    for i in cart:
        try:
            cartItems += cart[i]["quantity"]

            product = Meal.objects.get(id = i)
            total = (product.price * cart[i]["quantity"])

            order['get_cart_total'] += total
            order['get_cart_items'] += cart[i]["quantity"]

            item = {
                'product':{
                    'id':product.id,
                    'name':product.name,
                    'size':product.size,
                    'meal_type':product.meal_type,
                    'price':product.price,
                    'imageURL':product.imageURL,
                },
                'quantity':cart[i]["quantity"],
                'get_total':total,
            }
            items.append(item)
        except:
            pass
    
    return {'cartItems':cartItems, 'order':order, 'items':items}


def cartData(request):
    if request.user.is_authenticated:
        #one to one relationship with user
        user = request.user
        order, created = Order.objects.get_or_create(user = user, complete = False)
        # print("USER: "+user.name)
        #get all the orderitems that has order as a parent
        items = order.orderitem_set.all()
        print(items)
        cartItems = order.get_cart_items
        print(cartItems)
    else:
        #assigning data from cookie in utils.py
        cookieData = cookieCart(request)
        cartItems = cookieData['cartItems']
        order = cookieData['order']
        items = cookieData['items']
    
    return {'cartItems':cartItems, 'order':order, 'items':items}


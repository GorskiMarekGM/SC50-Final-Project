from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from datetime import datetime


from .models import *
from .utils import *


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def main(request):

    #assigning data from data in utils.py
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    meal1 = Meal.objects.get(id=1)
    meal2 = Meal.objects.get(id=2)
    meal3 = Meal.objects.get(id=3)
    recomended_list = []
    recomended_list.append(meal1)
    recomended_list.append(meal2)
    recomended_list.append(meal3)

    return render(request, "final/main.html",{
        "cartItems":cartItems,
        "items" : items,
        "order" : order,
        "recomended_list":recomended_list
    })

# Displaying lists of all meals
def meals(request):
    meals_list = Meal.objects.all()

    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    return render(request, "final/index.html",{
        "meals_list" : meals_list,
        "cartItems":cartItems,
        "items" : items,
        "order" : order,
    })

def events(request):
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    return render(request, "final/events.html",{
        "cartItems":cartItems,
        "items" : items,
        "order" : order,
    })

def contact(request):
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    return render(request, "final/contact.html",{
        "cartItems":cartItems,
        "items" : items,
        "order" : order,
    })


def cart(request):
    #assigning data from data in utils.py
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    if request.user.is_authenticated:
        total = float(order.get_cart_total)
    else:
        total = float(order['get_cart_total'])

    return render(request, "final/cart.html",{
        "cartItems":cartItems,
        "items" : items,
        "order" : order,
        "user" : request.user,
        "total":total,
    })

def meal(request, id):

    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']
    photo = Meal.objects.get(id=id)

    return render(request, "final/meal.html",{
        "cartItems":cartItems,
        "items" : items,
        "order" : order,
        "id" : id,
        "image" : photo.imageURL
    })

def thank_you(request):
    
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    return render(request, "final/thank_you.html",{
        "cartItems":cartItems,
        "items" : items,
        "order" : order,
    })

################# CHECKOUT

def checkout(request):
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    deliveryData = {
        'email':None,
        'phone_number':None,
        'city':None,
        'street':None,
        'houseNr':None,
    }

    deliveryData['email'] = request.POST["email"]
    deliveryData['phone_number'] = request.POST["phoneNr"]
    deliveryData['city'] = request.POST["city"]
    deliveryData['street'] = request.POST["street"]
    deliveryData['houseNr'] = request.POST["houseNr"]
    
    total = float(order['get_cart_total'])

    return render(request, "final/checkout.html",{
        "cartItems":cartItems,
        "items" : items,
        "order" : order,
        "user" : request.user,
        "total":total,
        "deliveryData":deliveryData,
        "email":deliveryData['email'],
        "phone_number":deliveryData['phone_number'],
        "city":deliveryData['city'],
        "street":deliveryData['street'],
        "houseNr":deliveryData['houseNr'],
    })

###### process order

def process_order(request):
    transaction_id = datetime.now().timestamp()
    data = json.loads(request.body)
    data2 = cartData(request)
    cartItems = data2['cartItems']
    order = data2['order']
    items = data2['items']

    deliveryData = {
        'email':data['form']['email'],
        'phone_number':data['form']['phoneNr'],
        'city':data['delivery']['city'],
        'street':data['delivery']['street'],
        'houseNr':data['delivery']['houseNr'],
    }
    

    # reading data from stringify json format in JS script inside checkout.html
    total = float(data['form']['total'])
    
    # check for personal collect
    delivery_transaction_type = str(data['form']['transactionType'])
    if delivery_transaction_type == "odbior":
        delivery_cost = 0
    else:
        delivery_cost = 5

    orderMess = "Adres:\n"
    orderMess += "Ul: " + str(data['delivery']['street']) + " " + str(data['delivery']['houseNr'])+ "\n"
    orderMess += "M: " + str(data['delivery']['city'])+ "\n"
    orderMess += "Tel: " + str(data['form']['phoneNr'])+ "\n"+ "\n"

    # Food part of the message
    for i in items:
        orderMess += str(i['quantity']) + " x " + str(i['product']['name'])
        if(str(i['product']['meal_type']) == "Pizza"):
            orderMess += " "+str(i['product']['size'])
        orderMess += "\n"

    #add comment
    try:
        comment = str(data['comment']['comment'])
    except:
        comment = ''

    return JsonResponse('Thank you for order', safe=False)


####### Update item


def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    print('Action: ', action)
    print('productId: ', productId)

    user = request.user
    product = Meal.objects.get(id = productId)
    order, created = Order.objects.get_or_create(user = user, complete = False)
    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action =='add':
        orderItem.quantity = (orderItem.quantity + 1)
    if action =='remove':
        orderItem.quantity = (orderItem.quantity - 1)
    if action =='delete':
        orderItem.quantity = 0

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Item was added', safe=False)






### API ROUTES

def all_meals(request,id):
    #Cart Data
    data = cartData(request)
    meals_list = Meal.objects.all()
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    meal = Meal.objects.get(id = id)
    ingredients = meal.ingredients.all()

    data = {
        "id": meal.id,
        "name":meal.name,
        "size":meal.size,
        "meal_type":meal.meal_type.name,
        "price":meal.price,
        "description":meal.description,
        "imageURL":meal.imageURL,
    }

    return JsonResponse(data)

def pizza_api(request,id,size):
    #Cart Data
    data = cartData(request)
    meals_list = Meal.objects.all()
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    meal = Meal.objects.get(id = id)
    ingredients = meal.ingredients.all()
    
    #Get this same item, but with difeerent size
    name = meal.name
    pizza = Meal.objects.filter(name = name).get(size = size)

    data = {
        "id": pizza.id,
        "name":pizza.name,
        "size":pizza.size,
        "meal_type":pizza.meal_type.name,
        "price":pizza.price,
        "description":pizza.description,
    }

    return JsonResponse(data)

def mealIngredients(request,meal_id):
    
    meal = Meal.objects.get(id=meal_id)
    ingredients = meal.ingredients.all()
    return JsonResponse([ingredient.serialize() for ingredient in ingredients], safe=False)
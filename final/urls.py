from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", views.main, name="index"),
    path("meals/", views.meals, name="meals"),
	path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),
	path('update_item/', views.updateItem, name="update_item"),
	# path('update_cart/', views.updateCart, name="updateCart"),
	path('events/', views.events, name="events"),
	path('contact/', views.contact, name="contact"),
	path('thank_you/', views.thank_you, name="thank_you"),
	path('process_order/', views.process_order, name="process_order"),
	path('meal/<int:id>/', views.meal, name="meal"),
	# path('pizza/<int:id>/', views.pizza, name="pizza"),
	# path('user/', views.user_profile, name="user"),
	# path('edit/', views.edit_user, name="edit_user"),
	# path('delete/', views.user_delete, name="user_delete"),
	# path('pass_change/', views.user_pass_change, name="user_pass_change"),

    #API ROUTES
	path('all_meals/<int:id>', views.all_meals, name="all_meals"),
	path('pizza_api/<int:id>/<int:size>', views.pizza_api, name="pizza_api"),
	path('ingredients/<int:meal_id>', views.mealIngredients, name="mealIngredients"),
    
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
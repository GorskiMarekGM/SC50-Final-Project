<h2> Restaurant project </h2> 
<h3> Introduction </h3>
At the begining i want to mantion that this course gave me a lot of knowledge witch I started to use as fast as I could. Therefore I have created an application for local restaurant in my town. <br>
<br>

This project is part of something bigger that I have created and spent ton of time on developing and learning.<br>
You can find my website under this link: <br>
https://restauracjaverona.pl/
<br>

It includes:
<ul>
<li> Google API</li>
<li> Paypal API</li>
<li> Email sending</li>
<li> cookies</li>
<li> many more</li>
</ul>
<br>

In this project I have focused on cookies, and cart the most. I think it satisfies requirements the most, because it is something out of the scope of the course, but still the most JavaScript and Python thing.

<h3> My files </h3>
<br>
<h4> JavaScript <h4>
<br>
<ul>
 <li><b>Cart.js </b>- Adding new items to the cart stored in cookies, and managing updating orders.</li>
 <li><b>Meal.js </b>- iFetching all the meals from my meals API. I am also getting ingredients for the meals, and changing the size of pizzas</li>
 <li><b>openCard.js </b>- Manages the whole card click, not just single button.</li>
 <li><b>parallax.min.js </b>- Parallax background in events.html</li>
 <li><b>popup.js</b> - Rendering a popup after adding new meal to the cart. It featch the data from all_meals API</li>
 <li><b>script.js</b> - Adjusting the footer based on the website height </li>
 <li><b>search.js</b> - Searching functionality in menu site for desktop and mobile</li>
</ul>

<br>
<h4> Python <h4>
<br>
<ul>
 <li><b>views.py </b> 
 <ul>
  <li><b>def main() </b>- renders main page of the restaurant with the cart data, and recomendations.</li>
  <li><b>def meals() </b>- renders menu with meals with the cart data, and meals data.</li>
  <li><b>def events() </b>- renders events page with the cart data.</li>
  <li><b>def contact() </b>- renders contact page with the cart data.</li>
  <li><b>def cart() </b>- renders cart page with the cart data.</li>
  <li><b>def meal() </b>- renders single meal page with the cart data.</li>
  <li><b>def thank_you() </b>- renders thank_you page with the cart data.</li>
  <li><b>def checkout() </b>- renders checkout page with the cart data, and delivery informations from cart (previous page)</li>
  <li><b>def process_order() </b>- it is processing the order, and adding delivery cost</li>
  <li><b>def updateItem() </b>- based on the action it is adding, removing or deleting order items</li>
  <br>
  API functions
  <li><b>def all_meals() </b>- returns all meals from DB</li>
  <li><b>def pizza_api() </b>- returns pizzas based on  the size</li>
  <li><b>def mealIngredients() </b>- returns pall the ingredients of meal</li>
  </ul>
 </li>
 <br>
 <li><b>utils.py </b>- cart management</li>
 <li><b>models.py </b>- stores information about all models</li>
</ul>

<br>
<h4> HTML <h4>
<br>
<ul>
 <li><b>main </b>- Main page with map to restaurant, slider, recomentation list, links to contact page and events page</li>
 <li><b>checkout </b>- Display summary of the order with all order items, shows 3 different payments options</li>
 <li><b>contact </b>- Display information page with phones to restaurant, and open hours shedule</li>
 <li><b>events </b>- little desctiption on how to reserve local for parties</li>
 <li><b>index </b> - displays list of all meals available in menu</li>
 <li><b>layout </b> - layout for the page </li>
 <li><b>meal</b> - display single meal based on its ID</li>
 <li><b>thank_you</b> - page rendered after selecting payment option</li>
</ul>
<br>
<h4> CSS <h4>
<br>
I have decided to copy all my CSS files from main project. 

<br>
<h3>Getting Started</h3>
<hr>
Download the distribution code from https://github.com/GorskiMarekGM/SC50-Final-Project and unzip it. <br>
In your terminal, cd into the final_project directory. <br>
Run python manage.py makemigrations network to make migrations for the network app. <br>
Run python manage.py migrate to apply migrations to your database. <br>



<h3>Welcome to my final project – “Verona restaurant”</h3>

Idea of this project came from the real aplication which I have created during CS50 course, my boss asked me to do application for online ordering for the restaurant in which I was working. This project is smaller part of my website, because here I just want to focus on cart, and cookies. To create this project I had to relay on all the knowledge which I have gained during this course. You can find whole website here https://restauracjaverona.pl/

My website is for users which live close to restaurant, it allows them to order food to their houses, or collecting it personally in restaurant. Moreover users can browse whole menu, they can also add items to cart even when they are not logged in. Cart stores all their data in cookies, so even if they close browser, they still have their orders.

When you arrive at the homepage you can see the big slider with the photos of the restaurant. You can also see current meal of the day, which is special for every week. And a little description of the restaurant which changes during special events. In information part, you can see two cards which links to contact, and events pages. You can also see current recommendations, and the location of restaurant on google maps.

Menu page displays all of the meals, and after you click them they display additional information about that meal for example ingredients, description, price. At the top of the screen you can search for particular dish.

In the upper right corner you can see the cart icon, when you click it you will be directed to cart page, where all your orders are displayed, you can live edit the quantity of the products or change pizza size. From this page you can go further to checkout or go back to menu. Before moving to checkout user will be asked to add additional information about address in order to calculate delivery distance.

This is all about my website, hope you enjoy 


<hr>
<h3>Requirements</h3>
<br>

1. Your web application must be sufficiently distinct from the other projects in this course (and, in addition, may not be based on the old CS50W Pizza project), and more complex than those.
2. Your web application must utilize Django (including at least one model) on the back-end and JavaScript on the front-end.
3. Your web application must be mobile-responsive.
4. In a README.md in your project’s main directory, include a writeup describing your project, and specifically your file MUST include all of the following:
Under its own header within the README called Distinctiveness and Complexity: Why you believe your project satisfies the distinctiveness and complexity requirements, mentioned above. What’s contained in each file you created. How to run your application. Any other additional information the staff should know about your project.
5. If you’ve added any Python packages that need to be installed in order to run your web application, be sure to add them to a requirements.txt file!

<hr>
<br>
<h4>Requirement No. 1</h4>
In my opinion my project is sufficiently distinct from the other projects in this course, and satisfies the distinctiveness and complexity requirements since this project includes this features:

- A JavaScript cookie feature which stores all the user cart information
- Many clicable buttons
- Search function which helps to navigate in meals
- Javascript slider in main page

<h4>Requirement No. 2</h4>
My application utilize Django on the back-end and JavaScript on the front-end. The data base include 7 models

User - stores basic information about user such as it's name, surname, email, phone number, usertype and address
Ingredient - names of ingredients used in particular meal
MealType - there is several meal types this model is connected with meal through foreign key
Meal - all detiled information about meal available to order such as name, size, price, description, mealtype, ingredients, image
Order - when the user makes order all necesarry data is stored here, referance to user which orders that, status of order (complete or not), comments from users, delivery type, total value of the cart and the type of transaction (cash, card)
OrderItem - referance to meal with it's quantity
DeliveryAddress - all the data necessary for making proper delivery (full address), transaction type and referance to user

<h4>Requirement No. 3</h4>
This web application is mobile-responsive. The responsiveness of the app is included in the style.css file, the css attributes of each Html elements of text and graphics keeps the scale for a better view in a screen sizes and resolutions.

<h4>Requirement No. 4</h4>
There is a lot of files in this project many of them was auto-created by django, but also there is a lot of files created by me. I will give a quick description of them.

<h3> My files </h3>
<br>
<h4> JavaScript </h4>
<br>
<ul>
 <li><b>Cart.js </b>- Adding new items to the cart stored in cookies, and managing updating orders.</li>
 <li><b>Meal.js </b>- Fetching all the meals from my meals API. I am also getting ingredients for the meals, and changing the size of pizzas</li>
 <li><b>openCard.js </b>- Javascript function for managing user click. Before using it I had trouble to manage whole card click. User was not able to click on whole card just on the button. This function fixes it.</li>
 <li><b>parallax.min.js </b>- Parallax background in events.html site</li>
 <li><b>popup.js</b> - Rendering a popup after adding new meal to the cart. It featch the data from all_meals API</li>
 <li><b>script.js</b> - Adjusting the footer based on the website height </li>
 <li><b>search.js</b> - Searching functionality in menu site for desktop and mobile</li>
</ul>

<br>
<h4> Python </h4>
<br>
<ul>
 <li><b>views.py </b> - This is one of the most important files. I am storing here logical behavior of the app. First it makes the most important imports in order for the app to work properly. Then it renders templates with all necessary data.
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
  <li><b>def pizza_api() </b>- returns pizzas based on the size</li>
  <li><b>def mealIngredients() </b>- returns all the ingredients of meal</li>
  </ul>
 </li>
 <br>
 <li><b>utils.py </b>- cart management</li>
 <li><b>models.py </b>- stores information about all 7 models</li>
 <li><b>admin.py </b>- here I registered the app models for management in django web administrator</li>
 <li><b>urls.py </b>- each valid path route is declared here</li>
</ul>

<br>
<h4> HTML </h4>
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

<h4>Requirement No. 5</h4>
 All packages was added to requirements.txt file


<br><br><br>
<h5>Getting Started</h5>
<hr>
Download the distribution code from https://github.com/GorskiMarekGM/SC50-Final-Project and unzip it. <br>
In your terminal, cd into the final_project directory. <br>
Run python manage.py makemigrations network to make migrations for the network app. <br>
Run python manage.py migrate to apply migrations to your database. <br>

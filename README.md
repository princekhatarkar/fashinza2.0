# fashinza2.0
Product service APIs for an e-Commerce website

Step 1:
Make sure PostgreSQL is up and running and connected to Django

Step 2:
If there are any changes in models.py then go to \fashinza2.0\fashinza2.0\ and run this command in terminal> python manage.py makemigrations
then
> python manage.py makemigrations 

Step 3:
To Run Server run this command> python manage.py runserver

Open Endpoints
Open endpoints require no Authentication

Endpoints for the APIs

Show Accessible APIs : GET /
Add A New Product : POST /ecart/
Show All Products : GET /ecart/
Show A Product : GET /ecart/:pk/
Update A Product : PUT /ecart/:pk/
Delete A Product : DELETE /ecart/:pk/
Search Products : GET /ecart/products/

Sample input to Add or Update A New Product: {"name":"PRODUCT_NAME", "quantity":PRODUCT_COUNT, "category_id":[INTEGER_ARRAY]}

Input example: {"name":"superdry", "quantity":100, "category_id":[4,5]}

For searching Product by Name or Category ID, click on Filters and Search.
# django_ecommerce



**A Django-based backend template for an eCommerce web app.
It aims to be easily extensible for any functional e-commerce application.
So, it packs all the basic features of a basic eCommerce website i.e. User Authentication, Customer Payments,
 Refunds, Social network integration etc with dynamic web pages having Bootstrap & jQuery support.**





## Visit it Online

[mD ecommerce webapp](http://mradul.pythonanywhere.com/)





## To run on Local Machine



- Install Python and Django, preferably in a virtualenv
- Copy the static folder and save it just outside this repository
- Change to directory and run following commands
- python manage.py makemigrations
- python manage.py migrate
- python manahe.py collectstatic
- python manage.py runserver
- Open browser and go to:<http://127.0.0.1:8000/>



## Current Features



- User SignUp/Login
- A fully functional user contact form on "Contact" page. It notifies the admin of the submission via email(having the user's name,email and message). Also, the submission triggers an autoreply to the user from the admin's gmail account.
- Dynamic wepages
- Customer Payments through the Donate button on HomePage.
- Customer payment recieving in admin's stripe account
- Support Bootstrap and jQuery using configured static directory outside of the app repository(for e.g. in virtualenv folder outside of the app repo in my local machine).
- Uses both function and class based views.



## Upcoming Features



- Search Functionality.

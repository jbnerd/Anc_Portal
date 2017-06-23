# ANC Portal

ANC stands for the famous All Night Canteen of BITS Pilani, which serves a variety of good quality food items with the uniqueness of operating till late nights. It often sees much crowd pouring in at night resulting in large queues near the billing counter. To reduce this queue, the then President of the Students' Union (2016-17) proposed the idea of ANC Portal.

This website would automate the billing process reducing the size of queues near the billing counter. This website was developed and hosted under coding club after getting the project of developing such a system.

The backend for the website based system was writtend in `Django 1.9.1` in `python 3.5.2`.

# Use case

- An online ordering website is hosted on a public server for students to order their food. The order is recorded on the server's database.
- A tablet is kept at the ANC where the user will have to confirm the order that they placed to generate the bill. The student shall not be charged for their orders until the bill is generated.
- Each student user can login to the website to place their orders using their college email accounts.
- Each of the student user is prompted for basic information which is not readily available via the gmail API.
- Each of them has to set a 6 digit personal pin which is used to verify the placed order and generate the bill.
- After each order a system generated mail is sent to the respective user's email account, stating the details of the order along with a 6 digit random number.
- A combination of the sent random number and the personal pin shall act as the verification model for confirming the order.
- If a user wishes to cancel the order, they can do so by returning the unused bill to the billing operator, who can then use his special credentials to cancel the order with the given bill number.

# Setup Instructions

- This webiste is deployed on a trial basis on [heroku](https://www.heroku.com/)'s freely available server space.
- This [tutorial](https://djangogirls.gitbooks.io/django-girls-tutorial-extensions/heroku/) was followed to deploy the website on [heroku](https://www.heroku.com/)

# Python Package Dependencies

- virtualenv
- django 1.9.1
- gunicorn and nginx
- oauthlib 2.0.0 and python-social-auth
- django-whitenoise
- psycopg2

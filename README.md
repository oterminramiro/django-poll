# Django Poll APP

Simple poll api usign Django Rest framework

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

- Generate virtualenv: ``virtualenv env``
- Activate it: ``source env/bin/activate``
- Install requirements: ``pip install -r requirements.txt``
- Run migrations: ``python manage.py migrate``
- Start the app: ``python manage.py runserver``

### Make authenticated request
- Generate user at: ``/polls/customer_create``
- Get your token at: ``/polls/api-token-auth/``
- Send your request with the next header: ``Authorization: Token YOUR_TOKEN``

## Built With

* [Django](https://www.djangoproject.com/) - The web framework used
* [Django REST Framework](https://www.django-rest-framework.org/) - Rest API

## Authors

* **Otermin Ramiro** - [oterminramiro](https://github.com/oterminramiro)

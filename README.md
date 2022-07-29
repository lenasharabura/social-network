# Social Network API

A simple REST API for social network.

## Installing / Getting started

Python 3 must be already installed

```shell
git https://github.com/lenasharabura/social-network.git
cd social-network
python -m venv venv
venv/scripts/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver  # start Django project
```

## Features

* user signup
* user login
* JWT authentication
* post creation, details
* post like, unlike 
* analytics about how many likes was made. Example url /api/analitics/?date_from=2020-02-02&date_to=2020-02-15
* user activity show when user was login last time and when he mades a last request to the service.





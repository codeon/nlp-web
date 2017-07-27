# Setting up a webservice framework (Django)

```
$ mkdir api-service
$ cd api-service
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install django
$ django-admin startproject demoapp
$ python manage.py startapp nlp-web
```

# To start using this repo
```
$ git clone git@github.com:codeon/nlp-web.git
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
$ cd demoapp
$ python manage.py runserver
```

Now you can open `http://localhost:8000/parse_text?input=This+is+a+sentence` to see it in action.

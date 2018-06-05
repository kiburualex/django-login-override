# Project Title

Email Or Username Model Backend

### Requirements

```
Django
```

### Installing

```
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

### Description

This mini project provides a class that overrides the default model backend authentication class. Instead of the default 
email/ password login, now one can login using any user model field as defined in the decorators.py file.

add the EmailOrUsernameModelBackend class from the decorators.py file to the AUTHENTICATION_BACKENDS array just before the default django authentication backend model

```
AUTHENTICATION_BACKENDS = [
    'decorators.EmailOrUsernameModelBackend',
    'django.contrib.auth.backends.ModelBackend',
]
```




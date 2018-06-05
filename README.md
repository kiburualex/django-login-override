# Project Title

Email Or Username Model Backend Authentication

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

### Run

Default user details
```
name:admin
email:admin@example.com
password:admin123
```

### Description

This mini project provides a class that overrides the default model backend authentication class. Instead of the default 
email/ password login, now one can login using any user model field or name field as defined in the decorators.py file.

add the EmailOrUsernameModelBackend class from the decorators.py file to the AUTHENTICATION_BACKENDS list just before the default django authentication backend model statement.

```
AUTHENTICATION_BACKENDS = [
    'decorators.EmailOrUsernameModelBackend',
    'django.contrib.auth.backends.ModelBackend',
]
```




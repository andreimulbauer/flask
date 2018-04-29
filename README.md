[![Build Status](https://travis-ci.org/python-sorocaba/flask_tutorial.svg?branch=master)](https://travis-ci.org/python-sorocaba/flask_tutorial)

# Flask NPS Platform
This is an NPS Platform based on flask. It is an educational project that I developed to learn how Flask works.

## How setup this project?
Create your virtualenv (using python3):

```
$ python3 -m venv .venv
```

Install requirements:

```
$ pip install -r requirements.txt
```

Configure your local `.env` file:

```
$ cp contrib/env-sample .env
```

Open `.env` with your favorite editor and configure your paramethers. Run your server with command below:

```
$ python manage.py runserver
```

More information? Follow explanatory videos below.

## How to execute queries manually?

Inside on your virtualenv:
```
$ python manage.py shell
```

Import db and model:
```
from tvseries.ext import db
from tvseries.core.models import TVSerie
```

Bind your session with your application:
```
db.app = app
```

Quering example:
```
db.session.query(TVSerie).all()
```

If operation is "create", "update" or "delete" dont forget to run commit operation to confirm operation:
```
db.session.commit()
```

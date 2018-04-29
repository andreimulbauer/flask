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

## 1.0 - Flask and the most basic application of the world!

- See release code: https://github.com/rafaelhenrique/flask_tutorial/tree/1.0
- See explanation about release: https://github.com/rafaelhenrique/flask_tutorial/releases/tag/1.0
- See video: https://www.youtube.com/watch?v=i5ewUO-zX4g

## 2.0 - Flask starting our TV series app!

- See release code: https://github.com/rafaelhenrique/flask_tutorial/tree/2.0
- See explanation about release: https://github.com/rafaelhenrique/flask_tutorial/releases/tag/2.0
- See video: https://www.youtube.com/watch?v=CxVhTwGtb3Y

## 3.0 - "Beautiful" banners, Jinja2 and starting SQLAlchemy world!

- See release code: https://github.com/rafaelhenrique/flask_tutorial/tree/3.0
- See explanation about release: https://github.com/rafaelhenrique/flask_tutorial/releases/tag/3.0
- See video: https://www.youtube.com/watch?v=KGNFeMb39A0

## 4.0 - ORM, creation and query data! (and some Windows problems :-o)

- See release code: https://github.com/rafaelhenrique/flask_tutorial/tree/4.0
- See explanation about release: https://github.com/rafaelhenrique/flask_tutorial/releases/tag/4.0
- See video: https://www.youtube.com/watch?v=8h9CC2zexsI

## 5.0 - Configuration, structure and Hen and Egg problem!

- See release code: https://github.com/rafaelhenrique/flask_tutorial/tree/5.0
- See explanation about release: https://github.com/rafaelhenrique/flask_tutorial/releases/tag/5.0
- See video: https://www.youtube.com/watch?v=VsFtrqTFyEE

## 6.0 - Structure and Hen and Egg problem (solved now)!

- See release code: https://github.com/rafaelhenrique/flask_tutorial/tree/6.0
- See explanation about release: https://github.com/rafaelhenrique/flask_tutorial/releases/tag/6.0
- See video: https://www.youtube.com/watch?v=ZMGimM8pE78

## 7.0 - Deploy part 1!

- See release code: https://github.com/rafaelhenrique/flask_tutorial/tree/7.0
- See explanation about release: https://github.com/rafaelhenrique/flask_tutorial/releases/tag/7.0
- See video: https://www.youtube.com/watch?v=-XDWUBIccrw

## 8.0 - Deploy part 2!

- See release code: https://github.com/rafaelhenrique/flask_tutorial/tree/8.0
- See explanation about release: https://github.com/rafaelhenrique/flask_tutorial/releases/tag/8.0
- See video: https://www.youtube.com/watch?v=mjrJOQAoDWk

## 9.0 - Automating deployment with Ansible!

- See release code: https://github.com/rafaelhenrique/flask_tutorial/tree/9.0
- See explanation about release: https://github.com/rafaelhenrique/flask_tutorial/releases/tag/9.0
- See video: https://www.youtube.com/watch?v=8hZQGDSA1Yo

## 10.0 - Automating deployment with Ansible (part 2)!

- See release code: https://github.com/rafaelhenrique/flask_tutorial/tree/10.0
- See explanation about release: https://github.com/rafaelhenrique/flask_tutorial/releases/tag/10.0
- See video: https://www.youtube.com/watch?v=guKkJmTGVgc

## 11.0 - Migrate databases (part 1)!

- See release code: https://github.com/rafaelhenrique/flask_tutorial/tree/11.0
- See explanation about release: https://github.com/rafaelhenrique/flask_tutorial/releases/tag/11.0
- See video: https://www.youtube.com/watch?v=k1IagndK9F8

## 12.0 - Migrate databases (part 2)!

- See release code: https://github.com/rafaelhenrique/flask_tutorial/tree/12.0
- See explanation about release: https://github.com/rafaelhenrique/flask_tutorial/releases/tag/12.0
- See video: https://www.youtube.com/watch?v=t4dGoI4S4SE

## 13.0 - Working with forms!

- See release code: https://github.com/rafaelhenrique/flask_tutorial/tree/13.0
- See explanation about release: https://github.com/rafaelhenrique/flask_tutorial/releases/tag/13.0
- See videos:
	- https://www.youtube.com/watch?v=ffJ3ia8SZds
	- https://www.youtube.com/watch?v=5-fUl-_ODhg

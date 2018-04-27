# django-react-search-personinfo
Django REST framework / React 

This repository is about Search information based on web app. It uses Django as backend and React as frontend.

**Frontend**

the main packages includes: React, React-Dom,webpack,babel

**Backend**

the main packages includes: Django==2.0.4,psycopg2,djangorestframework
Database: Postgres

## Development
* Make sure you are at the first directory
* Install Python dependencies: `pipenv install`
* Install Javascript dependencies: `npm i`
* Make the bundle: `npm run dev`
* enter into virtalenv: `pipenv shell`
* Makemigration: `python ./project/manage.py makemigrations`
* Migrate: `python ./project/manage.py migrate`
* Run locally: `python ./project/manage.py runserver`
* Head over http://127.0.0.1:8000/

## How to Use

Django templates page:
* the index page: http://127.0.0.1:8000/
* add person info page: http://127.0.0.1:8000/add
* view person info page: http://127.0.0.1:8000/view
* update person info page: http://127.0.0.1:8000/<pk?>/update
* delete person info page: http://127.0.0.1:8000/<pk?>/delete
* search person info page: http://127.0.0.1:8000/search

React:
* search person info page: http://127.0.0.1:8000/react





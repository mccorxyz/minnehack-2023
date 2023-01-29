# minnehack-2023
Project for Minnehack 2023

## Useful commands

python -m pip install django

django-admin startproject meeting_planner

cd meeting_planner/

python manage.py startapp website

### Run the webserver
```python manage.py runserver```

## Migrations

python manage.py showmigrations

python manage.py migrate

**After creating/updating a new model**
python manage.py makemigrations

**See generated SQL**
python manage.py sqlmigrate meetings 0001

**SQL shell**
python manage.py dbshell

**Model fields**
https://docs.djangoproject.com/en/4.1/ref/models/fields/

### Migration workflow
1. Change model code
2. Generate migration script (check it!)
    - `python manage.py makemigrations`
3. Optional: show Migrations
    - `python manage.py showmigraitons`
4. Run Migrations
    - `python manage.py migrate`

### Useful Colors

https://coolors.co/386641-6a994e-a7c957-f2e8cf-bc4749
## Howtos

#### 1. Create Django Project

```
python -m venv .env  (in folder Scripts run script activate for use environment)
git clone ...yr link
pip install django
django-admin startproject ProjectShop
python manage.py startapp shop, authentification
python manage.py runserver
```

#### 2. Add .gitignore

```
when clone from github yr repository press the check mark to clone gitignore file 
```

#### 3. Add package manager (pipenv, poetry)

```sql
pip install pipenv
```

#### 4. Add .env file with private environments

```
create .env file with info about yr SECRET_KEY
in settings:
change SECRET_KEY (SECRET_KEY = os.getenv("SECRET_KEY"))
```
# Anten_Quotidien_Projet

Il s'agit d'un projet Django servant de blog avec comme nom Anten quotidien. Vous trouverez ci-dessous les détails de la configuration et de l'utilisation de mon projet.

## Structure du Projet

```
my_django_project/
├── my_django_project/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── app/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── media/
│   ├── migrations/
│   │   └── __init__.py
│   ├── static/
│   │   └── style.css
│   ├── templates/
│   │    └── articles/
│   │        ├── article_confirm_delete.html
│   │        ├── article_detail.html
│   │        ├── article_form.html
│   │        ├── article_list.html
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── manage.py
└── requirements.txt
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd my_django_project
   ```

2. **Creation d'un environment de virtuel:**
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Installation de package requis :**
   ```
   pip install -r requirements.txt
   ```

4. **Run migrations:**
   ```
   python manage.py migrate
   ```

5. **Start the development server:**
   ```
   python manage.py runserver
   ```

## Usage

- Partie Access de l'application 
=> `http://127.0.0.1:8000/`

- Partie admin de l'interface de notre Application blog 
=> `http://127.0.0.1:8000/admin/`

 
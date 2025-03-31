# Anten_Quotidien_Projet

Il s'agit d'un projet Django servant de blog avec comme nom Anten quotidien. Vous trouverez ci-dessous les détails de la configuration et de l'utilisation de mon projet.

Cours - Langages et Frameworks Backend 2 (php, java, python, js, c#) : Django Master 2 - Conception et développement d'applications web, full stack et gaming (MICDA) Épreuve d'examen, Session normale, Mars 2025 Projet : Création d'un Blog avec Django

Cheikh Diop 

INE : N00292420181



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

 

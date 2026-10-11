# Django Lab 1

A Django project with a `tenant` app, project-level templates, and app-level templates.

## Local setup (Windows PowerShell)

Use Python 3.14, which was used to verify this project.

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python lab1/manage.py migrate
python lab1/manage.py test tenant
python lab1/manage.py runserver
```

Open http://127.0.0.1:8000/ for the home page and
http://127.0.0.1:8000/tenants/ for the tenant directory.

## Project structure

```text
.gitignore
requirements.txt
lab1/
    manage.py
    lab1/
        settings.py
        urls.py
        asgi.py
        wsgi.py
    templates/
        base.html
        home.html
    tenant/
        urls.py
        views.py
        tests.py
        migrations/
        templates/
            tenant/
                index.html
```

The home view renders `lab1/templates/home.html`. The tenant directory view
renders `lab1/tenant/templates/tenant/index.html`. Both extend the project-level
`base.html`. Project URL routing includes `tenant.urls`.

The virtual environment, local database, bytecode, and environment files are
excluded from Git. These settings are for local development, not production.
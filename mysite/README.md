# Garage Deals (Django site)

## Setup
    python -m venv venv
    venv\Scripts\activate        (Windows)   |   source venv/bin/activate   (Mac/Linux)
    pip install django
    python manage.py runserver

Open http://127.0.0.1:8000/

## Structure
- config/                project settings and main urls.py
- pages/views.py         PRODUCTS list, home view, contact view
- pages/urls.py          maps URLs to views
- pages/forms.py         Contact Seller form
- pages/templates/       HTML (base.html is shared by all pages)
- pages/static/pages/    style.css and product images (img/)

## Tip
To add a product, add a new dictionary to PRODUCTS in pages/views.py
and put its image in pages/static/pages/img/.

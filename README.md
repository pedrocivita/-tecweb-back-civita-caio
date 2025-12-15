# TecWeb Backend - Movie Management API

[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-4.2-092E20?style=flat&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![Django REST Framework](https://img.shields.io/badge/DRF-3.14-ff1709?style=flat&logo=django&logoColor=white)](https://www.django-rest-framework.org/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-316192?style=flat&logo=postgresql&logoColor=white)](https://www.postgresql.org/)
[![Gunicorn](https://img.shields.io/badge/Gunicorn-20.1-499848?style=flat&logo=gunicorn&logoColor=white)](https://gunicorn.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A RESTful API backend developed for the Web Technologies (TecWeb) course at Insper - Computer Engineering. This project implements a movie management system with full CRUD operations, demonstrating modern web development practices and API design principles.

## Table of Contents

- [About the Project](#about-the-project)
- [Technologies](#technologies)
- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Deployment](#deployment)
- [Contact](#contact)

## About the Project

This backend application was developed as part of Project 2 for the Web Technologies course at Insper's Computer Engineering program. The project demonstrates proficiency in building scalable REST APIs using Django and Django REST Framework, implementing database management with PostgreSQL, and deploying cloud-based applications.

The API provides a simple yet robust movie management system that allows users to create, read, and delete movie entries through a well-structured RESTful interface.

## Technologies

This project leverages modern Python web development technologies:

- **[Python 3.9+](https://www.python.org/)** - Core programming language
- **[Django 4.2](https://www.djangoproject.com/)** - High-level web framework
- **[Django REST Framework 3.14](https://www.django-rest-framework.org/)** - Powerful toolkit for building Web APIs
- **[PostgreSQL](https://www.postgresql.org/)** - Production database
- **[Gunicorn 20.1](https://gunicorn.org/)** - WSGI HTTP Server for production
- **[WhiteNoise 6.4](http://whitenoise.evans.io/)** - Static file serving
- **[Django CORS Headers](https://github.com/adamchainz/django-cors-headers)** - Cross-Origin Resource Sharing support
- **[dj-database-url](https://github.com/jazzband/dj-database-url)** - Database configuration utility
- **[psycopg2-binary](https://www.psycopg.org/)** - PostgreSQL adapter

## Features

- RESTful API architecture following industry best practices
- Full CRUD operations for movie entities
- PostgreSQL database integration with Railway
- CORS support for frontend integration
- Production-ready deployment configuration with Gunicorn
- Static file serving with WhiteNoise
- Comprehensive error handling
- Duplicate entry prevention

## Project Structure

```
tecweb-backend/
├── movies/                 # Main application module
│   ├── models.py          # Movie data model
│   ├── views.py           # API view controllers
│   ├── serializer.py      # DRF serializers
│   ├── urls.py            # URL routing
│   └── admin.py           # Admin interface configuration
├── tecweb/                # Project configuration
│   ├── settings.py        # Django settings
│   ├── urls.py            # Root URL configuration
│   ├── wsgi.py            # WSGI configuration
│   └── asgi.py            # ASGI configuration
├── manage.py              # Django management script
├── requirements.txt       # Python dependencies
├── Procfile              # Deployment configuration
└── README.md             # Project documentation
```

## Installation

### Prerequisites

- Python 3.9 or higher
- pip (Python package manager)
- PostgreSQL (for production) or SQLite (for development)

### Setup

1. Clone the repository:
```bash
git clone https://github.com/pedrocivita/-tecweb-back-civita-caio.git
cd -tecweb-back-civita-caio
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Configure environment variables (optional for local development):
```bash
# Create a .env file with your database configuration
DATABASE_URL=your_database_url_here
SECRET_KEY=your_secret_key_here
DEBUG=True
```

5. Run migrations:
```bash
python manage.py migrate
```

6. Create a superuser (optional, for admin access):
```bash
python manage.py createsuperuser
```

7. Start the development server:
```bash
python manage.py runserver
```

The API will be available at `http://localhost:8000/`

## Usage

### Running the Development Server

```bash
python manage.py runserver
```

### Running Tests

```bash
python manage.py test
```

### Accessing the Admin Panel

Navigate to `http://localhost:8000/admin/` and log in with your superuser credentials to manage movies through the Django admin interface.

## API Endpoints

### Base URL
```
http://localhost:8000/
```

### Endpoints

#### Get All Movies / Create Movie
```http
GET /movies/
POST /movies/
```

**GET Response Example:**
```json
[
  {
    "id": 1,
    "title": "The Shawshank Redemption"
  },
  {
    "id": 2,
    "title": "The Godfather"
  }
]
```

**POST Request Body:**
```json
{
  "title": "Inception"
}
```

**POST Response:**
```json
[
  {
    "id": 1,
    "title": "The Shawshank Redemption"
  },
  {
    "id": 2,
    "title": "The Godfather"
  },
  {
    "id": 3,
    "title": "Inception"
  }
]
```

#### Get Specific Movie / Delete Movie
```http
GET /movie/<title>/
DELETE /movie/<title>/
```

**GET Response Example:**
```json
{
  "id": 1,
  "title": "The Shawshank Redemption"
}
```

**DELETE Response:**
```json
{
  "id": 1,
  "title": "The Shawshank Redemption"
}
```

### Error Handling

The API implements proper HTTP status codes and error messages:

- `200 OK` - Request successful
- `404 Not Found` - Movie not found
- `400 Bad Request` - Invalid request or duplicate entry

## Deployment

This application is configured for deployment on platforms like Railway, Heroku, or similar PaaS providers.

### Deployment Configuration

The project includes:
- `Procfile` for process configuration
- `requirements.txt` for dependency management
- Static file configuration with WhiteNoise
- Database configuration using `dj-database-url`

### Environment Variables

For production deployment, set the following environment variables:
- `DATABASE_URL` - PostgreSQL database URL
- `SECRET_KEY` - Django secret key
- `DEBUG` - Set to `False` in production
- `ALLOWED_HOSTS` - Your domain name(s)

## Contact

**Pedro Civita**

- Email: pedrovac@al.insper.edu.br
- LinkedIn: [linkedin.com/in/pedro-civita](https://www.linkedin.com/in/pedro-civita)
- GitHub: [@pedrocivita](https://github.com/pedrocivita)

---

**Institution:** Insper - Instituto de Ensino e Pesquisa

**Course:** Computer Engineering - Web Technologies (TecWeb)

**Academic Year:** 2023

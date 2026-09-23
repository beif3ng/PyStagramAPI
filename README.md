# PyStagramAPI

An Instagram-inspired REST API built with Django REST Framework. Users can publish image posts under categories, with JWT and social authentication, post archiving, and advanced filtering. Fully Dockerized with PostgreSQL and Nginx.

## Features

- JWT authentication via `djangorestframework-simplejwt` + `djoser`
- Social authentication (OAuth2) via `social-auth-app-django`
- Categorized publications with image uploads
- Post archiving (soft-delete pattern)
- Filtering on categories and publications via `django-filter`
- Swagger / OpenAPI documentation via `drf-yasg`
- Object-level permissions: only the creator can edit or delete their posts
- Dockerized stack with PostgreSQL, Gunicorn, and Nginx

## Tech Stack

| Layer | Technology |
|---|---|
| Web framework | Django 5.1 + DRF 3.15 |
| Auth | djoser + simplejwt + social-auth |
| Database | PostgreSQL (psycopg2) |
| Storage | Django media files |
| API docs | drf-yasg (Swagger) |
| Deployment | Docker Compose + Nginx + Gunicorn |

## Data Model

```
Category (name, icon image)
 └──< Publication (user FK, category FK, image, content, is_archived)
```

| Model | Key Fields |
|---|---|
| `Category` | `name`, `icon` (ImageField) |
| `Publication` | `user` (FK), `category` (FK), `image`, `content`, `is_archived`, `created`, `updated` |

## Project Structure

```
PyStagramAPI/
├── blog/
│   ├── models.py         # Category, Publication
│   ├── serializers.py    # ModelSerializers
│   ├── views.py          # ListCreate + RetrieveUpdateDestroy generics
│   ├── permissions.py    # IsCreatorOrReadOnly
│   └── filters.py        # CategoryFilter, PublicationFilter
├── categories/           # Category app
├── publications/         # Publication app
├── main/                 # Django settings, root URLs
├── static/               # Static files
├── docker/               # Dockerfiles, Nginx config, entrypoints
├── docker-compose.yml
├── .env.example
└── requirements.txt
```

## Getting Started

### Local Setup

```bash
git clone https://github.com/beif3ng/PyStagramAPI.git
cd PyStagramAPI
cp .env.example .env  # fill in your values
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

### Docker

```bash
cp .env.example .env
docker compose up --build
```

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| POST | `/auth/users/` | Register a new user |
| POST | `/auth/jwt/create/` | Obtain JWT token pair |
| POST | `/auth/jwt/refresh/` | Refresh access token |
| GET / POST | `/categories/` | List or create categories |
| GET / PUT / DELETE | `/categories/<id>/` | Manage a category |
| GET / POST | `/publications/` | List active publications or create one |
| GET / PUT / DELETE | `/publications/<id>/` | Manage a publication (owner only) |

Swagger UI is available at `/swagger/`.

## Environment Variables

| Variable | Description |
|---|---|
| `SECRET_KEY` | Django secret key |
| `DEBUG` | `1` for development |
| `ALLOWED_HOSTS` | Comma-separated allowed hosts |
| `DB_ENGINE` | Database backend |
| `DB_NAME` | PostgreSQL database name |
| `DB_USER` | PostgreSQL username |
| `DB_PASSWORD` | PostgreSQL password |
| `DB_HOST` | Database host |
| `DB_PORT` | Database port |

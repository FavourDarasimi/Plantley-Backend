# Plantle Backend

Django API for tomato disease detection using TensorFlow.

## Local Development

```bash
python -m venv venv
venv\Scripts\activate    # Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## Docker

```bash
docker compose up --build
```

## Environment Variables

| Variable | Description | Default |
|---|---|---|
| `DEBUG` | Django debug mode | `False` |
| `SECRET_KEY` | Django secret key | *(required in production)* |
| `ALLOWED_HOSTS` | Comma-separated allowed hosts | `localhost,127.0.0.1` |
| `CORS_ALLOWED_ORIGINS` | Comma-separated CORS origins | `http://localhost:3000` |
| `DB_ENGINE` | `sqlite` or `postgresql` | `sqlite` |
| `DB_NAME` | PostgreSQL database name | — |
| `DB_USER` | PostgreSQL user | — |
| `DB_PASSWORD` | PostgreSQL password | — |
| `DB_HOST` | PostgreSQL host | — |
| `DB_PORT` | PostgreSQL port | — |
| `HF_TOKEN` | Hugging Face token | — |
| `HF_REPO_ID` | Hugging Face model repo ID | — |

## API

`POST /api/detect/` — Upload an image to classify.

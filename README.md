# Predictor Service

A Django microservice that serves the Magic 8-Ball predictor.

## Features

- Magic 8-Ball page at /
- API endpoint at /api/predict/ for JSON predictions
- Health check endpoint at /health/
- Stateless service with no database requirements
- Consistent hash-based predictions

## Installation

1. Create and activate virtual environment:
   ```bash
   python -m venv venv
   venv\Scripts\activate  # Windows
   source venv/bin/activate  # Mac/Linux
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run development server:
   ```bash
   python manage.py runserver
   ```

4. Test endpoints:
   - Magic 8-Ball: http://localhost:8000/
   - API: http://localhost:8000/api/predict/
   - Health: http://localhost:8000/health/

## API Usage

POST to `/api/predict/` with JSON:
```json
{
  "question": "Will I be rich?"
}
```

Response:
```json
{
  "question": "Will I be rich?",
  "answer": "Yes definitely",
  "status": "ok"
}
```

## Environment Variables

- `SECRET_KEY`: Django secret key (default: 'dev-secret-key')
- `DEBUG`: Enable debug mode (default: 'False')
- `ALLOWED_HOSTS`: Comma-separated allowed hosts (default: 'localhost')

## Production Deployment

```bash
gunicorn predictor.wsgi:application --bind 0.0.0.0:8000
```

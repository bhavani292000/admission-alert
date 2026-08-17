# Admission Alert
Render-ready Flask public dashboard.

Build command: `pip install -r requirements.txt`
Start command: `gunicorn app:app --bind 0.0.0.0:$PORT --workers 2 --timeout 120`
Health check: `/healthz`

This is the public dashboard package. Live scraping/notifications should be connected as a separate worker/cron service.

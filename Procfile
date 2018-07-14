release: cd frontend && npm install && npm build && cd .. && python backend/manage.py collectstatic --noinput
web: cd backend && gunicorn pj.wsgi

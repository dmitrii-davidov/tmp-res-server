release: npm build && python backend/manage.py collectstatic --noinput
web: cd backend && gunicorn pj.wsgi

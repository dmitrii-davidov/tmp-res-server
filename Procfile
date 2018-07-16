release: npm run-script build && python backend/manage.py collectstatic --noinput
web: cd backend && gunicorn pj.wsgi

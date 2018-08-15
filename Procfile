release: cd backend && python manage.py migrate

web: npm run-script build && cd backend && python manage.py collectstatic --noinput && gunicorn pj.wsgi

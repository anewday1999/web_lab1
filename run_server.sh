python3 webgiasu/manage.py collectstatic
cd webgiasu
sudo gunicorn --bind 0.0.0.0:8000 webgiasu.wsgi &
DJANGO_SETTINGS_MODULE=webgiasu.settings_read_only gunicorn --bind 0.0.0.0:8001 webgiasu.wsgi &
DJANGO_SETTINGS_MODULE=webgiasu.settings_read_only gunicorn --bind 0.0.0.0:8002 webgiasu.wsgi &
while true ; do
	:
done
trap "kill $(jobs -p)" EXIT
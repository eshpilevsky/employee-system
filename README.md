# Employee management

## About
This is a employee management api on Django.

API specification:
- swagger-ui view at api/v1/
- JSON view at api/swagger.json
- YAML view at api/swagger.yaml
- ReDoc view at api/redoc/

## Usage
Create 3 files in main folder:
.env.dev 
```
DEBUG=1
SECRET_KEY=*YOUR_KEY*
DJANGO_ALLOWED_HOSTS=*
SQL_ENGINE=django.db.backends.postgresql
SQL_DATABASE=django_dev
SQL_USER=django
SQL_PASSWORD=django_pass
SQL_HOST=db
SQL_PORT=5432
DATABASE=postgres
AWS_ACCESS_KEY_ID=AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY=AWS_SECRET_ACCESS_KEY
AWS_STORAGE_BUCKET_NAME=AWS_STORAGE_BUCKET_NAME
GOOGLE_MAP_API_KEY=GOOGLE_MAP_API_KEY

```
Update the file permissions locally:
```
$ chmod +x entrypoint.staging.sh
$ chmod +x entrypoint.sh
```

and run docker:
---
### Development:
```
# Up
$ make build-dev

# Navigate to:
# - admin http://localhost:8000/admin/
# - api (swagger) http://localhost:8000/api/

# Logs
$ make logs-dev

# if you need to do something inside container
$ docker-compose exec <name of container, for example - web or frontend or db> <command, for example - python manage.py ... >
# example
$ docker-compose exec db psql --username=hello_django --dbname=hello_django_dev

# Down
$ make stop-dev
```
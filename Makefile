build-dev:
	make stop-dev
	docker-compose -f build/development/docker-compose.yml up -d --build
build-staging:
	make stop-staging
	docker-compose -f build/staging/docker-compose.staging.yml up -d --build
run-dev:
	docker-compose -f build/development/docker-compose.yml up -d --build
stop-dev:
	docker-compose -f build/development/docker-compose.yml down -v
run-staging:
	docker-compose -f build/staging/docker-compose.staging.yml up -d --build
stop-staging:
	docker-compose -f build/staging/docker-compose.staging.yml down -v
create-admin-dev:
	docker exec -ti development_web_1 python manage.py createsuperuser
logs-dev:
	docker-compose -f build/development/docker-compose.yml logs -f
logs-staging:
	docker-compose -f build/staging/docker-compose.staging.yml logs -f

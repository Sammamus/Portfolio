version=$(shell date +%s)

build:
	@echo "building..."
	@docker build --no-cache -t draffle/airflow-server:latest .
	@echo "build complete!"

test_run_scheduler:
	@echo "testing docker run of container: draffle/airflow-server:latest -/- SETTING: scheduler..."
	@docker run -p 8080:8080 --rm --name test_server --env SETTING=scheduler draffle/airflow-server:latest

test_run_webserver:
	@echo "testing docker run of container: draffle/airflow-server:latest -/- SETTING: webserver..."
	@docker run -p 8080:8080 --rm --name test_server --env SETTING=webserver draffle/airflow-server:latest

test_run:
	@echo "testing docker run of container: draffle/airflow-server:latest..."
	@docker run -p 8080:8080 --rm --name test_server draffle/airflow-server:latest


version_test:
	@echo $(version)
	@date +%s

build-airflow:
	docker buildx build --platform linux/arm64 -t nelo86/airflow-arm64 ./airflow

build-superset:
	docker buildx build --platform linux/arm64 -t nelo86/superset-arm64 ./superset

build-all: build-airflow build-superset

publish:git add .
	git commit -m "Actualiza código"
	git push origin main

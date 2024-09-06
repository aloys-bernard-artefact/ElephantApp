
default : hello

hello : 
	@echo "Hello, grand elephant!"

run_local_api : 
	@echo "Running local API"
	uvicorn api.main:app --host 0.0.0.0 --port $(PORT) --reload     

test_api : 
	@echo "Testing API"
	curl -X GET "http://localhost:8080/healthcheck" 

build_local_api : 
	@echo "Building local API"
	docker build -t local-api -f Dockerfile .

run_local_api_docker : build_local_api
	@echo "Running local API in Docker"
	docker run -e PORT=$(PORT) -p 8080:$(PORT) local-api

.PHONY : tests 
tests : 
	@echo "Running tests"
	pytest -v tests

.PHONY: prep
prep: 
	@rm -rf expressJS/node_modules


.PHONY: build
build: prep
	@docker build -t ecomapp:latest -t ecomapp:prod .


.PHONY: run
run: build
	@docker-compose up -d


.PHONY: dev_build
dev_build: prep
	@docker build -t ecomapp:dev -f dev_Dockerfile .


.PHONY: dev_run
dev_run: dev_build
	@docker-compose --file dev_docker-compose.yaml up -d

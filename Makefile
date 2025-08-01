# Makefile for Python Search API

.PHONY: help setup install test test-quick test-unit test-api test-integration coverage lint format clean dev start docker-build docker-run docker-stop

help: ## Show help information
	@echo "Available commands:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

setup: ## Set up development environment
	./scripts/setup.sh

install: ## Install dependencies
	uv sync
	uv add --group dev pytest pytest-asyncio pytest-mock pytest-cov coverage httpx flake8 black mypy

test: ## Run all tests
	./scripts/test.sh

test-quick: ## Run quick tests
	./scripts/quick_test.sh

test-api: ## Run API tests
	PYTHONPATH=src uv run --group dev pytest tests/test_api.py -v --cov-fail-under=90

test-integration: ## Run integration tests
	PYTHONPATH=src uv run --group dev pytest tests/test_integration.py -v --cov-fail-under=60

coverage: ## Run tests and generate coverage report
	PYTHONPATH=src uv run --group dev coverage run -m pytest tests/
	uv run --group dev coverage report -m
	uv run --group dev coverage html
	@echo "Coverage report: htmlcov/index.html"

lint: ## Run code linting
	uv run --group dev flake8 src/ tests/ --max-line-length=88 --ignore=E203,W503

format: ## Format code
	uv run --group dev black src/ tests/

type-check: ## Run type checking
	uv run --group dev mypy src/

clean: ## Clean generated files
	rm -rf htmlcov/
	rm -rf .coverage
	rm -rf .pytest_cache/
	rm -rf __pycache__/
	find . -type d -name "__pycache__" -delete
	find . -type f -name "*.pyc" -delete

dev: ## Start in development mode
	./scripts/dev.sh

start: ## Start in production mode
	./scripts/start.sh

# Docker commands
GIT_COMMIT_SHA := $(shell git rev-parse --short HEAD)
IMAGE_NAME := fafnerzhang/python-search-api:$(GIT_COMMIT_SHA)

docker-build: ## Build Docker image with git commit sha tag
	docker build -t $(IMAGE_NAME) .

docker-run: ## Run Docker container with auto-restart and health check
	@if [ ! -f .env ]; then \
		echo "❌ .env file not found! Creating from .env.example..."; \
		if [ -f .env.example ]; then \
			cp .env.example .env; \
			echo "✅ Created .env from .env.example. Please review and update values if needed."; \
		else \
			echo "❌ .env.example not found! Please create .env file manually."; \
			exit 1; \
		fi; \
	fi
	docker run -d \
	  --name python-search-api \
	  --restart=unless-stopped \
	  -p 9410:9410 \
	  --env-file .env \
	  --health-cmd="curl -f http://localhost:9410/health || exit 1" \
	  --health-interval=30s \
	  --health-timeout=5s \
	  --health-retries=3 \
	  $(IMAGE_NAME)

docker-stop: ## Stop and remove Docker container
	docker stop python-search-api || true
	docker rm python-search-api || true

test-docker-build: ## Build Docker image and test health endpoint
	@if [ ! -f .env ]; then \
		echo "❌ .env file not found! Creating from .env.example..."; \
		if [ -f .env.example ]; then \
			cp .env.example .env; \
			echo "✅ Created .env from .env.example. Please review and update values if needed."; \
		else \
			echo "❌ .env.example not found! Please create .env file manually."; \
			exit 1; \
		fi; \
	fi
	@echo "🐳 Building Docker image..."
	docker build -t $(IMAGE_NAME) .
	@echo "🚀 Starting test container..."
	docker run -d --name test-container -p 9410:9410 --env-file .env -e API_TOKEN=test-token $(IMAGE_NAME)
	@echo "⏳ Waiting for container to be ready..."
	sleep 15
	@echo "🔍 Testing health endpoint..."
	curl -f http://localhost:9410/health || (echo "❌ Health check failed" && docker logs test-container && docker stop test-container && docker rm test-container && exit 1)
	@echo "📋 Testing API docs endpoint..."
	curl -f http://localhost:9410/docs || (echo "❌ Docs endpoint failed" && docker logs test-container && docker stop test-container && docker rm test-container && exit 1)
	@echo "✅ Docker build and health tests passed!"
	@echo "🧹 Cleaning up test container..."
	docker stop test-container
	docker rm test-container

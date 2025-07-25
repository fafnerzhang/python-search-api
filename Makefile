# Makefile for Python Search API

.PHONY: help setup install test test-quick test-unit test-api test-integration coverage lint format clean dev start

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

test-unit: ## Run unit tests
	PYTHONPATH=src uv run --group dev pytest tests/test_models.py tests/test_services.py -v --cov-fail-under=85

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

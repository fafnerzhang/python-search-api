# Makefile for Python Search API

.PHONY: help setup install test test-quick test-unit test-api test-integration coverage lint format clean dev start

help: ## 顯示幫助信息
	@echo "Available commands:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

setup: ## 設置開發環境
	./scripts/setup.sh

install: ## 安裝依賴
	uv sync
	uv add --group dev pytest pytest-asyncio pytest-mock coverage httpx flake8 black mypy

test: ## 運行所有測試
	./scripts/test.sh

test-quick: ## 運行快速測試
	./scripts/quick_test.sh

test-unit: ## 運行單元測試
	PYTHONPATH=src uv run --group dev pytest tests/test_models.py tests/test_services.py -v

test-api: ## 運行API測試
	PYTHONPATH=src uv run --group dev pytest tests/test_api.py -v

test-integration: ## 運行整合測試
	PYTHONPATH=src uv run --group dev pytest tests/test_integration.py -v

coverage: ## 運行測試並生成覆蓋率報告
	PYTHONPATH=src uv run --group dev coverage run -m pytest tests/
	uv run --group dev coverage report -m
	uv run --group dev coverage html
	@echo "Coverage report: htmlcov/index.html"

lint: ## 運行代碼檢查
	uv run --group dev flake8 src/ tests/ --max-line-length=88 --ignore=E203,W503

format: ## 格式化代碼
	uv run --group dev black src/ tests/

type-check: ## 運行類型檢查
	uv run --group dev mypy src/

clean: ## 清理生成的文件
	rm -rf htmlcov/
	rm -rf .coverage
	rm -rf .pytest_cache/
	rm -rf __pycache__/
	find . -type d -name "__pycache__" -delete
	find . -type f -name "*.pyc" -delete

dev: ## 開發模式啟動
	./scripts/dev.sh

start: ## 生產模式啟動
	./scripts/start.sh

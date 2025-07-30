#!/bin/bash

# Python Search API - 完整測試腳本

set -e

echo "🧪 Starting Python Search API Tests..."

# 確保在正確的目錄
cd "$(dirname "$0")/.."

# 檢查是否安裝了uv
if ! command -v uv &> /dev/null; then
    echo "❌ uv not found. Please install uv first."
    exit 1
fi

echo "📦 Installing test dependencies..."
uv add --group dev pytest pytest-asyncio pytest-mock coverage httpx

echo "🔧 Running linting checks..."
echo "- Running flake8..."
uv run --group dev flake8 src/ tests/ --max-line-length=88 --ignore=E203,W503 || echo "⚠️  Linting warnings found"

echo "🧪 Running unit tests..."
PYTHONPATH=src uv run --group dev pytest tests/ -v --tb=short

echo "📊 Running tests with coverage..."
PYTHONPATH=src uv run --group dev coverage run -m pytest tests/
uv run --group dev coverage report -m
uv run --group dev coverage html

echo "🎯 Running specific test categories..."
echo "- Unit tests:"
PYTHONPATH=src uv run --group dev pytest tests/test_models.py tests/test_services.py -v --no-cov

echo "- API tests:"
PYTHONPATH=src uv run --group dev pytest tests/test_api.py -v

echo "- Integration tests:"
PYTHONPATH=src uv run --group dev pytest tests/test_integration.py -v

echo "✅ All tests completed!"
echo "📋 Coverage report generated in htmlcov/"
echo "🌐 Open htmlcov/index.html to view detailed coverage report"

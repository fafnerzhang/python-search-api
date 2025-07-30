#!/bin/bash

# Python Search API - 快速測試腳本

set -e

echo "⚡ Running quick tests..."

# 確保在正確的目錄
cd "$(dirname "$0")/.."

# 運行快速測試（核心功能）- 只測試models、services和core模塊
PYTHONPATH=src uv run --group dev pytest tests/test_models.py tests/test_services.py -v --tb=short --override-ini="addopts=-ra -q --strict-markers --strict-config --cov=src.models --cov=src.services --cov=src.core --cov-report=term-missing --cov-fail-under=90"

echo "✅ Quick tests completed!"

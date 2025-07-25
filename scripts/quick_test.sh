#!/bin/bash

# Python Search API - 快速測試腳本

set -e

echo "⚡ Running quick tests..."

# 確保在正確的目錄
cd "$(dirname "$0")/.."

# 運行快速測試（核心功能）
PYTHONPATH=src uv run --with pytest --with pytest-asyncio --with pytest-mock --with httpx \
    pytest tests/test_models.py tests/test_services.py -v --tb=short

echo "✅ Quick tests completed!"

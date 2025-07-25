#!/bin/bash

# Python Search API - 開發模式啟動腳本

set -e

echo "� Starting Python Search API in development mode..."

# 確保在正確的目錄
cd "$(dirname "$0")/.."

# 檢查是否安裝了uv
if ! command -v uv &> /dev/null; then
    echo "❌ uv not found. Please install uv first."
    exit 1
fi

echo "� Starting development server..."
uv run --with fastapi --with "uvicorn[standard]" --with ddgs --with python-dotenv python main.py

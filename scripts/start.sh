#!/bin/bash

# Python Search API - 生產模式啟動腳本

set -e

echo "🚀 Starting Python Search API in production mode..."

# 確保在正確的目錄
cd "$(dirname "$0")/.."

# 檢查是否安裝了uv
if ! command -v uv &> /dev/null; then
    echo "❌ uv not found. Please install uv first:"
    echo "curl -LsSf https://astral.sh/uv/install.sh | sh"
    exit 1
fi

# 檢查環境文件
if [ ! -f .env ]; then
    echo "📝 Creating .env file from .env.example..."
    cp .env.example .env
fi

# 啟動生產服務器
echo "🌟 Starting production server..."
uv run --with fastapi --with "uvicorn[standard]" --with ddgs --with python-dotenv python main.py

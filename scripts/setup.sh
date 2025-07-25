#!/bin/bash

# Python Search API - 環境設置腳本

set -e

echo "🔧 Setting up Python Search API development environment..."

# 確保在正確的目錄
cd "$(dirname "$0")/.."

# 檢查是否安裝了uv
if ! command -v uv &> /dev/null; then
    echo "❌ uv not found. Installing uv..."
    curl -LsSf https://astral.sh/uv/install.sh | sh
    source $HOME/.cargo/env
fi

echo "📦 Installing dependencies..."
uv sync

echo "🧪 Installing development dependencies..."
uv add --group dev pytest pytest-asyncio pytest-mock coverage httpx flake8 black mypy

# 創建環境文件
if [ ! -f .env ]; then
    echo "📝 Creating .env file from .env.example..."
    cp .env.example .env
    echo "⚠️  Please edit .env file to configure API_TOKEN if needed"
fi

# 設置腳本執行權限
echo "🔐 Setting script permissions..."
chmod +x scripts/*.sh

echo "✅ Setup complete!"
echo ""
echo "📋 Available commands:"
echo "  ./scripts/dev.sh        - Start development server"
echo "  ./scripts/start.sh      - Start production server"
echo "  ./scripts/test.sh       - Run full test suite"
echo "  ./scripts/quick_test.sh - Run quick tests"
echo ""
echo "🚀 Ready to start development!"

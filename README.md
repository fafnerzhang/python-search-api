# Python Search API

基於FastAPI的DuckDuckGo搜尋API服務，使用DDGS 9.4.3庫實現。

## 功能特色

- 🔍 **多種搜尋類型**: 網頁搜尋、圖片搜尋、新聞搜尋
- 🚀 **高效能**: 基於FastAPI和異步處理
- 🔒 **安全認證**: 支援Bearer Token認證
- 🌐 **CORS支援**: 跨域請求支援
- 📚 **完整文檔**: 自動生成的API文檔
- 🧪 **測試覆蓋**: 完整的pytest測試套件
- 🏗️ **模組化架構**: 清晰的代碼結構

## 專案結構

```
python-search-api/
├── src/                          # 主要原始碼
│   ├── api/                      # API路由
│   │   ├── __init__.py
│   │   └── search.py            # 搜尋相關端點
│   ├── core/                     # 核心配置
│   │   ├── __init__.py
│   │   ├── config.py            # 應用程式配置
│   │   └── logging.py           # 日誌配置
│   ├── models/                   # Pydantic模型
│   │   ├── __init__.py
│   │   ├── requests.py          # 請求模型
│   │   └── responses.py         # 回應模型
│   ├── services/                 # 業務邏輯服務
│   │   ├── __init__.py
│   │   ├── auth_service.py      # 認證服務
│   │   └── ddgs_service.py      # DDGS搜尋服務
│   ├── __init__.py
│   └── app.py                    # FastAPI應用程式
├── tests/                        # 測試代碼
│   ├── __init__.py
│   ├── conftest.py              # 測試配置
│   ├── test_api.py              # API測試
│   ├── test_models.py           # 模型測試
│   ├── test_services.py         # 服務測試
│   └── test_integration.py      # 整合測試
├── main.py                       # 舊版入口點
├── main_new.py                   # 新版入口點
├── requirements.txt              # Python依賴
├── pyproject.toml               # 專案配置
├── pytest.ini                   # Pytest配置
├── Makefile                      # Make命令
├── test.sh                       # 測試腳本
├── quick_test.sh                # 快速測試腳本
├── dev.sh                        # 開發啟動腳本
├── start.sh                      # 生產啟動腳本
├── .env.example                  # 環境變數範例
├── .gitignore                    # Git忽略文件
└── README.md                     # 專案說明
```

## 快速開始

### 1. 環境需求

- Python 3.9+
- UV包管理器

### 2. 安裝依賴

```bash
# 使用Make
make install

# 或手動安裝
uv sync
uv add --group dev pytest pytest-asyncio pytest-mock coverage httpx flake8 black mypy
```

### 3. 環境配置

```bash
cp .env.example .env
# 編輯.env文件設定API_TOKEN（可選）
```

### 4. 啟動服務

```bash
# 開發模式（新架構）
make dev-new

# 或手動啟動
PYTHONPATH=src uv run --with fastapi --with "uvicorn[standard]" --with ddgs --with python-dotenv uvicorn src.app:app --host 0.0.0.0 --port 8999 --reload

# 舊版本（向後兼容）
make dev
```

### 5. API文檔

服務啟動後，訪問以下URL查看API文檔：

- **Swagger UI**: http://localhost:8999/docs
- **ReDoc**: http://localhost:8999/redoc
- **OpenAPI Schema**: http://localhost:8999/openapi.json

## 測試

### 完整測試套件

```bash
# 運行所有測試
make test

# 或使用腳本
./test.sh
```

### 快速測試

```bash
# 運行快速測試
make test-quick

# 或使用腳本
./quick_test.sh
```

### 特定測試類型

```bash
# 單元測試
make test-unit

# API測試
make test-api

# 整合測試
make test-integration

# 覆蓋率報告
make coverage
```

### 代碼品質

```bash
# 代碼檢查
make lint

# 代碼格式化
make format

# 類型檢查
make type-check
```

## API端點

### 網頁搜尋

**POST** `/search`
```json
{
  "query": "FastAPI",
  "region": "us-en",
  "safesearch": "moderate",
  "max_results": 10
}
```

**GET** `/search?q=FastAPI&max_results=10`

### 圖片搜尋

**POST** `/search/images`
```json
{
  "query": "python logo",
  "size": "Large",
  "max_results": 5
}
```

### 新聞搜尋

**POST** `/search/news`
```json
{
  "query": "technology news",
  "time_limit": "d",
  "max_results": 5
}
```

## 認證

API支援可選的Bearer Token認證：

```bash
curl -H "Authorization: Bearer YOUR_TOKEN" \
     -X POST "http://localhost:8999/search" \
     -H "Content-Type: application/json" \
     -d '{"query": "test"}'
```

## 開發

### 專案架構說明

- **src/core/**: 核心配置和共用工具
- **src/models/**: Pydantic數據模型
- **src/services/**: 業務邏輯和外部服務整合
- **src/api/**: FastAPI路由和端點
- **tests/**: 完整的測試套件

### 添加新功能

1. 在適當的模組中添加功能
2. 編寫對應的測試
3. 更新API文檔
4. 運行測試確保功能正常

### 測試策略

- **單元測試**: 測試個別功能和模型
- **API測試**: 測試HTTP端點
- **整合測試**: 測試完整的工作流程
- **Mock測試**: 模擬外部依賴（DDGS）

## 環境變數

```bash
# 可選設定
API_TOKEN=your_secret_token    # API認證token
HOST=0.0.0.0                   # 服務器主機
PORT=8999                      # 服務器端口
DEBUG=true                     # 除錯模式
```

## 故障排除

### 常見問題

1. **DDGS連接錯誤**: 檢查網路連接
2. **依賴安裝失敗**: 確保Python版本>=3.9
3. **測試失敗**: 檢查是否安裝了測試依賴

### 日誌查看

```bash
# 檢查應用程式日誌
tail -f uvicorn.log

# 除錯模式啟動
DEBUG=true make dev-new
```

## 貢獻

1. Fork專案
2. 創建功能分支
3. 添加測試
4. 確保所有測試通過
5. 提交Pull Request

## 許可證

MIT License

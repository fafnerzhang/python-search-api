"""
核心配置模組
"""

import os
from typing import Optional
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


class Settings:
    """
    應用程式設定
    """

    # API設定
    API_TITLE: str = "DuckDuckGo Search API"
    API_DESCRIPTION: str = "FastAPI application with DuckDuckGo search using DDGS"
    API_VERSION: str = "1.0.0"

    # 服務器設定
    HOST: str = os.getenv("HOST", "0.0.0.0")
    PORT: int = int(os.getenv("PORT", "8999"))
    DEBUG: bool = os.getenv("DEBUG", "False").lower() == "true"

    # 認證設定
    API_TOKEN: Optional[str] = os.getenv("API_TOKEN")

    # CORS設定
    ALLOWED_ORIGINS: list = ["*"]  # 在生產環境中應該限制特定域名

    # 搜尋預設值
    DEFAULT_REGION: str = "wt-wt"
    DEFAULT_SAFESEARCH: str = "moderate"
    MAX_RESULTS_LIMIT: int = 100
    DEFAULT_MAX_RESULTS: int = 10


settings = Settings()

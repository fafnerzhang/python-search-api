"""
主要的FastAPI應用程式
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime
from typing import Dict, Any

from src.core.config import settings
from src.core.logging import logger
from src.api.search import router as search_router


def create_app() -> FastAPI:
    """
    創建並配置FastAPI應用程式

    Returns:
        配置好的FastAPI應用程式實例
    """
    app = FastAPI(
        title=settings.API_TITLE,
        description=settings.API_DESCRIPTION,
        version=settings.API_VERSION,
        docs_url="/docs",
        redoc_url="/redoc",
    )

    # CORS middleware
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.ALLOWED_ORIGINS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # 註冊路由
    app.include_router(search_router, tags=["search"])

    # 根路由
    @app.get("/", response_model=Dict[str, Any])
    async def root():
        """
        API根路由，返回API信息
        """
        return {
            "message": settings.API_TITLE,
            "version": settings.API_VERSION,
            "endpoints": {
                "search": "/search",
                "search_images": "/search/images",
                "search_news": "/search/news",
                "docs": "/docs",
            },
            "powered_by": "DDGS 9.4.3",
        }

    # 健康檢查端點
    @app.get("/health")
    async def health_check():
        """
        健康檢查端點
        """
        return {"status": "healthy", "timestamp": datetime.now().isoformat()}

    # 例外處理器
    @app.exception_handler(HTTPException)
    async def http_exception_handler(request, exc):
        from fastapi.responses import JSONResponse

        return JSONResponse(
            status_code=exc.status_code,
            content={
                "success": False,
                "error": "HTTP Exception",
                "message": exc.detail,
                "status_code": exc.status_code,
                "timestamp": datetime.now().isoformat(),
            },
        )

    @app.exception_handler(Exception)
    async def general_exception_handler(request, exc):
        from fastapi.responses import JSONResponse

        logger.error(f"Unhandled exception: {str(exc)}")
        return JSONResponse(
            status_code=500,
            content={
                "success": False,
                "error": "Internal Server Error",
                "message": "An unexpected error occurred",
                "timestamp": datetime.now().isoformat(),
            },
        )

    return app


# 創建應用程式實例
app = create_app()

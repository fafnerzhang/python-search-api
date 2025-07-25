"""
搜尋API路由
"""

from fastapi import APIRouter, Depends, Query, HTTPException
from datetime import datetime
from typing import Optional

from src.models.requests import SearchRequest, ImageSearchRequest, NewsSearchRequest
from src.models.responses import (
    SearchResponse,
    ImageSearchResponse,
    NewsSearchResponse,
    SearchResult,
    ImageResult,
    NewsResult,
)
from src.services.ddgs_service import DDGSService
from src.services.auth_service import verify_token
from src.core.logging import logger

router = APIRouter()


@router.post("/search", response_model=SearchResponse)
async def search_web(
    request: SearchRequest, token: Optional[str] = Depends(verify_token)
):
    """
    網頁搜尋端點 (POST)
    """
    try:
        results = await DDGSService.safe_ddgs_operation(
            DDGSService.text_search,
            request.query,
            request.region,
            request.safesearch,
            request.time_limit,
            request.max_results,
        )

        # 轉換結果格式
        search_results = [
            SearchResult(
                title=result.get("title", ""),
                href=result.get("href", ""),
                body=result.get("body", ""),
            )
            for result in results
        ]

        return SearchResponse(
            success=True,
            query=request.query,
            results=search_results,
            total_results=len(search_results),
            timestamp=datetime.now().isoformat(),
            region=request.region,
            safesearch=request.safesearch,
            time_limit=request.time_limit,
        )

    except Exception as e:
        logger.error(f"Search failed: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Search failed: {str(e)}")


@router.get("/search", response_model=SearchResponse)
async def search_web_get(
    q: str = Query(..., description="Search query"),
    region: str = Query("wt-wt", description="Region code"),
    safesearch: str = Query("moderate", description="Safe search level"),
    time_limit: Optional[str] = Query(None, description="Time limit"),
    max_results: int = Query(10, ge=1, le=100, description="Maximum results"),
    token: Optional[str] = Depends(verify_token),
):
    """
    網頁搜尋端點 (GET)
    """
    request = SearchRequest(
        query=q,
        region=region,
        safesearch=safesearch,
        time_limit=time_limit,
        max_results=max_results,
    )
    return await search_web(request, token)


@router.post("/search/images", response_model=ImageSearchResponse)
async def search_images(
    request: ImageSearchRequest, token: Optional[str] = Depends(verify_token)
):
    """
    圖片搜尋端點
    """
    try:
        results = await DDGSService.safe_ddgs_operation(
            DDGSService.image_search,
            request.query,
            request.region,
            request.safesearch,
            request.size,
            request.color,
            request.type_image,
            request.layout,
            request.license_image,
            request.max_results,
        )

        # 轉換結果格式
        image_results = [
            ImageResult(
                title=result.get("title", ""),
                image=result.get("image", ""),
                thumbnail=result.get("thumbnail", ""),
                url=result.get("url", ""),
                height=result.get("height", 0),
                width=result.get("width", 0),
                source=result.get("source", ""),
            )
            for result in results
        ]

        return ImageSearchResponse(
            success=True,
            query=request.query,
            results=image_results,
            total_results=len(image_results),
            timestamp=datetime.now().isoformat(),
            region=request.region,
        )

    except Exception as e:
        logger.error(f"Image search failed: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Image search failed: {str(e)}")


@router.post("/search/news", response_model=NewsSearchResponse)
async def search_news(
    request: NewsSearchRequest, token: Optional[str] = Depends(verify_token)
):
    """
    新聞搜尋端點
    """
    try:
        results = await DDGSService.safe_ddgs_operation(
            DDGSService.news_search,
            request.query,
            request.region,
            request.safesearch,
            request.time_limit,
            request.max_results,
        )

        # 轉換結果格式
        news_results = [
            NewsResult(
                date=result.get("date", ""),
                title=result.get("title", ""),
                body=result.get("body", ""),
                url=result.get("url", ""),
                image=result.get("image"),
                source=result.get("source", ""),
            )
            for result in results
        ]

        return NewsSearchResponse(
            success=True,
            query=request.query,
            results=news_results,
            total_results=len(news_results),
            timestamp=datetime.now().isoformat(),
            region=request.region,
        )

    except Exception as e:
        logger.error(f"News search failed: {str(e)}")
        raise HTTPException(status_code=500, detail=f"News search failed: {str(e)}")

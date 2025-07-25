"""
API回應模型
"""

from pydantic import BaseModel
from typing import List, Optional


class SearchResult(BaseModel):
    """單個搜尋結果"""

    title: str
    href: str
    body: str


class ImageResult(BaseModel):
    """單個圖片結果"""

    title: str
    image: str
    thumbnail: str
    url: str
    height: int
    width: int
    source: str


class NewsResult(BaseModel):
    """單個新聞結果"""

    date: str
    title: str
    body: str
    url: str
    image: Optional[str] = None
    source: str


class SearchResponse(BaseModel):
    """搜尋回應模型"""

    success: bool
    query: str
    results: List[SearchResult]
    total_results: int
    timestamp: str
    region: str
    safesearch: str
    time_limit: Optional[str] = None


class ImageSearchResponse(BaseModel):
    """圖片搜尋回應模型"""

    success: bool
    query: str
    results: List[ImageResult]
    total_results: int
    timestamp: str
    region: str


class NewsSearchResponse(BaseModel):
    """新聞搜尋回應模型"""

    success: bool
    query: str
    results: List[NewsResult]
    total_results: int
    timestamp: str
    region: str


class ErrorResponse(BaseModel):
    """錯誤回應模型"""

    success: bool = False
    error: str
    message: str
    timestamp: str

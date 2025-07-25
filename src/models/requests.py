"""
API請求模型
"""

from pydantic import BaseModel, Field
from typing import Optional


class SearchRequest(BaseModel):
    """網頁搜尋請求模型"""

    query: str = Field(..., description="Search query", min_length=1, max_length=500)
    region: Optional[str] = Field(
        "wt-wt", description="Region code (e.g., 'us-en', 'tw-zh')"
    )
    safesearch: Optional[str] = Field(
        "moderate", description="Safe search level: 'strict', 'moderate', 'off'"
    )
    time_limit: Optional[str] = Field(
        None, description="Time limit: 'd' (day), 'w' (week), 'm' (month), 'y' (year)"
    )
    max_results: Optional[int] = Field(
        10, description="Maximum number of results", ge=1, le=100
    )


class ImageSearchRequest(BaseModel):
    """圖片搜尋請求模型"""

    query: str = Field(
        ..., description="Image search query", min_length=1, max_length=500
    )
    region: Optional[str] = Field("wt-wt", description="Region code")
    safesearch: Optional[str] = Field("moderate", description="Safe search level")
    size: Optional[str] = Field(
        None, description="Image size: 'Small', 'Medium', 'Large', 'Wallpaper'"
    )
    color: Optional[str] = Field(
        None,
        description="Image color: 'color', 'Monochrome', 'Red', 'Orange', etc.",
    )
    type_image: Optional[str] = Field(
        None, description="Image type: 'photo', 'clipart', 'gif', 'transparent', 'line'"
    )
    layout: Optional[str] = Field(
        None, description="Image layout: 'Square', 'Tall', 'Wide'"
    )
    license_image: Optional[str] = Field(
        None,
        description="License: 'any', 'Public', 'Share', 'ShareCommercially', 'Modify'",
    )
    max_results: Optional[int] = Field(
        10, description="Maximum number of results", ge=1, le=100
    )


class NewsSearchRequest(BaseModel):
    """新聞搜尋請求模型"""

    query: str = Field(
        ..., description="News search query", min_length=1, max_length=500
    )
    region: Optional[str] = Field("wt-wt", description="Region code")
    safesearch: Optional[str] = Field("moderate", description="Safe search level")
    time_limit: Optional[str] = Field(None, description="Time limit for news")
    max_results: Optional[int] = Field(
        10, description="Maximum number of results", ge=1, le=100
    )

"""
模型測試
"""

import os
import sys

import pytest
from pydantic import ValidationError

# 添加src目錄到Python路徑
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from src.models.requests import SearchRequest, ImageSearchRequest, NewsSearchRequest
from src.models.responses import SearchResponse, SearchResult


class TestRequestModels:
    """測試請求模型"""

    def test_search_request_valid(self):
        """測試有效的搜尋請求"""
        request = SearchRequest(
            query="test query", region="us-en", safesearch="moderate", max_results=10
        )
        assert request.query == "test query"
        assert request.region == "us-en"
        assert request.safesearch == "moderate"
        assert request.max_results == 10

    def test_search_request_defaults(self):
        """測試搜尋請求預設值"""
        request = SearchRequest(query="test")
        assert request.query == "test"
        assert request.region == "wt-wt"
        assert request.safesearch == "moderate"
        assert request.time_limit is None
        assert request.max_results == 10

    def test_search_request_empty_query(self):
        """測試空查詢字串"""
        with pytest.raises(ValidationError) as exc_info:
            SearchRequest(query="")

        errors = exc_info.value.errors()
        assert any(error["type"] == "string_too_short" for error in errors)

    def test_search_request_long_query(self):
        """測試過長查詢字串"""
        long_query = "a" * 501  # Exceeds 500 character limit
        with pytest.raises(ValidationError) as exc_info:
            SearchRequest(query=long_query)

        errors = exc_info.value.errors()
        assert any(error["type"] == "string_too_long" for error in errors)

    def test_search_request_invalid_max_results(self):
        """測試無效的最大結果數"""
        # Test max_results too low
        with pytest.raises(ValidationError):
            SearchRequest(query="test", max_results=0)

        # Test max_results too high
        with pytest.raises(ValidationError):
            SearchRequest(query="test", max_results=101)

    def test_image_search_request_valid(self):
        """測試有效的圖片搜尋請求"""
        request = ImageSearchRequest(
            query="test image",
            size="Large",
            color="Red",
            type_image="photo",
            max_results=5,
        )
        assert request.query == "test image"
        assert request.size == "Large"
        assert request.color == "Red"
        assert request.type_image == "photo"
        assert request.max_results == 5

    def test_news_search_request_valid(self):
        """測試有效的新聞搜尋請求"""
        request = NewsSearchRequest(
            query="breaking news", time_limit="d", max_results=3
        )
        assert request.query == "breaking news"
        assert request.time_limit == "d"
        assert request.max_results == 3


class TestResponseModels:
    """測試回應模型"""

    def test_search_result_valid(self):
        """測試有效的搜尋結果"""
        result = SearchResult(
            title="Test Title", href="https://example.com", body="Test content"
        )
        assert result.title == "Test Title"
        assert result.href == "https://example.com"
        assert result.body == "Test content"

    def test_search_response_valid(self):
        """測試有效的搜尋回應"""
        results = [
            SearchResult(
                title="Test Title", href="https://example.com", body="Test content"
            )
        ]

        response = SearchResponse(
            success=True,
            query="test query",
            results=results,
            total_results=1,
            timestamp="2024-01-01T12:00:00",
            region="us-en",
            safesearch="moderate",
        )

        assert response.success is True
        assert response.query == "test query"
        assert len(response.results) == 1
        assert response.total_results == 1
        assert response.region == "us-en"
        assert response.safesearch == "moderate"

    def test_search_response_empty_results(self):
        """測試空結果的搜尋回應"""
        response = SearchResponse(
            success=True,
            query="test query",
            results=[],
            total_results=0,
            timestamp="2024-01-01T12:00:00",
            region="us-en",
            safesearch="moderate",
        )

        assert response.success is True
        assert len(response.results) == 0
        assert response.total_results == 0

"""
服務層測試
"""

import os
import sys
from unittest.mock import MagicMock, patch

import pytest
from fastapi import HTTPException
from fastapi.security import HTTPAuthorizationCredentials

# 添加src目錄到Python路徑
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from src.services.ddgs_service import DDGSService
from src.services.auth_service import verify_token


class TestDDGSService:
    """測試DDGS服務"""

    @patch("src.services.ddgs_service.DDGS")
    @pytest.mark.asyncio
    async def test_text_search_success(self, mock_ddgs):
        """測試文字搜尋成功"""
        # Mock DDGS response
        mock_results = [
            {
                "title": "Test Title",
                "href": "https://example.com",
                "body": "Test body content",
            }
        ]

        mock_ddgs_instance = MagicMock()
        mock_ddgs_instance.text.return_value = mock_results
        mock_ddgs.return_value.__enter__.return_value = mock_ddgs_instance

        results = await DDGSService.safe_ddgs_operation(
            DDGSService.text_search, "test query", "us-en", "moderate", None, 5
        )

        assert len(results) == 1
        assert results[0]["title"] == "Test Title"
        mock_ddgs_instance.text.assert_called_once()

    @patch("src.services.ddgs_service.DDGS")
    @pytest.mark.asyncio
    async def test_image_search_success(self, mock_ddgs):
        """測試圖片搜尋成功"""
        # Mock DDGS image response
        mock_results = [
            {
                "title": "Test Image",
                "image": "https://example.com/image.jpg",
                "thumbnail": "https://example.com/thumb.jpg",
                "url": "https://example.com",
                "height": 300,
                "width": 400,
                "source": "example.com",
            }
        ]

        mock_ddgs_instance = MagicMock()
        mock_ddgs_instance.images.return_value = mock_results
        mock_ddgs.return_value.__enter__.return_value = mock_ddgs_instance

        results = await DDGSService.safe_ddgs_operation(
            DDGSService.image_search,
            "test image",
            "us-en",
            "moderate",
            None,
            None,
            None,
            None,
            None,
            3,
        )

        assert len(results) == 1
        assert results[0]["title"] == "Test Image"
        mock_ddgs_instance.images.assert_called_once()

    @patch("src.services.ddgs_service.DDGS")
    @pytest.mark.asyncio
    async def test_news_search_success(self, mock_ddgs):
        """測試新聞搜尋成功"""
        # Mock DDGS news response
        mock_results = [
            {
                "date": "2024-01-01",
                "title": "Test News",
                "body": "Test news content",
                "url": "https://example.com/news",
                "source": "example.com",
            }
        ]

        mock_ddgs_instance = MagicMock()
        mock_ddgs_instance.news.return_value = mock_results
        mock_ddgs.return_value.__enter__.return_value = mock_ddgs_instance

        results = await DDGSService.safe_ddgs_operation(
            DDGSService.news_search, "test news", "us-en", "moderate", None, 3
        )

        assert len(results) == 1
        assert results[0]["title"] == "Test News"
        mock_ddgs_instance.news.assert_called_once()

    @patch("src.services.ddgs_service.DDGS")
    @pytest.mark.asyncio
    async def test_ddgs_exception_handling(self, mock_ddgs):
        """測試DDGS異常處理"""
        # Mock DDGS to raise exception
        mock_ddgs.side_effect = Exception("DDGS connection error")

        with pytest.raises(Exception) as exc_info:
            await DDGSService.safe_ddgs_operation(DDGSService.text_search, "test query")

        assert "Search operation failed" in str(exc_info.value)

    def test_text_search_parameters(self):
        """測試文字搜尋參數"""
        with patch("src.services.ddgs_service.DDGS") as mock_ddgs:
            mock_ddgs_instance = MagicMock()
            mock_ddgs_instance.text.return_value = []
            mock_ddgs.return_value.__enter__.return_value = mock_ddgs_instance

            DDGSService.text_search(
                "test query",
                region="tw-zh",
                safesearch="strict",
                timelimit="w",
                max_results=20,
            )

            # 驗證調用參數
            mock_ddgs_instance.text.assert_called_once_with(
                "test query",
                region="tw-zh",
                safesearch="strict",
                timelimit="w",
                max_results=20,
            )

    def test_image_search_parameters(self):
        """測試圖片搜尋參數"""
        with patch("src.services.ddgs_service.DDGS") as mock_ddgs:
            mock_ddgs_instance = MagicMock()
            mock_ddgs_instance.images.return_value = []
            mock_ddgs.return_value.__enter__.return_value = mock_ddgs_instance

            DDGSService.image_search(
                "test image",
                region="us-en",
                safesearch="moderate",
                size="Large",
                type_image="photo",
                layout="Square",
                color="Red",
                license_image="Public",
                max_results=10,
            )

            # 驗證調用參數
            mock_ddgs_instance.images.assert_called_once_with(
                "test image",
                region="us-en",
                safesearch="moderate",
                size="Large",
                type_image="photo",
                layout="Square",
                color="Red",
                license_image="Public",
                max_results=10,
            )

    def test_news_search_parameters(self):
        """測試新聞搜尋參數"""
        with patch("src.services.ddgs_service.DDGS") as mock_ddgs:
            mock_ddgs_instance = MagicMock()
            mock_ddgs_instance.news.return_value = []
            mock_ddgs.return_value.__enter__.return_value = mock_ddgs_instance

            DDGSService.news_search(
                "test news",
                region="uk-en",
                safesearch="strict",
                timelimit="m",
                max_results=15,
            )

            # 驗證調用參數
            mock_ddgs_instance.news.assert_called_once_with(
                "test news",
                region="uk-en",
                safesearch="strict",
                timelimit="m",
                max_results=15,
            )

    @patch("src.services.ddgs_service.DDGS")
    @pytest.mark.asyncio
    async def test_safe_ddgs_operation_with_timeout(self, mock_ddgs):
        """測試DDGS操作超時處理"""
        import asyncio

        # Mock DDGS to raise timeout
        mock_ddgs.side_effect = asyncio.TimeoutError("Operation timed out")

        with pytest.raises(Exception) as exc_info:
            await DDGSService.safe_ddgs_operation(
                DDGSService.text_search, "test query", timeout=0.1
            )

        assert "Search operation failed" in str(exc_info.value)

    @patch("src.services.ddgs_service.DDGS")
    @pytest.mark.asyncio
    async def test_safe_ddgs_operation_with_connection_error(self, mock_ddgs):
        """測試DDGS連接錯誤處理"""
        import requests

        # Mock DDGS to raise connection error
        mock_ddgs.side_effect = requests.ConnectionError("Connection failed")

        with pytest.raises(Exception) as exc_info:
            await DDGSService.safe_ddgs_operation(DDGSService.text_search, "test query")

        assert "Search operation failed" in str(exc_info.value)

    @patch("src.services.ddgs_service.logger")
    @patch("src.services.ddgs_service.DDGS")
    @pytest.mark.asyncio
    async def test_safe_ddgs_operation_logs_error(self, mock_ddgs, mock_logger):
        """測試DDGS操作錯誤日誌記錄"""
        # Mock DDGS to raise exception
        mock_ddgs.side_effect = Exception("Test error")

        with pytest.raises(Exception):
            await DDGSService.safe_ddgs_operation(DDGSService.text_search, "test query")

        # 驗證錯誤日誌被記錄
        assert mock_logger.error.call_count >= 1

    def test_text_search_with_minimal_parameters(self):
        """測試最少參數的文字搜尋"""
        with patch("src.services.ddgs_service.DDGS") as mock_ddgs:
            mock_ddgs_instance = MagicMock()
            mock_ddgs_instance.text.return_value = []
            mock_ddgs.return_value.__enter__.return_value = mock_ddgs_instance

            DDGSService.text_search("minimal query")

        # 驗證調用參數
        mock_ddgs_instance.text.assert_called_once_with(
            "minimal query",
            region="wt-wt",
            safesearch="moderate",
            timelimit=None,
            max_results=10,
        )

    def test_image_search_with_minimal_parameters(self):
        """測試最少參數的圖片搜尋"""
        with patch("src.services.ddgs_service.DDGS") as mock_ddgs:
            mock_ddgs_instance = MagicMock()
            mock_ddgs_instance.images.return_value = []
            mock_ddgs.return_value.__enter__.return_value = mock_ddgs_instance

            DDGSService.image_search("minimal image")

        # 驗證調用參數
        mock_ddgs_instance.images.assert_called_once_with(
            "minimal image",
            region="wt-wt",
            safesearch="moderate",
            size=None,
            type_image=None,
            layout=None,
            color=None,
            license_image=None,
            max_results=10,
        )

    def test_news_search_with_minimal_parameters(self):
        """測試最少參數的新聞搜尋"""
        with patch("src.services.ddgs_service.DDGS") as mock_ddgs:
            mock_ddgs_instance = MagicMock()
            mock_ddgs_instance.news.return_value = []
            mock_ddgs.return_value.__enter__.return_value = mock_ddgs_instance

            DDGSService.news_search("minimal news")

        # 驗證調用參數
        mock_ddgs_instance.news.assert_called_once_with(
            "minimal news",
            region="wt-wt",
            safesearch="moderate",
            timelimit=None,
            max_results=10,
        )


class TestAuthService:
    """測試認證服務"""

    @patch("src.services.auth_service.settings.API_TOKEN", None)
    def test_verify_token_no_api_token_configured(self):
        """測試未配置API_TOKEN時的錯誤"""
        credentials = HTTPAuthorizationCredentials(
            scheme="Bearer", credentials="test-token"
        )

        with pytest.raises(HTTPException) as exc_info:
            verify_token(credentials)

        assert exc_info.value.status_code == 500
        assert "API_TOKEN not configured" in exc_info.value.detail

    @patch("src.services.auth_service.settings.API_TOKEN", "valid-token")
    def test_verify_token_invalid_token(self):
        """測試無效token時的錯誤"""
        credentials = HTTPAuthorizationCredentials(
            scheme="Bearer", credentials="invalid-token"
        )

        with pytest.raises(HTTPException) as exc_info:
            verify_token(credentials)

        assert exc_info.value.status_code == 401
        assert "Invalid authentication token" in exc_info.value.detail

    @patch("src.services.auth_service.settings.API_TOKEN", "valid-token")
    def test_verify_token_valid_token(self):
        """測試有效token時的成功"""
        credentials = HTTPAuthorizationCredentials(
            scheme="Bearer", credentials="valid-token"
        )

        result = verify_token(credentials)
        assert result == "valid-token"

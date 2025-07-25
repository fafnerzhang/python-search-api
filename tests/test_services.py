"""
服務層測試
"""

import os
import sys
from unittest.mock import MagicMock, patch

import pytest

# 添加src目錄到Python路徑
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from src.services.ddgs_service import DDGSService


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

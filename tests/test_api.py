"""
API端點測試
"""

from fastapi.testclient import TestClient
from unittest.mock import patch, MagicMock


class TestRootEndpoints:
    """測試基本端點"""

    def test_root_endpoint(self, client: TestClient, auth_headers):
        """測試根端點"""
        response = client.get("/", headers=auth_headers)
        assert response.status_code == 200
        data = response.json()
        assert data["message"] == "DuckDuckGo Search API"
        assert "endpoints" in data
        assert "version" in data

    def test_health_endpoint(self, client: TestClient, auth_headers):
        """測試健康檢查端點"""
        response = client.get("/health", headers=auth_headers)
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "healthy"
        assert "timestamp" in data


class TestSearchEndpoints:
    """測試搜尋端點"""

    @patch("src.services.ddgs_service.DDGS")
    def test_search_post_success(
        self, mock_ddgs, client: TestClient, sample_search_data, auth_headers
    ):
        """測試POST搜尋成功"""
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

        response = client.post("/search", json=sample_search_data, headers=auth_headers)
        assert response.status_code == 200

        data = response.json()
        assert data["success"] is True
        assert data["query"] == sample_search_data["query"]
        assert len(data["results"]) == 1
        assert data["results"][0]["title"] == "Test Title"

    def test_search_validation_error(self, client: TestClient, auth_headers):
        """測試搜尋驗證錯誤"""
        # Empty query should fail validation
        response = client.post("/search", json={"query": ""}, headers=auth_headers)
        assert response.status_code == 422

    def test_search_invalid_max_results(self, client: TestClient, auth_headers):
        """測試無效的最大結果數"""
        response = client.post(
            "/search",
            json={"query": "test", "max_results": 200},  # Exceeds limit
            headers=auth_headers,
        )
        assert response.status_code == 422

    @patch("src.services.ddgs_service.DDGS")
    def test_search_ddgs_exception(
        self, mock_ddgs, client: TestClient, sample_search_data, auth_headers
    ):
        """測試DDGS異常處理"""
        # Mock DDGS to raise exception
        mock_ddgs.side_effect = Exception("DDGS error")

        response = client.post("/search", json=sample_search_data, headers=auth_headers)
        assert response.status_code == 500

        data = response.json()
        assert data["success"] is False
        assert "error" in data


class TestImageSearchEndpoints:
    """測試圖片搜尋端點"""

    @patch("src.services.ddgs_service.DDGS")
    def test_image_search_success(
        self, mock_ddgs, client: TestClient, sample_image_search_data, auth_headers
    ):
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

        response = client.post(
            "/search/images", json=sample_image_search_data, headers=auth_headers
        )
        assert response.status_code == 200

        data = response.json()
        assert data["success"] is True
        assert data["query"] == sample_image_search_data["query"]
        assert len(data["results"]) == 1
        assert data["results"][0]["title"] == "Test Image"


class TestNewsSearchEndpoints:
    """測試新聞搜尋端點"""

    @patch("src.services.ddgs_service.DDGS")
    def test_news_search_success(
        self, mock_ddgs, client: TestClient, sample_news_search_data, auth_headers
    ):
        """測試新聞搜尋成功"""
        # Mock DDGS news response
        mock_results = [
            {
                "date": "2024-01-01",
                "title": "Test News",
                "body": "Test news content",
                "url": "https://example.com/news",
                "image": "https://example.com/news.jpg",
                "source": "example.com",
            }
        ]

        mock_ddgs_instance = MagicMock()
        mock_ddgs_instance.news.return_value = mock_results
        mock_ddgs.return_value.__enter__.return_value = mock_ddgs_instance

        response = client.post(
            "/search/news", json=sample_news_search_data, headers=auth_headers
        )
        assert response.status_code == 200

        data = response.json()
        assert data["success"] is True
        assert data["query"] == sample_news_search_data["query"]
        assert len(data["results"]) == 1
        assert data["results"][0]["title"] == "Test News"


class TestAuthentication:
    """測試認證功能"""

    def test_no_auth_header_fails(self, auth_client: TestClient):
        """測試沒有認證標頭時失敗"""
        response = auth_client.post("/search", json={"query": "test"})
        assert response.status_code == 403

    def test_invalid_auth_token_fails(self, auth_client: TestClient):
        """測試無效認證標記時失敗"""
        headers = {"Authorization": "Bearer invalid-token"}
        response = auth_client.post("/search", json={"query": "test"}, headers=headers)
        assert response.status_code == 401

    def test_search_requires_auth(self, auth_client: TestClient, sample_search_data):
        """測試搜尋端點需要認證"""
        response = auth_client.post("/search", json=sample_search_data)
        assert response.status_code == 403

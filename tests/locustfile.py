"""
Locust performance testing configuration for Python Search API.
This file is used by the performance testing workflow.
"""

from locust import HttpUser, task, between
import json


class SearchAPIUser(HttpUser):
    wait_time = between(1, 3)

    def on_start(self):
        """Setup method called before any task is executed."""
        # Check if the API is healthy before starting tests
        response = self.client.get("/health")
        if response.status_code != 200:
            print(f"API health check failed: {response.status_code}")

    @task(3)
    def test_health_endpoint(self):
        """Test the health endpoint (highest weight)."""
        self.client.get("/health")

    @task(2)
    def test_web_search_get(self):
        """Test web search using GET method."""
        self.client.get("/search?q=FastAPI&max_results=5")

    @task(2)
    def test_web_search_post(self):
        """Test web search using POST method."""
        search_data = {
            "query": "Python programming",
            "region": "us-en",
            "safesearch": "moderate",
            "max_results": 5
        }
        self.client.post(
            "/search",
            data=json.dumps(search_data),
            headers={"Content-Type": "application/json"}
        )

    @task(1)
    def test_image_search(self):
        """Test image search endpoint."""
        search_data = {
            "query": "python logo",
            "size": "Medium",
            "max_results": 3
        }
        self.client.post(
            "/search/images",
            data=json.dumps(search_data),
            headers={"Content-Type": "application/json"}
        )

    @task(1)
    def test_news_search(self):
        """Test news search endpoint."""
        search_data = {
            "query": "technology news",
            "time_limit": "d",
            "max_results": 3
        }
        self.client.post(
            "/search/news",
            data=json.dumps(search_data),
            headers={"Content-Type": "application/json"}
        )

    @task(1)
    def test_api_docs(self):
        """Test API documentation endpoints."""
        self.client.get("/docs")
        self.client.get("/openapi.json")

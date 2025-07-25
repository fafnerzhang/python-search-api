"""
測試配置
"""

import asyncio
import os
import sys
from typing import Generator

import pytest
from fastapi.testclient import TestClient

# 添加src目錄到Python路徑
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from src.app import create_app


@pytest.fixture(scope="session")
def event_loop() -> Generator:
    """Create an instance of the default event loop for the test session."""
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture
def app():
    """Create a test FastAPI application."""
    return create_app()


@pytest.fixture
def client(app):
    """Create a test client."""
    return TestClient(app)


@pytest.fixture
def sample_search_data():
    """Sample search request data for testing."""
    return {
        "query": "FastAPI testing",
        "region": "us-en",
        "safesearch": "moderate",
        "max_results": 5,
    }


@pytest.fixture
def sample_image_search_data():
    """Sample image search request data for testing."""
    return {
        "query": "python logo",
        "region": "us-en",
        "safesearch": "moderate",
        "max_results": 3,
    }


@pytest.fixture
def sample_news_search_data():
    """Sample news search request data for testing."""
    return {
        "query": "technology news",
        "region": "us-en",
        "safesearch": "moderate",
        "max_results": 3,
    }

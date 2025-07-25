# Python Search API 🔍

[![Tests](https://github.com/fafnerzhang/python-search-api/workflows/Tests/badge.svg)](https://github.com/fafnerzhang/python-search-api/actions/workflows/tests.yml)
[![Code Quality](https://github.com/fafnerzhang/python-search-api/workflows/Code%20Quality/badge.svg)](https://github.com/fafnerzhang/python-search-api/actions/workflows/code-quality.yml)
[![CI/CD](https://github.com/fafnerzhang/python-search-api/workflows/CI%2FCD/badge.svg)](https://github.com/fafnerzhang/python-search-api/actions/workflows/ci-cd.yml)
[![Performance Tests](https://github.com/fafnerzhang/python-search-api/workflows/Performance%20Tests/badge.svg)](https://github.com/fafnerzhang/python-search-api/actions/workflows/performance.yml)
[![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115%2B-green.svg)](https://fastapi.tiangolo.com)
[![uv](https://img.shields.io/badge/uv-managed-orange.svg)](https://github.com/astral-sh/uv)
[![codecov](https://codecov.io/gh/fafnerzhang/python-search-api/branch/main/graph/badge.svg)](https://codecov.io/gh/fafnerzhang/python-search-api)
[![Docker](https://img.shields.io/badge/Docker-Available-2496ED.svg)](https://github.com/fafnerzhang/python-search-api/packages)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A high-performance FastAPI-based search service using DuckDuckGo Search (DDGS) with authentication support.

## ✨ Features

- 🔍 **Multiple Search Types**: Web search, image search, news search
- 🚀 **High Performance**: Built with FastAPI and async/await
- � **Secure Authentication**: Optional Bearer Token authentication
- 🌐 **CORS Support**: Cross-origin request support
- 📚 **Complete Documentation**: Auto-generated API documentation
- 🧪 **Test Coverage**: Comprehensive pytest test suite (91% coverage)
- 🏗️ **Modular Architecture**: Clean and maintainable code structure

## 📁 Project Structure

```
python-search-api/
├── src/                          # Main source code
│   ├── api/                      # API routes
│   │   ├── __init__.py
│   │   └── search.py            # Search endpoints
│   ├── core/                     # Core configuration
│   │   ├── __init__.py
│   │   ├── config.py            # Application configuration
│   │   └── logging.py           # Logging configuration
│   ├── models/                   # Pydantic models
│   │   ├── __init__.py
│   │   ├── requests.py          # Request models
│   │   └── responses.py         # Response models
│   ├── services/                 # Business logic services
│   │   ├── __init__.py
│   │   ├── auth_service.py      # Authentication service
│   │   └── ddgs_service.py      # DDGS search service
│   ├── __init__.py
│   └── app.py                    # FastAPI application
├── tests/                        # Test code
│   ├── __init__.py
│   ├── conftest.py              # Test configuration
│   ├── test_api.py              # API tests
│   ├── test_models.py           # Model tests
│   ├── test_services.py         # Service tests
│   └── test_integration.py      # Integration tests
├── scripts/                      # Utility scripts
│   ├── dev.sh                   # Development startup
│   ├── start.sh                 # Production startup
│   ├── test.sh                  # Test runner
│   ├── quick_test.sh            # Quick test runner
│   └── setup.sh                 # Environment setup
├── main.py                       # Application entry point
├── requirements.txt              # Python dependencies
├── pyproject.toml               # Project configuration
├── pytest.ini                   # Pytest configuration
├── Makefile                      # Make commands
├── .env.example                  # Environment variables example
├── .gitignore                    # Git ignore file
└── README.md                     # Project documentation
```

## 🚀 Quick Start

### Prerequisites

- Python 3.9+
- [uv](https://github.com/astral-sh/uv) package manager

### Installation

```bash
# Clone the repository
git clone https://github.com/fafnerzhang/python-search-api.git
cd python-search-api

# Install uv (if not already installed)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Install dependencies
make install
# or manually
uv sync
```

### Configuration

```bash
# Copy environment file
cp .env.example .env
# Edit .env to set your API_TOKEN (optional)
```

### Start the Service

```bash
# Development mode
make dev
# or
./scripts/dev.sh

# Production mode
make start
# or
./scripts/start.sh
```

### API Documentation

After starting the service, visit:

- **Swagger UI**: http://localhost:9410/docs
- **ReDoc**: http://localhost:9410/redoc
- **OpenAPI Schema**: http://localhost:9410/openapi.json

## 📊 Workflow Status

| Workflow | Status | Description |
|----------|--------|-------------|
| Tests | [![Tests](https://github.com/fafnerzhang/python-search-api/workflows/Tests/badge.svg)](https://github.com/fafnerzhang/python-search-api/actions/workflows/tests.yml) | Comprehensive test suite |
| Code Quality | [![Code Quality](https://github.com/fafnerzhang/python-search-api/workflows/Code%20Quality/badge.svg)](https://github.com/fafnerzhang/python-search-api/actions/workflows/code-quality.yml) | Linting, formatting, type checking |
| Unit Tests | [![Unit Tests](https://github.com/fafnerzhang/python-search-api/workflows/Unit%20Tests/badge.svg)](https://github.com/fafnerzhang/python-search-api/actions/workflows/unit-tests.yml) | Focused unit testing |
| Performance | [![Performance Tests](https://github.com/fafnerzhang/python-search-api/workflows/Performance%20Tests/badge.svg)](https://github.com/fafnerzhang/python-search-api/actions/workflows/performance.yml) | Performance benchmarks |
| CI/CD | [![CI/CD](https://github.com/fafnerzhang/python-search-api/workflows/CI%2FCD/badge.svg)](https://github.com/fafnerzhang/python-search-api/actions/workflows/ci-cd.yml) | Continuous integration |
| Nightly | [![Nightly Build](https://github.com/fafnerzhang/python-search-api/workflows/Nightly%20Build/badge.svg)](https://github.com/fafnerzhang/python-search-api/actions/workflows/nightly.yml) | Daily builds and scans |

## 🧪 Testing

### Full Test Suite

```bash
# Run all tests
make test
# or
./scripts/test.sh
```

### Quick Tests

```bash
# Run quick tests (models + services)
make test-quick
# or
./scripts/quick_test.sh
```

### Specific Test Categories

```bash
# Unit tests
make test-unit

# API tests
make test-api

# Integration tests
make test-integration

# Coverage report
make coverage
```

### Code Quality

```bash
# Linting
make lint

# Code formatting
make format

# Type checking
make type-check
```

## 📚 API Endpoints

### Web Search

**POST** `/search`
```json
{
  "query": "FastAPI",
  "region": "us-en",
  "safesearch": "moderate",
  "max_results": 10
}
```

**GET** `/search?q=FastAPI&max_results=10`

### Image Search

**POST** `/search/images`
```json
{
  "query": "python logo",
  "size": "Large",
  "max_results": 5
}
```

### News Search

**POST** `/search/news`
```json
{
  "query": "technology news",
  "time_limit": "d",
  "max_results": 5
}
```

## 🔐 Authentication

The API supports optional Bearer Token authentication:

```bash
curl -H "Authorization: Bearer YOUR_TOKEN" \
     -X POST "http://localhost:8999/search" \
     -H "Content-Type: application/json" \
     -d '{"query": "test"}'
```

## 🛠️ Development

### Project Architecture

- **src/core/**: Core configuration and shared utilities
- **src/models/**: Pydantic data models
- **src/services/**: Business logic and external service integration
- **src/api/**: FastAPI routes and endpoints
- **tests/**: Comprehensive test suite

### Adding New Features

1. Add functionality in the appropriate module
2. Write corresponding tests
3. Update API documentation
4. Run tests to ensure functionality works

### Testing Strategy

- **Unit Tests**: Test individual functions and models
- **API Tests**: Test HTTP endpoints
- **Integration Tests**: Test complete workflows
- **Mock Tests**: Mock external dependencies (DDGS)

## ⚙️ Environment Variables

```bash
# Optional configuration
API_TOKEN=your_secret_token    # API authentication token
HOST=0.0.0.0                   # Server host
PORT=9410                      # Server port
DEBUG=true                     # Debug mode
LOG_LEVEL=info                 # Logging level

# DDGS Configuration
DEFAULT_REGION=wt-wt           # Default search region
DEFAULT_SAFESEARCH=moderate    # Default safesearch level
DEFAULT_MAX_RESULTS=10         # Default max results
MAX_ALLOWED_RESULTS=100        # Maximum allowed results

# CORS Configuration
ALLOWED_ORIGINS=*              # Allowed origins
ALLOWED_METHODS=*              # Allowed methods
ALLOWED_HEADERS=*              # Allowed headers
```

## 🚀 Production Deployment

### Using Docker

```dockerfile
FROM python:3.11-slim

WORKDIR /app
COPY . .

RUN pip install uv
RUN uv pip install --system -r requirements.txt

EXPOSE 9410
CMD ["python", "main.py"]
```

### Direct Deployment

```bash
# Install dependencies
uv pip install -r requirements.txt

# Start production server
make start
```

## 🐛 Troubleshooting

### Common Issues

1. **DDGS Connection Error**: Check network connection
2. **Dependency Installation Failed**: Ensure Python version >= 3.9
3. **Tests Failing**: Check if test dependencies are installed

### Viewing Logs

```bash
# Check application logs
tail -f uvicorn.log

# Start in debug mode
DEBUG=true make dev
```

## 🤝 Contributing

1. Fork the project
2. Create a feature branch: `git checkout -b feature-name`
3. Add tests for your changes
4. Ensure all tests pass: `make test`
5. Format code: `make format`
6. Commit your changes: `git commit -am 'Add feature'`
7. Push to the branch: `git push origin feature-name`
8. Submit a pull request

## 🔄 CI/CD Workflows

This project uses comprehensive GitHub Actions workflows for continuous integration and deployment:

### Core Workflows
- **Tests** (`tests.yml`): Runs comprehensive test suite across multiple Python versions
- **Code Quality** (`code-quality.yml`): Enforces code standards with linting, formatting, and type checking
- **Unit Tests** (`unit-tests.yml`): Focused unit testing with detailed coverage reporting

### Specialized Workflows
- **Performance Tests** (`performance.yml`): Automated performance benchmarking
- **CI/CD** (`ci-cd.yml`): Continuous integration and deployment pipeline
- **Release** (`release.yml`): Automated release management with Docker image publishing
- **Nightly Build** (`nightly.yml`): Daily builds with extended testing and security scans

### Maintenance Workflows
- **Dependency Updates** (`dependency-updates.yml`): Automated dependency updates
- **Cleanup & Maintenance** (`cleanup.yml`): Repository maintenance and cleanup tasks

### Workflow Features
- ✅ Multi-version Python testing (3.9, 3.10, 3.11, 3.12)
- 📊 Comprehensive test coverage reporting via Codecov
- 🐳 Docker image building and publishing to GitHub Container Registry
- 🔒 Security scanning with Bandit and Safety
- 📈 Performance benchmarking and monitoring
- 🔄 Automated dependency updates with PR creation
- 🧹 Automated cleanup of old artifacts and containers

### Coverage Reporting

Test coverage is automatically tracked and reported via [Codecov](https://codecov.io/gh/fafnerzhang/python-search-api). The coverage badge in the README updates automatically with each test run.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🔗 Links

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [DuckDuckGo Search](https://github.com/deedy5/duckduckgo_search)
- [uv Package Manager](https://github.com/astral-sh/uv)

## 📞 Support

If you have any questions or run into issues, please [open an issue](https://github.com/fafnerzhang/python-search-api/issues) on GitHub.

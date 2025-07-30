# Python Search API 🔍

[![CI/CD Pipeline](https://github.com/fafnerzhang/python-search-api/workflows/CI%2FCD%20Pipeline/badge.svg)](https://github.com/fafnerzhang/python-search-api/actions/workflows/ci.yml)
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

## 📊 CI/CD Pipeline & Testing

This project uses a comprehensive GitHub Actions workflow that leverages all Makefile commands for automated testing, quality assurance, and deployment.

### Workflow Overview

Our CI/CD pipeline (`ci.yml`) includes the following stages:

| Stage | Commands Used | Description |
|-------|---------------|-------------|
| **Quick Tests** | `make test-quick` | Fast unit tests across Python 3.9-3.12 |
| **API Tests** | `make test-api` | Comprehensive API endpoint testing |
| **Integration Tests** | `make test-integration` | End-to-end integration testing |
| **Coverage Report** | `make coverage` | Generate and upload coverage reports |
| **Code Quality** | `make lint`, `make format`, `make type-check` | Code quality enforcement |
| **Docker Build** | `make docker-build` | Build Docker images with commit SHA tags |
| **Docker Test** | `make docker-run` + health checks | Test containerized application |
| **Deploy Staging** | Triggered on `develop` branch | Deploy to staging environment |
| **Deploy Production** | Triggered on `main` branch | Deploy to production environment |

### Performance Testing

A separate workflow (`performance.yml`) runs daily performance tests to ensure optimal API performance.

### Available Make Commands

The following Makefile commands are used throughout the CI/CD pipeline:

```bash
# Testing commands
make test-quick      # Quick unit tests
make test-api        # API endpoint tests
make test-integration # Integration tests
make coverage        # Generate coverage reports

# Code quality commands
make lint            # Run code linting
make format          # Format code with black
make type-check      # Run mypy type checking

# Docker commands
make docker-build    # Build Docker image
make docker-run      # Run Docker container
make docker-stop     # Stop and remove container

# Development commands
make install         # Install dependencies
make dev            # Start development server
make start          # Start production server
make clean          # Clean generated files
```

## 🧪 Testing

The testing strategy mirrors the CI/CD pipeline, using the same Makefile commands locally and in automation.

### Local Testing (Same as CI)

```bash
# Install dependencies (same as CI)
make install

# Run the same tests as in CI pipeline
make test-quick      # Quick tests (Python 3.9-3.12 in CI)
make test-api        # API tests (90% coverage requirement)
make test-integration # Integration tests (60% coverage requirement)
make coverage        # Generate coverage report + upload in CI

# Code quality checks (same as CI)
make lint           # Linting with flake8
make format         # Format with black (CI checks for changes)
make type-check     # Type checking with mypy
```

### Full Test Suite

```bash
# Run all tests (combines multiple Makefile commands)
make test
# or
./scripts/test.sh
```

### Docker Testing (Same as CI)

```bash
# Build and test Docker container (same as CI)
make docker-build
make docker-run

# Test health endpoint (same as CI validation)
curl -f http://localhost:9410/health

# Cleanup (same as CI)
make docker-stop
```

### Test Categories

| Test Type | Command | Coverage Requirement | CI Stage |
|-----------|---------|---------------------|----------|
| Quick Tests | `make test-quick` | N/A | Parallel across Python versions |
| API Tests | `make test-api` | 90% | After quick tests |
| Integration Tests | `make test-integration` | 60% | After quick tests |
| Full Coverage | `make coverage` | Combined report | After API + Integration |

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

## � Docker Usage

### Using Make Commands

```bash
# Build Docker image (uses git commit SHA as tag)
make docker-build

# Run Docker container with health checks and auto-restart
make docker-run

# Stop and remove Docker container
make docker-stop
```

### Manual Docker Commands

```bash
# Build image
docker build -t python-search-api .

# Run container
docker run -d --name python-search-api -p 9410:9410 python-search-api

# Check logs
docker logs python-search-api
```

### Docker Hub Images

The CI/CD pipeline automatically builds and pushes Docker images to GitHub Container Registry with the following tags:
- `ghcr.io/fafnerzhang/python-search-api:latest` (main branch)
- `ghcr.io/fafnerzhang/python-search-api:develop` (develop branch)
- `ghcr.io/fafnerzhang/python-search-api:<commit-sha>` (all commits)

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

### Setting Up Repository for CI/CD

Before the CI/CD pipeline can run successfully, ensure the following repository secrets are configured:

1. **GitHub Secrets** (Repository Settings → Secrets and variables → Actions):
   ```
   CODECOV_TOKEN        # Optional: For coverage reporting
   ```

2. **GitHub Container Registry**: 
   - The workflow automatically uses `GITHUB_TOKEN` for pushing Docker images
   - No additional setup required for GHCR access

### Development Workflow

1. Fork the project
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes and add tests
4. Run local testing (same commands as CI):
   ```bash
   make install          # Install dependencies
   make test-quick       # Quick tests
   make test-api         # API tests
   make test-integration # Integration tests
   make coverage         # Coverage report
   make lint            # Code linting
   make format          # Code formatting
   make type-check      # Type checking
   ```
5. Ensure Docker build works: `make docker-build && make docker-run`
6. Commit your changes: `git commit -am 'Add feature'`
7. Push to the branch: `git push origin feature-name`
8. Submit a pull request

### Pull Request Guidelines

- All CI checks must pass (same tests run locally)
- Code coverage should not decrease
- Follow existing code style (enforced by `make format`)
- Include tests for new functionality
- Update documentation if needed

The CI/CD pipeline will automatically:
- Run all tests across Python versions 3.9-3.12
- Check code quality and formatting
- Build and test Docker images
- Deploy to staging (on `develop` branch)
- Deploy to production (on `main` branch)

## 🔄 CI/CD Architecture

This project implements a modern CI/CD pipeline using GitHub Actions that leverages the comprehensive Makefile commands:

### Pipeline Stages

1. **Parallel Testing Phase**
   - Quick tests across multiple Python versions (3.9-3.12)
   - API endpoint testing with 90% coverage requirement
   - Integration testing with 60% coverage requirement

2. **Quality Assurance Phase**
   - Code linting with flake8
   - Code formatting validation with black
   - Type checking with mypy

3. **Coverage & Reporting Phase**
   - Comprehensive coverage report generation
   - Automatic upload to Codecov
   - Coverage thresholds enforcement

4. **Containerization Phase**
   - Docker image building with git commit SHA tagging
   - Multi-registry publishing (GitHub Container Registry)
   - Container health testing and validation

5. **Deployment Phase**
   - Staging deployment on `develop` branch pushes
   - Production deployment on `main` branch pushes
   - Environment-specific configuration management

### Key Features

- ✅ **Multi-version Testing**: Ensures compatibility across Python 3.9-3.12
- � **Container-first Approach**: Docker images built and tested automatically
- 📊 **Coverage Tracking**: Integrated with Codecov for coverage monitoring
- � **Quality Gates**: Enforced linting, formatting, and type checking
- 🚀 **Automated Deployment**: Environment-specific deployments
- ⚡ **Performance Monitoring**: Scheduled performance testing
- 🏷️ **Smart Tagging**: Git SHA-based container tagging

### Makefile Integration

The CI/CD pipeline extensively uses Makefile commands to ensure consistency between local development and automated testing:

```bash
# Core testing commands used in CI
make install         # Dependency installation
make test-quick      # Fast unit testing
make test-api        # API endpoint testing
make test-integration # Integration testing
make coverage        # Coverage reporting

# Quality assurance commands
make lint           # Code linting
make format         # Code formatting
make type-check     # Type checking

# Docker operations
make docker-build   # Container building
make docker-run     # Container deployment
make docker-stop    # Container cleanup
```

This approach ensures that developers can run the exact same commands locally as those used in the CI/CD pipeline, providing consistency and reliability across all environments.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🔗 Links

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [DuckDuckGo Search](https://github.com/deedy5/duckduckgo_search)
- [uv Package Manager](https://github.com/astral-sh/uv)

## 📞 Support

If you have any questions or run into issues, please [open an issue](https://github.com/fafnerzhang/python-search-api/issues) on GitHub.

# Dockerfile for python-search-api
FROM python:3.11-slim

# Set work directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy project files
COPY . /app

# Install uv (for dependency management)
RUN pip install uv

# Install Python dependencies using Makefile
RUN make install

# Expose port (adjust if your app uses a different port)
EXPOSE 9410

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV PORT=9410

# Command to run the API using Makefile (production start)
CMD ["make", "start"]

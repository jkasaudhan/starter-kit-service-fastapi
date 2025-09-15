FROM mcr.microsoft.com/devcontainers/python:3.9

# Install Poetry
RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH="/root/.local/bin:${PATH}"

# Install additional system packages if needed
RUN apt-get update && apt-get install -y \
    git \
    vim \
    && rm -rf /var/lib/apt/lists/*

# Install Python linting and formatting tools
RUN pip install --no-cache-dir \
    flake8 \
    black \
    autopep8 \
    mypy \
    pylint

# Set up working directory
WORKDIR /app
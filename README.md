# FastAPI Todo Starter Kit with Poetry

A production-ready FastAPI Todo application with REST API best practices, Poetry dependency management, Docker support, and development tools.

## Features

- RESTful API with proper HTTP status codes
- SQLModel for database operations with SQLite (easily switchable to PostgreSQL)
- Pydantic validation for request/response models
- Poetry for dependency management
- Docker and Docker Compose setup
- Dev Container configuration for VS Code
- Automatic code formatting with Black
- Linting with Ruff
- Unit tests with pytest
- Environment configuration with python-dotenv

## Quick Start

### Prerequisites

- Python 3.9+
- Poetry (install via `pip install poetry` or follow [official instructions](https://python-poetry.org/docs/#installation))
- Docker and Docker Compose (optional)

### Using Poetry

1. Clone the repository
2. Install dependencies: `poetry install`
3. Activate the virtual environment: `poetry shell`
4. Run the application: `poetry run start`
5. Access the API at `http://localhost:8000`
6. Interactive API docs at `http://localhost:8000/docs`

### Using Docker Compose

1. Clone the repository
2. Run `docker-compose up`
3. Access the API at `http://localhost:8000`
4. Interactive API docs at `http://localhost:8000/docs`

### Using Dev Containers (VS Code)

1. Open the project in VS Code
2. Install the "Dev Containers" extension if not already installed
3. Reopen in container (Ctrl+Shift+P → "Reopen in Container")
4. The server will start automatically with hot reload

## API Endpoints

- `GET /api/v1/health` - Health check
- `GET /api/v1/todos` - List all todos
- `POST /api/v1/todos` - Create a new todo
- `GET /api/v1/todos/{id}` - Get a specific todo
- `PUT /api/v1/todos/{id}` - Update a todo
- `DELETE /api/v1/todos/{id}` - Delete a todo

## Project Structure
fastapi-todo-starter-kit/
├── app/
│ ├── main.py # FastAPI application
│ ├── api/ # API routes
│ ├── models/ # Database models
│ ├── schemas/ # Pydantic schemas
│ ├── core/ # Configuration and settings
│ └── db/ # Database session management
├── tests/ # Unit tests
├── .devcontainer/ # Dev container configuration
├── .vscode/ # VS Code settings
├── docker-compose.yml # Docker Compose setup
├── Dockerfile # Production Dockerfile
├── pyproject.toml # Poetry configuration
├── .env.example # Environment variables template
└── README.md # This file


## Development Tools

- **Dependency Management**: Poetry
- **Code Formatting**: Black (automatically formats on save in VS Code)
- **Linting**: Ruff for fast linting
- **Testing**: pytest for unit tests
- **Database**: SQLModel with SQLite (easily switchable to PostgreSQL)

## Useful Poetry Commands

- Install dependencies: `poetry install`
- Add a new dependency: `poetry add <package>`
- Add a development dependency: `poetry add --group dev <package>`
- Run the application: `poetry run start`
- Run tests: `poetry run test`
- Activate virtual environment: `poetry shell`
- Update dependencies: `poetry update`

## Deployment

### Docker Deployment

1. Build the image: `docker build -t todo-app .`
2. Run the container: `docker run -p 8000:8000 todo-app`

### Docker Compose for Production

A production-ready Docker Compose file can be created by modifying the development version to:
- Use a production-grade database like PostgreSQL
- Remove volume mounts for production
- Use a production WSGI server like Gunicorn

### Cloud Deployment

This application can be deployed to:
- AWS ECS/EKS
- Google Cloud Run
- Azure Container Apps
- Heroku
- DigitalOcean App Platform

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Ensure all tests pass
6. Submit a pull request

## License

MIT License. See LICENSE file for details.
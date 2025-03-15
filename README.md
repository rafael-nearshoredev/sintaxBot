# FastAPI Syntax Analyzer

## Overview
This project is a FastAPI-based syntax analyzer that evaluates the grammatical correctness of sentences in different languages. It includes API endpoints to analyze syntax and returns structured responses.

## Features
- FastAPI framework for high-performance API
- Syntax analysis using spaCy
- Logging with Loguru
- Swagger UI documentation (configurable via environment variable)
- Dockerized for easy deployment

## Requirements
- Python 3.12
- Docker & Docker Compose

### Running with Docker
1. Build and run the service:
   ```bash
   docker compose up --build
   ```
2. The API will be available at `http://localhost:8000`

## Environment Variables
| Variable       | Description                                   | Default |
|---------------|-----------------------------------------------|---------|
| `ACTIVE_SWAGGER` | Enables Swagger UI (`true`/`false`)         | `true`  |

## API Endpoints
| Method | Endpoint       | Description                |
|--------|---------------|----------------------------|
| GET    | `/`           | Redirects to `/docs` if `ACTIVE_SWAGGER=true` |
| POST   | `/analyze`    | Analyzes sentence syntax |


## Access the API documentation at:
   - Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)
   - Redoc: [http://localhost:8000/redoc](http://localhost:8000/redoc)


## License
This project is licensed under the MIT License.

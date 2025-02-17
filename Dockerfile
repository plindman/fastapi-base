FROM python:3.10-slim

# Install uv.
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Create working directory.
WORKDIR /project

# Install the application dependencies.
COPY pyproject.toml /project/pyproject.toml
RUN uv sync --frozen --no-cache

# Copy the application into the container.
COPY ./app /project/app

# Run the application.
CMD ["uv", "run", "fastapi", "run", "app/main.py", "--port", "8080", "--host", "0.0.0.0"]

FROM python:3.12-slim-bookworm
COPY --from=ghcr.io/astral-sh/uv:0.6.1 /uv /uvx /bin/

ENV UV_COMPILE_BYTECODE=1
ENV UV_LINK_MODE=copy

WORKDIR /app

# Build the .venv
ADD pyproject.toml /app
ADD uv.lock /app
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen

# Copy app and run
ADD app /app

# Run the FastAPI application by default
ENV PATH="/app/.venv/bin:$PATH"

CMD ["fastapi", "run", "/app/main.py"]
# "uv", "run", 
# "--host", "0.0.0.0", 

# template-fastapi

Simple template for FastAPI projects

## Commands

```sh
uv run fastapi dev --help
uv run fastapi dev app/main.py --port=8000
uv run fastapi run app/main.py
uv run pytest
```

## Commands used to create it

```sh
git init
uv init app 
uv add fastapi --extra standard 
uv add pydantic-settings
uv add pytest
```

## Inspiration

- https://fastapi.tiangolo.com/
- https://docs.astral.sh/uv/guides/integration/fastapi/

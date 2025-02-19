# fastapi-base

FastAPI project based on plindman/fastapi-base

## Getting started

1. Set the API key in environment variable or `.env` in the root folder

``` ini
FASTAPI_API_KEY=[your api key]
```

2. Run the development server

```sh
uv run fastapi dev app/main.py --port=8000
```

### Other commands

```sh
uv run fastapi dev app/main.py --port=8000
uv run fastapi run app/main.py
uv run fastapi dev --help
uv run pytest # remember to add your own tests for the APIs you add
```

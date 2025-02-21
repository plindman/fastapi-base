''' fastAPI app main file ''' 
from fastapi import FastAPI

app = FastAPI()
app.title = "[API app title here]"

# Middleware 
# https://fastapi.tiangolo.com/tutorial/middleware/
# https://fastapi.tiangolo.com/advanced/middleware/
# HTTPSRedirectMiddleware
# TrustedHostMiddleware
# https://fastapi.tiangolo.com/tutorial/cors/
# CORS
# https://github.com/florimondmanca/awesome-asgi
# OpenTelemetry ASGI Instrumentation

# Logging
# Security

# Routes
from app.core.router import router as app_router
app.include_router(app_router, tags=["App"], prefix="/app", )

# from app.services.data_service.router import router as data_service_router
# app.include_router(data_service_router, prefix="/data", tags=["Data"])

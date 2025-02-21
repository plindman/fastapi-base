''' fastAPI app main file ''' 
from fastapi import FastAPI
from app.core.router import router as app_router
from app.services.data_service.router import router as data_service_router

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
app.include_router(app_router, tags=["App"], prefix="/app", )
app.include_router(data_service_router, prefix="/data", tags=["Data"])

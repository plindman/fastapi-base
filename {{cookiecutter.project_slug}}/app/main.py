''' fastAPI app main file ''' 
from fastapi import FastAPI

app = FastAPI()
app.title = "[API app title here]"

# Middleware 
# https://fastapi.tiangolo.com/tutorial/middleware/
# https://fastapi.tiangolo.com/advanced/middleware/

# HTTPSRedirectMiddleware
# from starlette.middleware.httpsredirect import HTTPSRedirectMiddleware
# app.add_middleware(HTTPSRedirectMiddleware)

# TrustedHostMiddleware
# from starlette.middleware.trustedhost import TrustedHostMiddleware
# app.add_middleware(TrustedHostMiddleware)

# CORS
# https://fastapi.tiangolo.com/tutorial/cors/
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this to your needs
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# OpenTelemetry ASGI Instrumentation
# https://github.com/florimondmanca/awesome-asgi
# from opentelemetry.instrumentation.asgi import ASGIInstrumentor
# ASGIInstrumentor.instrument_app(app)

# Logging

# Routes
from app.core.router import router as app_router
app.include_router(app_router, tags=["App"], prefix="/app", )

from app.services import router as services_router
app.include_router(services_router)

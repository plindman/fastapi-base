''' fastAPI app main file ''' 
from fastapi import FastAPI
from app.common.router import router as common_router

app = FastAPI()

app.include_router(common_router)

# from src.routers import get_status
from src.routers import account_router, status_router 
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
def create_app():
    app = FastAPI(
        title = "lattergalary"
    )
    app.include_router(status_router)
    app.include_router(account_router)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_methods=["*"],
        allow_credentials=True,
    )
    return app


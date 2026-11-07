from starlette.staticfiles import StaticFiles
from pathlib import Path
from dotenv import load_dotenv
from fastapi import FastAPI
from src.features.products.infraestructure.routes.ProductRoutes import router as product_router
from fastapi.middleware.cors import CORSMiddleware
import os

load_dotenv()

app = FastAPI()

Path("assets/products").mkdir(parents=True, exist_ok=True)

app.mount("/static", StaticFiles(directory="assets"), name="static")

raw_origins = os.getenv("ORIGINS")

origins = [origin.strip() for origin in raw_origins.join(",") if origin.strip()]

app.add_middleware(
    CORSMiddleware,
    allow_origins= origins, 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(product_router)

@app.get("/health")
def health_check():
    return {
        "version": "v1.0.0",
        "status": "ok"
    }
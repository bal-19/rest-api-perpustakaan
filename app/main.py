from fastapi import FastAPI
from fastapi_cache import FastAPICache
from fastapi_cache.backends.inmemory import InMemoryBackend

from app.controller.library_controller import router as library_router

app = FastAPI()

# Include the library route
app.include_router(library_router, prefix="/api/v1/perpustakaan")

@app.get("/")
def read_root():
    return {"message": "Welcome to the Perpustakaan Crawler API!"}

@app.on_event("startup")
async def startup():
    FastAPICache.init(InMemoryBackend(), prefix="fastapi-cache")
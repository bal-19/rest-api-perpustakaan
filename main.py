import uvicorn
from fastapi import FastAPI
from fastapi_cache import FastAPICache
from fastapi_cache.backends.inmemory import InMemoryBackend

from source.controller.library_controller import router as library_router

app = FastAPI(title="Perpustakaan Service", description="Service untuk mendapatkan data perpustakaan yang ada di Indonesia")

# Include the library route
app.include_router(library_router, prefix="/api/v1/perpustakaan")

@app.get("/")
async def read_root():
    return {"message": "Welcome to the Perpustakaan Crawler API!"}

@app.on_event("startup")
async def startup():
    FastAPICache.init(InMemoryBackend(), prefix="fastapi-cache")
    

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=1919, reload=True)
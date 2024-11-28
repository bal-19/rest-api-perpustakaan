import uvicorn
import argparse

from fastapi_cache.backends.inmemory import InMemoryBackend
from fastapi_cache import FastAPICache
from fastapi import FastAPI

from api.v1.endpoints import perpusnas
from core.database import db
from core.config import settings

app = FastAPI(title=settings.APP_NAME, version="1.0.0")

# Event startup dan shutdown for connection database
@app.on_event("startup")
async def startup_event():
    FastAPICache.init(InMemoryBackend(), prefix="fastapi-cache")
    await db.connect()

@app.on_event("shutdown")
async def shutdown_event():
    await FastAPICache.clear()
    await db.close()


# Router
app.include_router(perpusnas.router, prefix="/api/v1/perpusnas")

@app.get("/")
async def root():
    return {"message": "hhuh!?"}

if __name__ == "__main__":
    argp = argparse.ArgumentParser()
    argp.add_argument("--host", dest="host", type=str, default="127.0.0.1")
    argp.add_argument("--port", dest="port", type=int, default=8000)
    argp.add_argument("--reload", dest="reload", action="store_true")
    args = argp.parse_args()
    
    uvicorn.run(
        "main:app",
        host=args.host,
        port=args.port,
        reload=args.reload
    )
from fastapi import APIRouter
from fastapi_cache.decorator import cache

from app.service.crawler_service import LibraryCrawlerService

router = APIRouter()

@router.get("/")
@cache(expire=3600)  # Cache this endpoint for 1 hour
def get_libraries():
    # Instantiate the crawler service and fetch libraries data
    service = LibraryCrawlerService()
    libraries = service.fetch_libraries_data()
    return libraries

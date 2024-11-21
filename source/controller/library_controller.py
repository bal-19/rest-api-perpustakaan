from fastapi import APIRouter, HTTPException, Query
from fastapi_cache.decorator import cache

from ..service.crawler_service import LibraryCrawlerService
from ..helper.fetch import FetchDataPerpustakaan

router = APIRouter()
service = LibraryCrawlerService()
fetcher = FetchDataPerpustakaan()

@router.get("/data", tags=["Perpustakaan"])
@cache(expire=1800)  # Cache this endpoint for 30 minute
async def get_libraries(
    limit: int = Query(10, ge=5, le=50, description="Maximum amount of data to be displayed"),
    page: int = Query(1, ge=1, description="The data page you want to retrieve")
):
    
    libraries = fetcher.get_all(page=page, limit=limit)

    if libraries:
        return {
            'status': 'success',
            'data': libraries
        }

@router.get("/data/search", tags=["Perpustakaan"])
@cache(expire=1800)  # Cache this endpoint for 30 minute
async def get_libraries_by_search(
    query: str,
    limit: int = Query(10, ge=5, le=50, description="Maximum amount of data to be displayed"),
    page: int = Query(1, ge=1, description="The data page you want to retrieve")
):
    
    libraries = fetcher.get_by_search(query, page=page, limit=limit)

    if libraries:
        return {
            'status': 'success',
            'data': libraries
        }

@router.get("/data/filter", tags=["Perpustakaan"])
@cache(expire=1800)  # Cache this endpoint for 30 minute
async def get_libraries_by_filter(
    key: str,
    value: str,
    limit: int = Query(10, ge=5, le=50, description="Maximum amount of data to be displayed"),
    page: int = Query(1, ge=1, description="The data page you want to retrieve")
):
    """
    Key for column name <br>
    Value for value at column
    """
    
    
    libraries = fetcher.get_by_filter(key, value, page=page, limit=limit)

    if libraries:
        return {
            'status': 'success',
            'data': libraries
        }

@router.get("/list/type", tags=["Type"], description="Getting type list")
@cache(expire=900) # cache for 15 minute
async def get_type():
    types = service.fetch_type_data()
    
    if types:
        return {
            'status': 'success',
            'types': types
        }
    
@router.get("/list/subtype/{type_name}", tags=["Type"], description="Getting subtype list")
@cache(expire=900) # cache for 15 minute
async def get_subtype(type_name: str):
    subtypes = service.fetch_subtype_data(type_name)
    
    if subtypes:
        return {
            'status': 'success',
            'subtypes': subtypes
        }

@router.get("/list/region/provinces", tags=["Region"], description="Get all provinces at Indonesia")
@cache(expire=900) # cache for 15 minute
async def get_provinces():
    provinces = service.fetch_province_data()
    
    if provinces:
        return {
            'status': 'success',
            'data': provinces
        }
        
    else:
        return {
            'status': 'error',
            'message': 'empty data',
            'data': provinces
        }

@router.get("/list/region/regencies/{id_province}", tags=["Region"], description="Get all regencies in a province")
@cache(expire=900)
async def get_regencies(id_province: str):
    regencies = service.fetch_city_data(id_province)
    
    if regencies:
        return {
            'status': 'success',
            'data': regencies,
        }
    
    else:
        return {
            'status': 'error',
            'message': 'empty data',
            'data': regencies
        }

@router.get("/list/region/districts/{id_regency}", tags=["Region"], description="Get all district in a regency")
@cache(expire=900)
async def get_districts(id_regency: str):
    district = service.fetch_district_data(id_regency)
    
    if district:
        return {
            'status': 'success',
            'data': district,
        }
    
    else:
        return {
            'status': 'error',
            'message': 'empty data',
            'data': district
        }

@router.get("/list/region/villages/{id_district}", tags=["Region"], description="Get all villages in a district")
@cache(expire=900)
async def get_villages(id_district: str):
    subdistrict = service.fetch_subdistrict_data(id_district)
    
    if subdistrict:
        return {
            'status': 'success',
            'data': subdistrict,
        }
    
    else:
        return {
            'status': 'error',
            'message': 'empty data',
            'data': subdistrict
        }
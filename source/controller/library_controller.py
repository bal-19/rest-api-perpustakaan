from fastapi import APIRouter, HTTPException, Query
from fastapi_cache.decorator import cache

from ..service.crawler_service import LibraryCrawlerService

router = APIRouter()
service = LibraryCrawlerService()

@router.get("/data", tags=["Perpustakaan"])
@cache(expire=1800)  # Cache this endpoint for 30 minute
async def get_libraries(
    type_name: str = Query('', description="Jenis perpustakaan (opsional)"),
    subtype_name: str = Query('', description="Subjenis perpustakaan (opsional)"),
    province_id: str = Query('', description="ID provinsi (opsional)"),
    regency_id: str = Query('', description="ID kabupaten/kota (opsional)"),
    subdistrict_id: str = Query('', description="ID kecamatan (opsional)"),
    village_id: str = Query('', description="ID kelurahan (opsional)"),
    start: int = Query(0, description="Start length. ex: 0, 10, 20 (opsional)"),
    length: int = Query(10, description="Jumlah data yang ingin diambil (opsional)")
):
    # Instantiate the crawler service and fetch libraries data
    libraries = service.fetch_libraries_data(
        jenis=type_name,
        subjenis=subtype_name,
        provinsi_id=province_id,
        kabkota_id=regency_id,
        kecamatan_id=subdistrict_id,
        kelurahan_id=village_id,
        start=start,
        length=length
    )

    if libraries.get("data"):
        return {
            'status': 'success',
            **libraries
        }
        
    else:
        return {
            'status': 'error',
            'message': 'empty data',
            **libraries
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
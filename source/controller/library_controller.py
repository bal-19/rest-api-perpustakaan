from fastapi import APIRouter, HTTPException, Query
from fastapi_cache.decorator import cache

from service.crawler_service import LibraryCrawlerService

router = APIRouter()
service = LibraryCrawlerService()

@router.get("/data", tags=["Perpustakaan"])
@cache(expire=1800)  # Cache this endpoint for 30 minute
async def get_libraries(
    type_name: str = Query('', description="Jenis perpustakaan (opsional)"),
    province_id: str = Query('', description="ID provinsi (opsional)"),
    city_id: str = Query('', description="ID kabupaten/kota (opsional)"),
    district_id: str = Query('', description="ID kecamatan (opsional)"),
    subdistrict_id: str = Query('', description="ID kelurahan (opsional)"),
    length: int = Query(10, description="Jumlah data yang ingin diambil (opsional)")
):
    # Instantiate the crawler service and fetch libraries data
    libraries = service.fetch_libraries_data(
        jenis=type_name,
        provinsi_id=province_id,
        kabkota_id=city_id,
        kecamatan_id=district_id,
        kelurahan_id=subdistrict_id,
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
    
@router.get("/list/subtype/{nama_jenis}", tags=["Type"], description="Getting subtype list")
@cache(expire=900) # cache for 15 minute
async def get_subtype(nama_jenis: str):
    subtypes = service.fetch_subtype_data(nama_jenis)
    
    if subtypes:
        return {
            'status': 'success',
            'subtypes': subtypes
        }

@router.get("/list/region/province", tags=["Region"], description="Get all province at Indonesia")
@cache(expire=900) # cache for 15 minute
async def get_province():
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

@router.get("/list/region/city/{id_province}", tags=["Region"], description="Get all cities in a province")
@cache(expire=900)
async def get_city(id_province: str):
    cities = service.fetch_city_data(id_province)
    
    if cities:
        return {
            'status': 'success',
            'data': cities,
        }
    
    else:
        return {
            'status': 'error',
            'message': 'empty data',
            'data': cities
        }

@router.get("/list/region/district/{id_city}", tags=["Region"], description="Get all district/kecamatan in a city")
@cache(expire=900)
async def get_district(id_city: str):
    district = service.fetch_district_data(id_city)
    
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

@router.get("/list/region/subdistrict/{id_district}", tags=["Region"], description="Get all subdistrict/kelurahan in a district")
@cache(expire=900)
async def get_subdistrict(id_district: str):
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
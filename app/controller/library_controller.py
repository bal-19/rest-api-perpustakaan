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

@router.get("/type", tags=["Type"])
@cache(expire=900) # cache for 15 minute
async def get_type():
    types = service.fetch_type_data()
    
    if types:
        return {
            'status': 'success',
            'types': types
        }
    
@router.get("/subtype/{nama_jenis}", tags=["Type"])
@cache(expire=900) # cache for 15 minute
async def get_subtype(nama_jenis: str):
    subtypes = service.fetch_subtype_data(nama_jenis)
    
    if subtypes:
        return {
            'status': 'success',
            'subtypes': subtypes
        }

@router.get("/region/province", tags=["Region"])
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
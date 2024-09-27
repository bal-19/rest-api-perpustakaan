from fastapi import APIRouter, HTTPException, Query
from fastapi_cache.decorator import cache

from service.crawler_service import LibraryCrawlerService

router = APIRouter()

@router.get("/data")
@cache(expire=1800)  # Cache this endpoint for 30 minute
async def get_libraries(
    jenis: str = Query('', description="Jenis perpustakaan (opsional)"),
    provinsi_id: str = Query('', description="ID provinsi (opsional)"),
    kabkota_id: str = Query('', description="ID kabupaten/kota (opsional)"),
    kecamatan_id: str = Query('', description="ID kecamatan (opsional)"),
    kelurahan_id: str = Query('', description="ID kelurahan (opsional)"),
    length: int = Query(10, description="Jumlah data yang ingin diambil (opsional)")
):
    # Instantiate the crawler service and fetch libraries data
    try:
        service = LibraryCrawlerService()
        libraries = service.fetch_libraries_data(
            jenis=jenis,
            provinsi_id=provinsi_id,
            kabkota_id=kabkota_id,
            kecamatan_id=kecamatan_id,
            kelurahan_id=kelurahan_id,
            length=length
        )

        if libraries:
            return {
                'status': 'success',
                **libraries
            }
            
        else:
            return {
                'status': 'error',
                **libraries
            }

    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error {e}")

@router.get("/jenis")
@cache(expire=900) # cache for 15 minute
async def get_type():
    try:
        service = LibraryCrawlerService()
        types = service.fetch_type_data()
        
        if types:
            return {
                'status': 'success',
                'types': types
            }

        else:
            return {
                'status': 'success',
                'types': []
            }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error {e}")
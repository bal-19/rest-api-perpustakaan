from fastapi import APIRouter, Depends, Query
from fastapi_cache.decorator import cache

from schemas.perpusnas import PerpusnasResponse
from services.perpusnas_service import PerpusnasService


router = APIRouter()

@router.get("/data", response_model=PerpusnasResponse, tags=["Perpustakaan"], description="Mengambil semua data perpustakaan tanpa filter")
@cache(expire=1800)
async def get_libraries(
    service: PerpusnasService = Depends(),
    limit: int = Query(10, ge=5, le=50, description="Maximum amount of data to be displayed"),
    page: int = Query(1, ge=1, description="The data page you want to retrieve")
):
    return await service.get_all(page=page, limit=limit)

@router.get("/data/search", response_model=PerpusnasResponse, tags=["Perpustakaan"], description="Mengambil semua data perpustakaan berdasarkan nama perpustakaan yang dicari")
@cache(expire=1800)
async def get_libraries_by_search(
    query: str,
    service: PerpusnasService = Depends(),
    limit: int = Query(10, ge=5, le=50, description="Maximum amount of data to be displayed"),
    page: int = Query(1, ge=1, description="The data page you want to retrieve")
):
    return await service.get_by_search(query, page=page, limit=limit)

@router.get("/data/filter", response_model=PerpusnasResponse, tags=["Perpustakaan"], description="Mengambil semua data perpustakaan berdasarkan filter yang telah ditetapkan")
@cache(expire=1800)
async def get_libraries_by_filter(
    key: str,
    value: str,
    service: PerpusnasService = Depends(),
    limit: int = Query(10, ge=5, le=50, description="Maximum amount of data to be displayed"),
    page: int = Query(1, ge=1, description="The data page you want to retrieve")
):
    """
    Key for column name <br>
    Value for value at column
    """
    return await service.get_by_filter(key, value, page=page, limit=limit)


@router.get("/list/type", response_model=list, tags=["Type"], description="Mengambil jenis jenis perpustakaan yang tersedia")
@cache(expire=3600)
async def get_type(
    service: PerpusnasService = Depends()
):
    return service.get_type()

@router.get("/list/subtype/{type_name}", response_model=list, tags=["Type"], description="Mengambil subjenis perpustakaan yang tersedia")
@cache(expire=3600)
async def get_subtype(
    type_name: str,
    service: PerpusnasService = Depends()
):
    return service.get_subtype(type_name)


@router.get("/list/region/provinces", tags=["Region"], description="Mengambil semua Provinsi yang ada di Indonesia")
@cache(expire=3600) 
async def get_provinces(
    service: PerpusnasService = Depends()
):
    return service.get_province()

@router.get("/list/region/regencies/{id_province}", tags=["Region"], description="Mengambil semua Kab/Kota yang ada di Indonesia")
@cache(expire=3600)
async def get_regencies(
    id_province: str,
    service: PerpusnasService = Depends()
):
    return service.get_city(id_province)

@router.get("/list/region/districts/{id_regency}", tags=["Region"], description="Mengambil semua Kecamatan yang ada di Indonesia")
@cache(expire=3600)
async def get_districts(
    id_regency: str,
    service: PerpusnasService = Depends()
):
    return service.get_district(id_regency)

@router.get("/list/region/villages/{id_district}", tags=["Region"], description="Mengambil semua Kelurahan/Desa yang ada di Indonesia")
@cache(expire=3600)
async def get_villages(
    id_district: str,
    service: PerpusnasService = Depends()
):
    return service.get_subdistrict(id_district)
from pydantic import BaseModel
from typing import Optional, List

from models.perpusnas import PerpusnasModel

class PerpusnasResponse(BaseModel):
    page: int
    limit: int
    total_data: int
    total_pages: int
    result: List[PerpusnasModel]

class ProvinceResponse(BaseModel):
    id: str
    nama: str
    singkatan: str
    keterangan: Optional[str]
    latitude: Optional[str]
    longitude: Optional[str]
    created_at: Optional[str]
    updated_at: Optional[str]
    deleted_at: Optional[str]
    kode_map: Optional[str]

class CityResponse(BaseModel):
    id: str
    province_id: str
    nama: str
    nama_provinsi: str
    keterangan: Optional[str]
    latitude: Optional[str]
    longitude: Optional[str]
    created_at: Optional[str]
    updated_at: Optional[str]
    deleted_at: Optional[str]
    
class DistrictResponse(BaseModel):
    id: str
    city_id: str
    nama: str
    nama_provinsi: str
    nama_kabkota: str
    keterangan: Optional[str]
    latitude: Optional[str]
    longitude: Optional[str]
    created_at: Optional[str]
    updated_at: Optional[str]
    deleted_at: Optional[str]
    
class VillageResponse(BaseModel):
    id: str
    district_id: str
    nama: str
    nama_provinsi: str
    nama_kabkota: str
    nama_kecamatan: str
    keterangan: Optional[str]
    latitude: Optional[str]
    longitude: Optional[str]
    created_at: Optional[str]
    updated_at: Optional[str]
    deleted_at: Optional[str]
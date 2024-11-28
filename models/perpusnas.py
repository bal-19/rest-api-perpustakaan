from pydantic import BaseModel
from typing import Optional


class PerpusnasModel(BaseModel):
    npp: Optional[str]
    npp_lama: Optional[str]
    nama: str
    lembaga: Optional[str]
    jenis: str
    subjenis: Optional[str]
    status: Optional[str]
    status_npp: Optional[str]
    alamat: Optional[str]
    telepon: Optional[str]
    email: Optional[str]
    website: Optional[str]
    kode_pos: Optional[str]
    kelurahan: str
    kecamatan: str
    kabkota: str
    provinsi: str
    created_at: int
    updated_at: int
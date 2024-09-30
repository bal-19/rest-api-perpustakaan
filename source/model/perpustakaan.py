from pydantic import BaseModel, Field

class PerpustakaanMeta(BaseModel):
    npp: str
    nama: str
    lembaga: str
    alamat: str
    telepon: str
    email: str
    website: str
    jenis: str
    subjenis: str
    status_perpustakaan: str
    kode_pos: str
    provinsi: str
    kabkota: str
    kecamatan: str
    kelurahan: str
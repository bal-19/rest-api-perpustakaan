from pydantic import BaseModel

class Library(BaseModel):
    npp: str
    nama: str
    alamat: str
    kode_pos: str
    telepon: str
    jenis: str
    sub_jenis: str
    lembaga_induk: str
    status_perpustakaan: str
    provinsi: str
    kota: str
    kecamatan: str
    kelurahan: str
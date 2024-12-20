import urllib.parse
from typing import List

from models.perpusnas import PerpusnasModel
from utils.scraper import WebScraper
from utils import validate_data
from core.config import settings
from core.database import db


class PerpusnasService:
    def __init__(self) -> None:
        self.scraper = WebScraper()
        self.source = "https://data.perpusnas.go.id"
    
    def get_type(self) -> List:
        url = f"{self.source}/reference/list-dropdown/jenis-perpustakaan"
        
        types = self.scraper.scrape_type(url)
        return types
    
    def get_subtype(self, type: str) -> List:
        type_encode = urllib.parse.quote(type.upper())
        url = f"{self.source}/reference/list-dropdown/subjenis-perpustakaan/{type_encode}"
        
        subtypes = self.scraper.scrape_type(url)
        return subtypes

    def get_province(self) -> List[dict]:
        url = f"{self.source}/public/kewilayahan/dati1/list-dropdown"
        
        provinces = self.scraper.scrape_region(url)
        return provinces

    def get_city(self, id_provinsi: str) -> List[dict]:
        url = f"{self.source}/public/kewilayahan/dati2/list-dropdown/{id_provinsi}"
        
        city = self.scraper.scrape_region(url)
        for c in city:
            c["province_id"]  = c.pop("dati1id")
        
        return city
    
    def get_district(self, id_kabkota: str) -> List[dict]:
        url = f"{self.source}/public/kewilayahan/dati3/list-dropdown/{id_kabkota}"
        
        district = self.scraper.scrape_region(url)
        for d in district:
            d["city_id"]  = d.pop("dati2id")
            
        return district

    def get_subdistrict(self, id_kecamatan: str) -> List[dict]:
        url = f"{self.source}/public/kewilayahan/dati4/list-dropdown/{id_kecamatan}"
        
        subdistrict = self.scraper.scrape_region(url)
        for s in subdistrict:
            s["district_id"]  = s.pop("dati3id")
        
        return subdistrict
    
    
    @staticmethod
    async def get_all(page: int, limit: int, **kwargs) -> dict:
        """
        Mengambil semua data dari MongoDB

        Args:
            page (int): Halaman yang ingin ditampilkan
            limit (int): Batas data yang ingin ditampilkan

        Returns:
            dict: Deskripsi data dan list data perpustakaan
        """
        filter_mongo = {}
        fields = ["jenis", "subjenis", "provinsi", "kabkota", "kecamatan", "kelurahan"]
        for field in fields:
            value = kwargs.get(field)
            if value:
                filter_mongo[field] = {
                    "$regex": f"^{value}$", 
                    "$options": "i"
                }
        
        offset = (page - 1) * limit
        
        cursor = db.client[settings.DATABASE_NAME]["data_perpustakaan"].find(filter_mongo).skip(offset).limit(limit)
        result = await cursor.to_list()
        
        total_data = await db.client[settings.DATABASE_NAME]["data_perpustakaan"].count_documents(filter_mongo)
        
        data: List[PerpusnasModel] = list()
        for row in result:
            row.pop("_id")
            data.append(await validate_data(row))
        
        return {
            "page": page,
            "limit": limit,
            "total_data": total_data,
            "total_pages": (total_data + limit - 1) // limit,
            "result": data
        }
    
    @staticmethod
    async def get_by_search(value: str, page: int, limit: int) -> dict:
        """
        Mengambil semua data dari MongoDB berdasarkan nama perpustakaan yang dicari

        Args:
            value (str): Nama perpustakaan yang akan dicari
            page (int): Halaman yang ingin ditampilkan
            limit (int): Batas data yang ingin ditampilkan

        Returns:
            dict: Deskripsi data dan list data perpustakaan
        """
        filter_mongo = { "$text": { "$search": value } }

        offset = (page - 1) * limit
        
        cursor = db.client[settings.DATABASE_NAME]["data_perpustakaan"].find(filter_mongo).skip(offset).limit(limit)
        result = await cursor.to_list()
        
        total_data = await db.client[settings.DATABASE_NAME]["data_perpustakaan"].count_documents(filter_mongo)
        
        data: List[PerpusnasModel] = list()
        for row in result:
            row.pop("_id")
            data.append(await validate_data(row))
        
        return {
            "query": value,
            "page": page,
            "limit": limit,
            "total_data": total_data,
            "total_pages": (total_data + limit - 1) // limit,
            "result": data
        }
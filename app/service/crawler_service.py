import urllib.parse

from fastapi import HTTPException
from typing import List

from helper.scraper import WebScraper

class LibraryCrawlerService:
    def __init__(self):
        self.scraper = WebScraper()

    # DATA PERPUSTAKAAN
    def fetch_libraries_data(self, jenis: str, provinsi_id: str, kabkota_id: str, kecamatan_id: str, kelurahan_id: str, length: int) -> List[dict]:
        url = "https://data.perpusnas.go.id/public/direktori/list"
        
        # fetch data using scraper helper
        libraries = self.scraper.scrape_libraries(
            url,
            jenis=jenis,
            provinsi_id=provinsi_id,
            kabkota_id=kabkota_id,
            kecamatan_id=kecamatan_id,
            kelurahan_id=kelurahan_id,
            length=length
        )
        return libraries
        
    # TYPE
    def fetch_type_data(self) -> List:
        url = "https://data.perpusnas.go.id/reference/list-dropdown/jenis-perpustakaan"
        
        # fetch data
        types = self.scraper.scrape_type(url)
        return types
    
    # SUBTYPE
    def fetch_subtype_data(self, type: str) -> List:
        type_encode = urllib.parse.quote(type.upper())
        url = f"https://data.perpusnas.go.id/reference/list-dropdown/subjenis-perpustakaan/{type_encode}"
        
        # fetch all subtype from type
        subtypes = self.scraper.scrape_subtype(url)
        return subtypes

    # PROVINCE
    def fetch_province_data(self) -> List[dict]:
        url = "https://data.perpusnas.go.id/public/kewilayahan/dati1/list-dropdown"
        
        # fetch all province at Indonesia
        provinces = self.scraper.scrape_province(url)
        return provinces
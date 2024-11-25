import urllib.parse

from fastapi import HTTPException
from typing import List

from ..helper.scraper import WebScraper
from ..helper.fetch import FetchDataPerpustakaan

class LibraryCrawlerService:
    def __init__(self):
        self.scraper = WebScraper()
        self.source = "https://data.perpusnas.go.id"

    def fetch_type_data(self) -> List:
        url = f"{self.source}/reference/list-dropdown/jenis-perpustakaan"
        
        # fetch data
        types = self.scraper.scrape_type(url)
        return types
    
    # SUBTYPE
    def fetch_subtype_data(self, type: str) -> List:
        type_encode = urllib.parse.quote(type.upper())
        url = f"{self.source}/reference/list-dropdown/subjenis-perpustakaan/{type_encode}"
        
        # fetch all subtype from type
        subtypes = self.scraper.scrape_type(url)
        return subtypes

    # PROVINCE
    def fetch_province_data(self) -> List[dict]:
        url = f"{self.source}/public/kewilayahan/dati1/list-dropdown"
        
        # fetch all province at Indonesia
        provinces = self.scraper.scrape_region(url)
        return provinces

    # CITY
    def fetch_city_data(self, id_provinsi: str) -> List[dict]:
        url = f"{self.source}/public/kewilayahan/dati2/list-dropdown/{id_provinsi}"
        
        # fetch all city in province
        city = self.scraper.scrape_region(url)
        return city
    
    # DISTRICT
    def fetch_district_data(self, id_kabkota: str) -> List[dict]:
        url = f"{self.source}/public/kewilayahan/dati3/list-dropdown/{id_kabkota}"
        
        # fetch all district/kecamatan
        district = self.scraper.scrape_region(url)
        return district

    # SUBDISTRICT
    def fetch_subdistrict_data(self, id_kecamatan: str) -> List[dict]:
        url = f"{self.source}/public/kewilayahan/dati4/list-dropdown/{id_kecamatan}"
        
        # fetch all subdistrict/kelurahan
        subdistrict = self.scraper.scrape_region(url)
        return subdistrict
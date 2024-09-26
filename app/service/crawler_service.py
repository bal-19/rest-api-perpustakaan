from fastapi import HTTPException
from typing import List

from helper.scraper import WebScraper

class LibraryCrawlerService:
    def __init__(self):
        self.scraper = WebScraper()

    def fetch_libraries_data(self, jenis: str, provinsi_id: str, kabkota_id: str, kecamatan_id: str, kelurahan_id: str, length: int) -> List[dict]:
        url = "https://data.perpusnas.go.id/public/direktori/list"
        
        try:
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
        
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Internal server error {e}")
        

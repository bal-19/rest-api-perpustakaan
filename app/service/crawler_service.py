from app.helper.scraper import WebScraper

class LibraryCrawlerService:
    def __init__(self):
        self.scraper = WebScraper()

    def fetch_libraries_data(self):
        url = "https://data.perpusnas.go.id/public/direktori/perpustakaan-umum"
        # fetch data using scraper helper
        libraries = self.scraper.scrape_libraries(url)
        return libraries

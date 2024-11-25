import requests

from bs4 import BeautifulSoup
from fastapi import HTTPException
from typing import List


class WebScraper:
    def __init__(self) -> None:
        self.cookies = {
            'ci_session': 'kasghvuv2v4c7f1jdl6gglbqrc843tvg',
        }
        
        self.headers = {
            'accept': 'application/json, text/javascript, */*; q=0.01',
            'accept-language': 'en-US,en;q=0.9',
            'priority': 'u=1, i',
            'referer': 'https://data.perpusnas.go.id/public/direktori/perpustakaan-umum',
            'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
            'sec-ch-ua-arch': '"x86"',
            'sec-ch-ua-bitness': '"64"',
            'sec-ch-ua-full-version': '"130.0.6723.6"',
            'sec-ch-ua-full-version-list': '"Chromium";v="130.0.6723.6", "Google Chrome";v="130.0.6723.6", "Not?A_Brand";v="99.0.0.0"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-model': '""',
            'sec-ch-ua-platform': '"Windows"',
            'sec-ch-ua-platform-version': '"15.0.0"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest',
        }

    def scrape_type(self, url: str) -> List:
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            type_list = list()
            
            options = soup.select("option")
            
            if options:
                for option in options:
                    type_value = option.get("value")
                    type_list.append(type_value)
                return type_list
            
            else:
                raise HTTPException(status_code=404, detail="Not Found")
        else:
            raise HTTPException(status_code=response.status_code, detail=response.reason)
    
    def scrape_region(self, url: str) -> List[dict]:
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            result = response.json()
            return result
            
        else:
            raise HTTPException(status_code=response.status_code, detail=response.reason)
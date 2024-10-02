import requests

from bs4 import BeautifulSoup
from fastapi import HTTPException
from datetime import datetime
from typing import List

from ..model.perpustakaan import PerpustakaanMeta

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
    
    def mapping(self, data: dict) -> PerpustakaanMeta:
        # mapping
        npp = data.get("npp") if data.get("npp") else "-"
        nama = data.get("nama") if data.get("nama") else "-"
        lembaga_induk = data.get("lembaga_induk") if data.get("lembaga_induk") else "-"
        alamat = data.get("alamat") if data.get("alamat") else "-"
        telepon = data.get("telepon") if data.get("telepon") else "-"
        email = data.get("email") if data.get("email") else "-"
        website = data.get("website") if data.get("website") else "-"
        jenis = data.get("jenis") if data.get("jenis").capitalize() else "-"
        sub_jenis = data.get("subjenis") if data.get("subjenis") else "-"
        status_perpus = data.get("status_perpus").capitalize() if data.get("status_perpus") else "-"
        kode_pos = data.get("kode_pos") if data.get("kode_pos") else "-"
        provinsi = data.get("nama_provinsi") if data.get("nama_provinsi") else "-"
        kabkota = data.get("nama_kabkota") if data.get("nama_kabkota") else "-"
        kecamatan = data.get('nama_kecamatan') if data.get("nama_kecamatan") else "-"
        kelurahan = data.get("nama_kelurahan").capitalize() if data.get("nama_kelurahan") else "-"

        # saving to variable
        raw_data = PerpustakaanMeta(
            npp=npp,
            nama=nama,
            lembaga=lembaga_induk,
            alamat=alamat,
            telepon=telepon,
            email=email,
            website=website,
            jenis=jenis,
            subjenis=sub_jenis,
            status_perpustakaan=status_perpus,
            kode_pos=kode_pos,
            provinsi=provinsi,
            kabkota=kabkota,
            kecamatan=kecamatan,
            kelurahan=kelurahan
        )
        
        return raw_data
        
    def scrape_libraries(self, url: str, **kwargs) -> List[dict]:
        current_timestamp = int(datetime.now().timestamp())
        params = {
            'jenis': str(kwargs.get('jenis', '')).upper(),
            'provinsi_id': str(kwargs.get('provinsi_id', '')),
            'kabkota_id': str(kwargs.get('kabkota_id', '')),
            'kecamatan_id': str(kwargs.get('kecamatan_id', '')),
            'kelurahan_id': str(kwargs.get('kelurahan_id', '')),
            'subjenis': '',
            'draw': '0',
            'columns[0][data]': 'id',
            'columns[0][name]': 'id',
            'columns[0][searchable]': 'true',
            'columns[0][orderable]': 'false',
            'columns[0][search][value]': '',
            'columns[0][search][regex]': 'false',
            'columns[1][data]': 'npp',
            'columns[1][name]': '',
            'columns[1][searchable]': 'true',
            'columns[1][orderable]': 'false',
            'columns[1][search][value]': '',
            'columns[1][search][regex]': 'false',
            'columns[2][data]': 'nama',
            'columns[2][name]': '',
            'columns[2][searchable]': 'true',
            'columns[2][orderable]': 'false',
            'columns[2][search][value]': '',
            'columns[2][search][regex]': 'false',
            'columns[3][data]': 'nama_provinsi',
            'columns[3][name]': '',
            'columns[3][searchable]': 'true',
            'columns[3][orderable]': 'false',
            'columns[3][search][value]': '',
            'columns[3][search][regex]': 'false',
            'columns[4][data]': 'nama_kabkota',
            'columns[4][name]': '',
            'columns[4][searchable]': 'true',
            'columns[4][orderable]': 'false',
            'columns[4][search][value]': '',
            'columns[4][search][regex]': 'false',
            'columns[5][data]': 'alamat',
            'columns[5][name]': '',
            'columns[5][searchable]': 'true',
            'columns[5][orderable]': 'false',
            'columns[5][search][value]': '',
            'columns[5][search][regex]': 'false',
            'columns[6][data]': 'telepon',
            'columns[6][name]': '',
            'columns[6][searchable]': 'true',
            'columns[6][orderable]': 'false',
            'columns[6][search][value]': '',
            'columns[6][search][regex]': 'false',
            'start': '0',
            'length': str(kwargs.get('length', '10')),
            'search[value]': '',
            'search[regex]': 'false',
            '_': str(current_timestamp),
        }
        
        response = requests.get(url, params=params, cookies=self.cookies, headers=self.headers)
        
        # Handle if status code != 200
        if response.status_code == 200:
            result = response.json()
            total_data = result.get("recordsTotal")
            library_data = dict(total=total_data, data=list())

            datas = result.get("data")
            
            # scraping logic
            for library in datas:
                data = self.mapping(library)
                library_data.get("data").append(data.__dict__)
            return library_data
            
        else:
            raise HTTPException(status_code=response.status_code, detail=response.reason)
        

    def scrape_type(self, url: str) -> List:
        response = requests.get(url, headers=self.headers)
        
        # Handle if status code != 200
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
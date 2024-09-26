import requests

from fastapi import HTTPException
from datetime import datetime
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
    
    def mapping(self, data: dict) -> dict:
        # mapping
        npp = data.get("npp")
        nama = data.get("nama")
        lembaga_induk = data.get("lembaga_induk")
        alamat = data.get("alamat")
        telepon = data.get("telepon")
        email = data.get("email")
        website = data.get("website")
        jenis = data.get("jenis")
        sub_jenis = data.get("subjenis")
        status_perpus = data.get("status_perpus")
        kode_pos = data.get("kode_pos")
        provinsi = data.get("nama_provinsi")
        kabkota = data.get("nama_kabkota")
        kecamatan = data.get('nama_kecamatan')
        kelurahan = data.get("nama_kelurahan")

        # saving to variable
        raw_data = dict(
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
        if response.status_code == 404:
            raise HTTPException(status_code=404, detail="Page not found")
        elif response.status_code == 403:
            raise HTTPException(status_code=403, detail="Access forbidden")
        elif response.status_code >= 500:
            raise HTTPException(status_code=500, detail="Server error")
        elif response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail="An error occurred")
        
        result = response.json()
        total_data = result.get("recordsTotal")
        library_data = dict(total=total_data, data=list())

        # scraping logic
        for library in result.get("data"):
            data = self.mapping(library)
            library_data.get("data").append(data)

        return library_data

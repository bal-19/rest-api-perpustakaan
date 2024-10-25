# Rest Api Data Perpustakaan

This project aims to build a REST API service using FastAPI that automates the process of data retrieval (scraping) from the national library website. This API allows users to send HTTP requests and receive responses in the form of library data scraped in real-time from web pages. This scraping process is done using libraries such as requests to collect data from dynamic sites.

## Using Docker

clone project using git

```bash
git clone https://github.com/bal-19/rest-api-perpustakaan.git
cd rest-api-perpustakaan
```

build docker image

```bash
sudo docker build -t image-name:tag .
```

run docker image

```bash
sudo docker run -d -p 1919:1919 image-name:tag
```

## Installation

clone project using git

```bash
git clone https://github.com/bal-19/rest-api-perpustakaan.git
cd rest-api-perpustakaan
```

create python virtual environment

```bash
python3 -m venv .venv
```

activate virtual environment

-   Windows

```bash
.venv\Scripts\Activate.ps1
```

-   Linux

```bash
source .venv/bin/activate
```

install project requirements

```bash
pip install -r requirements.txt
```

start project

```bash
python3 main.py
```

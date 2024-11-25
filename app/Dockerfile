FROM python:3.10.14-bookworm

COPY requirements.txt /

WORKDIR /

RUN  pip install -r requirements.txt

RUN ln -fs /usr/share/zoneinfo/Asia/Jakarta /etc/localtime \
    && echo "Asia/Jakarta" > /etc/timezone \
    && dpkg-reconfigure -f noninteractive tzdata

WORKDIR /app

COPY . /app

EXPOSE 8000

ENTRYPOINT ["python", "main.py"]
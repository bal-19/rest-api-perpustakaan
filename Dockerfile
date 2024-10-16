FROM python:3.10.14-bookworm

WORKDIR /app

RUN ln -fs /usr/share/zoneinfo/Asia/Jakarta /etc/localtime \
    && echo "Asia/Jakarta" > /etc/timezone \
    && dpkg-reconfigure -f noninteractive tzdata

COPY . .

RUN python -m venv venv

RUN venv/bin/pip install --no-cache-dir -r requirements.txt

EXPOSE 7700

CMD [ "venv/bin/python", "main.py" ]

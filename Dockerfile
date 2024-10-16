FROM python:3.10.14-bookworm

WORKDIR /

RUN ln -fs /usr/share/zoneinfo/Asia/Jakarta /etc/localtime \
    && echo "Asia/Jakarta" > /etc/timezone \
    && dpkg-reconfigure -f noninteractive tzdata

COPY . /app/

RUN python -m venv venv

RUN . venv/bin/activate && pip install -r requirements.txt

EXPOSE 7700

CMD [ "venv/bin/python", "main.py" ]

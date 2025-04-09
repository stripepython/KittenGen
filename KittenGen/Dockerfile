FROM python:3.12-slim

RUN apt-get update && \
    apt-get install -y --no-install-recommends g++ gcc gdb

WORKDIR /app

COPY . /app/

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 2025

CMD [ "python", "__main__.py"]
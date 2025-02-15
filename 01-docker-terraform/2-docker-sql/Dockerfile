FROM python:3.11


RUN pip install pandas sqlalchemy psycopg2 requests

WORKDIR /app
COPY raw_data_ingest.py raw_data_ingest.py

ENTRYPOINT [ "python", "raw_data_ingest.py" ]
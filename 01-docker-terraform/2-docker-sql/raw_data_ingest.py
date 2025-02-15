
import pandas as pd
import os
from sqlalchemy import create_engine
from time import time
import argparse
import requests



def main(params):

    username = params.user
    password = params.password
    host = params.host
    port = params.port
    dbname = params.db
    table_name = params.table_name
    url = params.url

    if url.endswith('.csv.gz'):
        csv_name = 'output.csv.gz'
    else:
        csv_name = 'output.csv'

    print(f"Downloading {url}...")

    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(csv_name, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    print(f"Downloaded file to {csv_name}")

    engine = create_engine(f'postgresql+psycopg2://{username}:{password}@{host}:{port}/{dbname}')
    engine.connect()

    df_iter = pd.read_csv(csv_name, iterator=True, chunksize=100000)
    
    # We'll read the first chunk to get the schema, then create/replace the table
    df_first_chunk = next(df_iter)
    df_first_chunk.tpep_pickup_datetime = pd.to_datetime(df_first_chunk.tpep_pickup_datetime)
    df_first_chunk.tpep_dropoff_datetime = pd.to_datetime(df_first_chunk.tpep_dropoff_datetime)
    
    # Create table
    df_first_chunk.head(0).to_sql(name=table_name, con=engine, if_exists='replace')

    # Insert first chunk
    t_start = time()
    df_first_chunk.to_sql(name=table_name, con=engine, if_exists='append')
    t_end = time()
    print(f'Inserted the first chunk, took {round(t_end - t_start, 2)} seconds')

    for i, df_chunk in enumerate(df_iter, start=2):
        t_start = time()

        df_chunk.tpep_pickup_datetime = pd.to_datetime(df_chunk.tpep_pickup_datetime)
        df_chunk.tpep_dropoff_datetime = pd.to_datetime(df_chunk.tpep_dropoff_datetime)
        
        df_chunk.to_sql(name=table_name, con=engine, if_exists='append')
        
        t_end = time()  
        print(f'Inserted a new chunk {i} Time taken (in s) -  {round(t_end-t_start,2)}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Ingest CSV data to postgres")

    parser.add_argument('--user', help="user name for postgres")
    parser.add_argument('--password', help="password for postgres")
    parser.add_argument('--host', help="host name for postgres")
    parser.add_argument('--port', help="port number for postgres")
    parser.add_argument('--db', help="database name for postgres")
    parser.add_argument('--table_name', help="name of the table where we will write csv to")
    parser.add_argument('--url', help="url for the csv")

    args = parser.parse_args()
    main(args)

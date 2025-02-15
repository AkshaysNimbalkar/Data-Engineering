{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "54ac6d86-1178-4a86-bae4-71983703945c",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import os"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "f0a4dce3-e6ff-49ee-af67-6cdc36c2c1d1",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'2.0.3'"
      ]
     },
     "execution_count": 33,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "pd.__version__"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "id": "99f9a0df-679d-48f8-b991-f089b588532c",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\aksha\\AppData\\Local\\Temp\\ipykernel_28464\\2836296694.py:1: DtypeWarning: Columns (6) have mixed types. Specify dtype option on import or set low_memory=False.\n",
      "  df = pd.read_csv(\"yellow_tripdata_2021-01.csv\")\n"
     ]
    }
   ],
   "source": [
    "df = pd.read_csv(\"yellow_tripdata_2021-01.csv\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "9d50d90c-3bcf-4274-9c8f-3cbbfd3fa676",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "CREATE TABLE \"yellow_taxi_data\" (\n",
      "\"VendorID\" REAL,\n",
      "  \"tpep_pickup_datetime\" TEXT,\n",
      "  \"tpep_dropoff_datetime\" TEXT,\n",
      "  \"passenger_count\" REAL,\n",
      "  \"trip_distance\" REAL,\n",
      "  \"RatecodeID\" REAL,\n",
      "  \"store_and_fwd_flag\" TEXT,\n",
      "  \"PULocationID\" INTEGER,\n",
      "  \"DOLocationID\" INTEGER,\n",
      "  \"payment_type\" REAL,\n",
      "  \"fare_amount\" REAL,\n",
      "  \"extra\" REAL,\n",
      "  \"mta_tax\" REAL,\n",
      "  \"tip_amount\" REAL,\n",
      "  \"tolls_amount\" REAL,\n",
      "  \"improvement_surcharge\" REAL,\n",
      "  \"total_amount\" REAL,\n",
      "  \"congestion_surcharge\" REAL\n",
      ")\n"
     ]
    }
   ],
   "source": [
    "print(pd.io.sql.get_schema(df, name='yellow_taxi_data'))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "id": "61d711af-e815-43e6-ba6a-e00f9278ae9f",
   "metadata": {},
   "outputs": [],
   "source": [
    "df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)\n",
    "df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)"
   ]
  },
  {
   "cell_type": "raw",
   "id": "a67093f0-c5a2-4128-81c8-f2e5fadacc9c",
   "metadata": {},
   "source": [
    "!pip install sqlalchemy psycopg2-binary"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "id": "f93e30ca-af31-4202-9a5a-9c37eed0cbb0",
   "metadata": {},
   "outputs": [],
   "source": [
    "# to write data to database use sqlalchemy\n",
    "#!pip install sqlalchemy\n",
    "from sqlalchemy import create_engine"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "id": "c1d33279-cba9-4efa-a946-5a54a43d8c0c",
   "metadata": {},
   "outputs": [],
   "source": [
    "username = \"root\"\n",
    "password = \"root\"\n",
    "host = \"localhost\"\n",
    "port = \"5432\"\n",
    "dbname = \"ny_taxi\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "id": "a95c7502-e1ff-4b6e-a21a-9ce8b066c1c5",
   "metadata": {},
   "outputs": [],
   "source": [
    "engine = create_engine(f'postgresql+psycopg2://{username}:{password}@{host}:{port}/{dbname}')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "id": "4c0e9835-5dab-484c-a7d9-d1f1c3e1e898",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<sqlalchemy.engine.base.Connection at 0x2340a0cc490>"
      ]
     },
     "execution_count": 40,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "engine.connect()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "id": "74fc946d-ad8a-447f-90a7-c64d5982aa20",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "CREATE TABLE yellow_taxi_data (\n",
      "\t\"VendorID\" FLOAT(53), \n",
      "\ttpep_pickup_datetime TIMESTAMP WITHOUT TIME ZONE, \n",
      "\ttpep_dropoff_datetime TIMESTAMP WITHOUT TIME ZONE, \n",
      "\tpassenger_count FLOAT(53), \n",
      "\ttrip_distance FLOAT(53), \n",
      "\t\"RatecodeID\" FLOAT(53), \n",
      "\tstore_and_fwd_flag TEXT, \n",
      "\t\"PULocationID\" BIGINT, \n",
      "\t\"DOLocationID\" BIGINT, \n",
      "\tpayment_type FLOAT(53), \n",
      "\tfare_amount FLOAT(53), \n",
      "\textra FLOAT(53), \n",
      "\tmta_tax FLOAT(53), \n",
      "\ttip_amount FLOAT(53), \n",
      "\ttolls_amount FLOAT(53), \n",
      "\timprovement_surcharge FLOAT(53), \n",
      "\ttotal_amount FLOAT(53), \n",
      "\tcongestion_surcharge FLOAT(53)\n",
      ")\n",
      "\n",
      "\n"
     ]
    }
   ],
   "source": [
    "print(pd.io.sql.get_schema(df, name='yellow_taxi_data', con=engine))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "id": "10788e6b-9b11-46f4-843d-65dbafb98738",
   "metadata": {},
   "outputs": [],
   "source": [
    "df_iter = pd.read_csv(\"yellow_tripdata_2021-01.csv\", iterator=True, chunksize=100000)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "id": "1b706384-04e0-447e-86ba-4619bba66f2e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0"
      ]
     },
     "execution_count": 43,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head(n=0).to_sql(name='yellow_taxi_data', con=engine, if_exists='replace')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "id": "bab44148-db06-405e-bfed-6df3b5874154",
   "metadata": {},
   "outputs": [],
   "source": [
    "df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)\n",
    "df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "id": "96437e6e-bb92-4a7a-bcb3-0bad8b8aebf7",
   "metadata": {},
   "outputs": [],
   "source": [
    "from time import time"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "id": "d21da2ca-59fc-48dd-bf58-01a99a174215",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Inserted a new chunk. Time taken (in s) -  14.56\n",
      "Inserted a new chunk. Time taken (in s) -  13.83\n",
      "Inserted a new chunk. Time taken (in s) -  13.51\n",
      "Inserted a new chunk. Time taken (in s) -  14.52\n",
      "Inserted a new chunk. Time taken (in s) -  13.89\n",
      "Inserted a new chunk. Time taken (in s) -  13.84\n",
      "Inserted a new chunk. Time taken (in s) -  14.36\n",
      "Inserted a new chunk. Time taken (in s) -  14.95\n",
      "Inserted a new chunk. Time taken (in s) -  13.4\n",
      "Inserted a new chunk. Time taken (in s) -  13.36\n",
      "Inserted a new chunk. Time taken (in s) -  13.33\n",
      "Inserted a new chunk. Time taken (in s) -  13.19\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\aksha\\AppData\\Local\\Temp\\ipykernel_28464\\904051732.py:1: DtypeWarning: Columns (6) have mixed types. Specify dtype option on import or set low_memory=False.\n",
      "  for df in df_iter:\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Inserted a new chunk. Time taken (in s) -  12.73\n",
      "Inserted a new chunk. Time taken (in s) -  8.01\n"
     ]
    }
   ],
   "source": [
    "for df in df_iter:\n",
    "    t_start = time()\n",
    "    \n",
    "    df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)\n",
    "    df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)\n",
    "    \n",
    "    df.to_sql(name=\"yellow_taxi_data\", con=engine, if_exists='append')\n",
    "    \n",
    "    t_end = time()\n",
    "    \n",
    "    print(f'Inserted a new chunk. Time taken (in s) -  {round(t_end-t_start,2)}')"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}

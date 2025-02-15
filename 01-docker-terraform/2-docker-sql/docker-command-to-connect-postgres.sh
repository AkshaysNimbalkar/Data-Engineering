C:/Users/aksha/Documents/Study/DE_Zoomcamp/Week1


winpty docker run -it \
    -e POSTGRES_USER="root" \
    -e POSTGRES_PASSWORD="root" \
    -e POSTGRES_DB="ny_taxi" \
    -v "/c/Users/aksha/Documents/Study/DE_Zoomcamp/Week1/ny_taxi_postgres_data:/var/lib/postgresql/data" \
    -p 5432:5432 \
    postgres:13
  

install pgcli
pip install pgcli
pip install psycopg[binary,pool]

pgcli --help


command to run created postgres container:
Winpty docker run my-postgres

command to connect to postgres:
winpty pgcli -h localhost -p 5432 -U root -d ny_taxi
pass: root

command to pull docker image of PGADMIN:
Winpty docker pull dpage/pgadmin4


command to connect to Postgres using pgadmin:
winpty docker run -it \
    -e PGADMIN_DEFAULT_EMAIL="admin@admin.com" \
    -e PGADMIN_DEFAULT_PASSWORD="root" \
    -p 8080:80 \
    dpage/pgadmin4


docker network to connect two containers pgadmin and my-postgrs
create docker network:
docker network create pg-network


winpty docker run -it \
    -e POSTGRES_USER="root" \
    -e POSTGRES_PASSWORD="root" \
    -e POSTGRES_DB="ny_taxi" \
    -v "/c/Users/aksha/Documents/Study/DE_Zoomcamp/Week1/ny_taxi_postgres_data:/var/lib/postgresql/data" \
    --network=pg-network \
    --name pg-database \
    -p 5432:5432 postgres


docker container inspect pg-database

docker start pg-database


We will now run the pgAdmin container on another terminal:

Winpty docker run -it \
    -e PGADMIN_DEFAULT_EMAIL="admin@admin.com" \
    -e PGADMIN_DEFAULT_PASSWORD="root" \
    -p 8080:80 \
    --network=pg-network \
    --name pgadmin \
    dpage/pgadmin4   




python Ingest_postgresData_Docker.py \
    --user=root \
    --password=root \
    --host=localhost \
    --port=5432 \
    --db=ny_taxi \
    --table_name=green_taxi_data \
    --url "https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2019-01.csv.gz"



docker build -t taxi_ingest:v001 .

winpty docker run -it \
--network=pg-network \
taxi_ingest:v001 \
    --user=root \
    --password=root \
    --host=pg-database \
    --port=5432 \
    --db=ny_taxi \
    --table_name=green_taxi_data \
    --url "https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2019-01.csv.gz"


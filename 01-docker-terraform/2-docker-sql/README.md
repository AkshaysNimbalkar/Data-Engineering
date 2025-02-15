### Docker Commands to run the Postgres


```
C:/Users/aksha/Documents/Study/2025-DE-Zoomcamp/01-docker-terraform/2-docker-sql
```

#### Command to Run the Posetgres

```bash
winpty docker run -it \
    -e POSTGRES_USER="root" \
    -e POSTGRES_PASSWORD="root" \
    -e POSTGRES_DB="ny_taxi" \
    -v /c/Users/aksha/Documents/Study/2025-DE-Zoomcamp/01-docker-terraform/2-docker-sql/ny_taxi_postgres_data:/var/lib/postgresql/data \
    -p 5432:5432 \
    postgres:13
```

#### command to run pgadmin
```bash
winpty docker run -it \
    -e PGADMIN_DEFAULT_EMAIL="admin@admin.com" \
    -e PGADMIN_DEFAULT_PASSWORD="root" \
    -p 8080:80 \
    dpage/pgadmin4
```

#### create docker network
```bash
docker network create pg-network-25
```

#### docker network to connect two containers pgadmin and postgres
```bash
winpty docker run -it \
    -e POSTGRES_USER="root" \
    -e POSTGRES_PASSWORD="root" \
    -e POSTGRES_DB="ny_taxi" \
    -v C:\\Users\\aksha\\Documents\\Study\\2025-DE-Zoomcamp\\01-docker-terraform\\2-docker-sql\\ny_taxi_postgres_data:/var/lib/postgresql/data \
    --network=pg-network-25 \
    --name=pg-database-25 \
    -p 5432:5432 \
    postgres:13

```

```bash
winpty docker run -it \
    -e PGADMIN_DEFAULT_EMAIL="admin@admin.com" \
    -e PGADMIN_DEFAULT_PASSWORD="root" \
    -p 8080:80 \
    --network=pg-network-25 \
    --name=pgadmin-25 \
    dpage/pgadmin4
```

#### Run Python script locally using argument parser using cmd
```bash
URL="https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/yellow_tripdata_2021-01.csv.gz"

Python raw_data_ingest.py \
    --user=root \
    --password=root \
    --host=localhost \
    --port=5432 \
    --db=ny_taxi \
    --table_name=yellow_taxi_data \
    --url=${URL}
```

#### Dockerize the script and build docker image
```bash
docker build -t taxi_ingest:v001 .
```

#### run the docker Image
```bash

URL="https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/yellow_tripdata_2021-01.csv.gz"

winpty docker run -it \
--network=pg-network-25 \
taxi_ingest:v001 \
    --user=root \
    --password=root \
    --host=pg-database-25 \
    --port=5432 \
    --db=ny_taxi \
    --table_name=yellow_taxi_data \
    --url=${URL}

```

#### Docker Compose to run multiple container using yaml file:


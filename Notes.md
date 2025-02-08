docker run -it `
--name taxi_db `
--network db-network `
-e POSTGRES_DB=testdb `
-e POSTGRES_USER=test `
-e POSTGRES_PASSWORD=test `
-v D:\wip\zoomcamp\de_zoommcamp_2025\module_1\db_data:/var/lib/postgresql/data `
-p 5432:5432 `
postgres:16


docker run -it `
-e PGADMIN_DEFAULT_EMAIL="admin@admin.com" `
-e PGADMIN_DEFAULT_PASSWORD="root" `
-p 8080:80 `
--network db-network `
--name taxi_pg `
dpage/pgadmin4

docker network create db-network
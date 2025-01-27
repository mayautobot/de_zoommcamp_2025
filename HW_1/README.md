# Homework - Module 1

## Question 1. Understanding docker first run
Run following command to:
- Run the container with python:3.12.8 in interactive mode
```
docker run -it --entrypoint=bash python:3.12.8
```
- Get the verion of pip

```
pip --version
```
*Output*:
```
pip 24.3.1 from /usr/local/lib/python3.12/site-packages/pip (python 3.12)
```

## Question 2. Understanding Docker networking and docker-compose

`Answer`

```
db:5432
```

## Question 3. Trip Segmentation Count

`Query`

```
WITH transformed_data AS (
  SELECT
    CASE
    WHEN trip_distance <= 1 THEN "Up to 1 mile"
    WHEN trip_distance > 1 AND trip_distance <= 3 THEN "In between 1 (exclusive) and 3 miles (inclusive)"
    WHEN trip_distance > 3 AND trip_distance <= 7 THEN "In between 3 (exclusive) and 7 miles (inclusive)"
    WHEN trip_distance > 7 AND trip_distance <= 10 THEN "In between 7 (exclusive) and 10 miles (inclusive)"
    WHEN trip_distance > 10 THEN "Over 10 miles"
    END AS trip_distance_buckets,
    lpep_pickup_datetime,
    lpep_dropoff_datetime
  FROM
    `green_tripdata`
  WHERE
    lpep_pickup_datetime >= CAST('2019-10-01 00:00:00 UTC' AS TIMESTAMP) AND lpep_pickup_datetime < CAST('2019-11-01 00:00:00 UTC' AS TIMESTAMP) AND lpep_dropoff_datetime < CAST('2019-11-01 00:00:00 UTC' AS TIMESTAMP)
)
SELECT
  trip_distance_buckets , COUNT(1) AS count_of_trips
FROM transformed_data
GROUP BY trip_distance_buckets
```

`Answer`

```
104,802; 198,924; 109,603; 27,678; 35,189
```

## Question 4. Longest trip for each day

`Query`

```
SELECT
  lpep_pickup_datetime,
  trip_distance
FROM
  `green_tripdata`
WHERE
  trip_distance = (
  SELECT
    MAX(trip_distance)
  FROM
    `green_tripdata`)
```

`Answer`

```
2019-10-31
```

## Question 5. Three biggest pickup zones

`Query`

```
WITH
  transformed_data AS (
  SELECT
    PULocationID,
    SUM(total_amount) AS total_amount_by_pickup_location
  FROM
    `green_tripdata`
  WHERE
    CAST(lpep_pickup_datetime AS DATE) = CAST('2019-10-18' AS DATE)
  GROUP BY
    PULocationID
  ORDER BY
    2 DESC )
SELECT
  transformed_data.*,
  tz.Zone
FROM
  transformed_data
LEFT JOIN
  `taxi_zone_lookup` tz
ON
  tz.LocationID = transformed_data.PULocationID
WHERE
  transformed_data.total_amount_by_pickup_location >= 13000
ORDER BY
  transformed_data.total_amount_by_pickup_location DESC
```

`Answer`

```
East Harlem North, East Harlem South, Morningside Heights
```

## Question 6. Largest tip

`Query`

```
SELECT
  tripdata.PULocationID,
  tripdata.DOLocationID,
  tripdata.lpep_pickup_datetime,
  tripdata.tip_amount,
  pickup_lookup.Zone AS pickup_zone,
  drop_lookup.Zone AS drop_zone,
FROM
  `green_tripdata` AS tripdata
LEFT JOIN
  `taxi_zone_lookup` AS pickup_lookup
ON
  pickup_lookup.LocationID = tripdata.PULocationID
LEFT JOIN
  `taxi_zone_lookup` AS drop_lookup
ON
  drop_lookup.LocationID = tripdata.DOLocationID
WHERE
  CAST(lpep_pickup_datetime AS DATE) BETWEEN CAST('2019-10-01' AS DATE)
  AND CAST('2019-10-31' AS DATE)
  AND pickup_lookup.Zone = 'East Harlem North'
ORDER BY
  4 DESC
```

`Answer`

```
JFK Airport
```

## Question 7. Terraform Workflow

`Answer`

```
terraform init, terraform apply -auto-approve, terraform destroy
```
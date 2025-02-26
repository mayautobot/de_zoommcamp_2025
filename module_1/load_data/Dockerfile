FROM python:3.10

WORKDIR /test/app

ADD https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2019-10.csv.gz data/
RUN gzip -d data/green_tripdata_2019-10.csv.gz
ADD https://github.com/DataTalksClub/nyc-tlc-data/releases/download/misc/taxi_zone_lookup.csv data/

COPY requirements.txt load_data.py .

RUN pip install -r requirements.txt
RUN python load_data.py

CMD ["bash"]
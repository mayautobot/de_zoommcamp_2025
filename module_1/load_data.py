import pandas as pd
from datetime import datetime
from sqlalchemy import create_engine, URL

def load_data():
    data_df_iter = pd.read_csv('green_tripdata_2019-10.csv', iterator=True, chunksize=100000)


    db_url = URL.create(
        drivername='postgresql',
        username='test',
        password='test',
        host='localhost',
        port=5432,
        database='testdb'
    )
    db_engine = create_engine(db_url)

    first_insert_flag = 0

    for data_df in data_df_iter:
        data_df.lpep_pickup_datetime = pd.to_datetime(data_df.lpep_pickup_datetime , format="%Y-%m-%d %H:%M:%S")
        data_df.lpep_dropoff_datetime = pd.to_datetime(data_df.lpep_dropoff_datetime , format="%Y-%m-%d %H:%M:%S")

        if first_insert_flag == 0:
            data_df.head(0).to_sql(name='taxi_data', con=db_engine, if_exists='replace')
            first_insert_flag = 1

        data_df.to_sql(name='taxi_data', con=db_engine, if_exists='append')

        print(f"Inserted chunck with shape: {data_df.shape}")

if __name__ == '__main__':
    load_data()
from datetime import datetime, timedelta
from os import sep
from airflow import DAG
import config as config
from datetime import date
from airflow.models import DAG
from airflow.utils.dates import days_ago
import awswrangler as wr
from airflow.operators.python_operator import PythonOperator
import pandas as pd
from io import StringIO  # python3; python2: BytesIO
import boto3

## import s3fs

######################################################################
#
#                     Extration Data from S3 2009
######################################################################


def extract_load_data2009():
    print(f"Getting data from {config.BUCKET_RAW}...")
    raw_path2009 = f"s3://{config.BUCKET_RAW}/raw/2009.csv"
    raw_df2009 = wr.s3.read_csv(path=raw_path2009)
    print(raw_df2009)

    print(f"Writing data to {config.DB_NAME}...")

    ######################################################################
    #                          Tranformation data 2009
    #     calcular promedio del tiempo de salida por dia por aeropuerto
    ######################################################################
    #    raw_ave_delay = raw_df['DEP_DELAY'], raw_df['ORIGIN'], raw_df['FL_DATE']
    raw_ave_delay2009 = raw_df2009.groupby(["ORIGIN", "FL_DATE"])["DEP_DELAY"].mean()
    print(f"The average delay by airport for day is")
    print(raw_ave_delay2009)

    ######################################################################
    #              Load data to Postgres 2009
    #               insersion en la DB
    ######################################################################
    raw_ave_delay2009.to_sql(
        name=config.TBL_NAME2009,
        con=config.engine,
        schema="public",
        if_exists="replace",
        index=True,
    )
    print(f"Data written to {config.DB_NAME}")

    ######################################################################
    #              Guardado en S3 como csv 2009
    #
    ######################################################################

    path_out2009 = f"s3://{config.BUCKET_RAW}/raw-out/2009.csv"
    wr.s3.to_csv(
        df=raw_ave_delay2009,
        path=path_out2009,
        sep=",",
        index=True,
    )

    print(f"Data written to {config.BUCKET_RAW}/{path_out2009}")


######################################################################
#
#                     Extration Data from S3 2010
######################################################################


def extract_load_data2010():
    print(f"Getting data from {config.BUCKET_RAW}...")
    raw_path2010 = f"s3://{config.BUCKET_RAW}/raw/2010.csv"
    raw_df2010 = wr.s3.read_csv(path=raw_path2010)
    print(raw_df2010)

    print(f"Writing data to {config.DB_NAME}...")

    ######################################################################
    #                          Tranformation data 2010
    #     calcular promedio del tiempo de salida por dia por aeropuerto
    ######################################################################
    #    raw_ave_delay = raw_df['DEP_DELAY'], raw_df['ORIGIN'], raw_df['FL_DATE']
    raw_ave_delay2010 = raw_df2010.groupby(["ORIGIN", "FL_DATE"])["DEP_DELAY"].mean()
    print(f"The average delay by airport for day is")
    print(raw_ave_delay2010)

    ######################################################################
    #              Load data to Postgres 2010
    #               insersion en la DB
    ######################################################################
    raw_ave_delay2010.to_sql(
        name=config.TBL_NAME2010,
        con=config.engine,
        schema="public",
        if_exists="replace",
        index=True,
    )
    print(f"Data written to {config.DB_NAME}")

    ######################################################################
    #              Guardado en S3 como csv 2010
    #
    ######################################################################

    path_out2010 = f"s3://{config.BUCKET_RAW}/raw-out/2010.csv"
    wr.s3.to_csv(
        df=raw_ave_delay2010,
        path=path_out2010,
        sep=",",
        index=True,
    )

    print(f"Data written to {config.BUCKET_RAW}/{path_out2010}")


######################################################################
#
#                     Extration Data from S3 2011
######################################################################


def extract_load_data2011():
    print(f"Getting data from {config.BUCKET_RAW}...")
    raw_path2011 = f"s3://{config.BUCKET_RAW}/raw/2011.csv"
    raw_df2011 = wr.s3.read_csv(path=raw_path2011)
    print(raw_df2011)

    print(f"Writing data to {config.DB_NAME}...")

    ######################################################################
    #                          Tranformation data 2011
    #     calcular promedio del tiempo de salida por dia por aeropuerto
    ######################################################################
    #    raw_ave_delay = raw_df['DEP_DELAY'], raw_df['ORIGIN'], raw_df['FL_DATE']
    raw_ave_delay2011 = raw_df2011.groupby(["ORIGIN", "FL_DATE"])["DEP_DELAY"].mean()
    print(f"The average delay by airport for day is")
    print(raw_ave_delay2011)

    ######################################################################
    #              Load data to Postgres 2011
    #               insersion en la DB
    ######################################################################
    raw_ave_delay2011.to_sql(
        name=config.TBL_NAME2011,
        con=config.engine,
        schema="public",
        if_exists="replace",
        index=True,
    )
    print(f"Data written to {config.DB_NAME}")

    ######################################################################
    #              Guardado en S3 como csv 2011
    #
    ######################################################################

    path_out2011 = f"s3://{config.BUCKET_RAW}/raw-out/2011.csv"
    wr.s3.to_csv(
        df=raw_ave_delay2011,
        path=path_out2011,
        sep=",",
        index=True,
    )

    print(f"Data written to {config.BUCKET_RAW}/{path_out2011}")


######################################################################
#
#                     Extration Data from S3 2012
######################################################################


def extract_load_data2012():
    print(f"Getting data from {config.BUCKET_RAW}...")
    raw_path2012 = f"s3://{config.BUCKET_RAW}/raw/2012.csv"
    raw_df2012 = wr.s3.read_csv(path=raw_path2012)
    print(raw_df2012)

    print(f"Writing data to {config.DB_NAME}...")

    ######################################################################
    #                          Tranformation data 2012
    #     calcular promedio del tiempo de salida por dia por aeropuerto
    ######################################################################
    #    raw_ave_delay = raw_df['DEP_DELAY'], raw_df['ORIGIN'], raw_df['FL_DATE']
    raw_ave_delay2012 = raw_df2012.groupby(["ORIGIN", "FL_DATE"])["DEP_DELAY"].mean()
    print(f"The average delay by airport for day is")
    print(raw_ave_delay2012)

    ######################################################################
    #              Load data to Postgres 2012
    #               insersion en la DB
    ######################################################################
    raw_ave_delay2012.to_sql(
        name=config.TBL_NAME2012,
        con=config.engine,
        schema="public",
        if_exists="replace",
        index=True,
    )
    print(f"Data written to {config.DB_NAME}")

    ######################################################################
    #              Guardado en S3 como csv 2012
    #
    ######################################################################

    path_out2012 = f"s3://{config.BUCKET_RAW}/raw-out/2012.csv"
    wr.s3.to_csv(
        df=raw_ave_delay2012,
        path=path_out2012,
        sep=",",
        index=True,
    )

    print(f"Data written to {config.BUCKET_RAW}/{path_out2012}")


######################################################################
#
#                     Extration Data from S3 2013
######################################################################


def extract_load_data2013():
    print(f"Getting data from {config.BUCKET_RAW}...")
    raw_path2013 = f"s3://{config.BUCKET_RAW}/raw/2013.csv"
    raw_df2013 = wr.s3.read_csv(path=raw_path2013)
    print(raw_df2013)

    print(f"Writing data to {config.DB_NAME}...")

    ######################################################################
    #                          Tranformation data 2013
    #     calcular promedio del tiempo de salida por dia por aeropuerto
    ######################################################################
    #    raw_ave_delay = raw_df['DEP_DELAY'], raw_df['ORIGIN'], raw_df['FL_DATE']
    raw_ave_delay2013 = raw_df2013.groupby(["ORIGIN", "FL_DATE"])["DEP_DELAY"].mean()
    print(f"The average delay by airport for day is")
    print(raw_ave_delay2013)

    ######################################################################
    #              Load data to Postgres 2013
    #               insersion en la DB
    ######################################################################
    raw_ave_delay2013.to_sql(
        name=config.TBL_NAME2013,
        con=config.engine,
        schema="public",
        if_exists="replace",
        index=True,
    )
    print(f"Data written to {config.DB_NAME}")

    ######################################################################
    #              Guardado en S3 como csv 2013
    #
    ######################################################################

    path_out2013 = f"s3://{config.BUCKET_RAW}/raw-out/2013.csv"
    wr.s3.to_csv(
        df=raw_ave_delay2013,
        path=path_out2013,
        sep=",",
        index=True,
    )

    print(f"Data written to {config.BUCKET_RAW}/{path_out2013}")


######################################################################
#
#                     Extration Data from S3 2014
######################################################################


def extract_load_data2014():
    print(f"Getting data from {config.BUCKET_RAW}...")
    raw_path2014 = f"s3://{config.BUCKET_RAW}/raw/2014.csv"
    raw_df2014 = wr.s3.read_csv(path=raw_path2014)
    print(raw_df2014)

    print(f"Writing data to {config.DB_NAME}...")

    ######################################################################
    #                          Tranformation data 2014
    #     calcular promedio del tiempo de salida por dia por aeropuerto
    ######################################################################
    #    raw_ave_delay = raw_df['DEP_DELAY'], raw_df['ORIGIN'], raw_df['FL_DATE']
    raw_ave_delay2014 = raw_df2014.groupby(["ORIGIN", "FL_DATE"])["DEP_DELAY"].mean()
    print(f"The average delay by airport for day is")
    print(raw_ave_delay2014)

    ######################################################################
    #              Load data to Postgres 2014
    #               insersion en la DB
    ######################################################################
    raw_ave_delay2014.to_sql(
        name=config.TBL_NAME2014,
        con=config.engine,
        schema="public",
        if_exists="replace",
        index=True,
    )
    print(f"Data written to {config.DB_NAME}")

    ######################################################################
    #              Guardado en S3 como csv 2014
    #
    ######################################################################

    path_out2014 = f"s3://{config.BUCKET_RAW}/raw-out/2014.csv"
    wr.s3.to_csv(
        df=raw_ave_delay2014,
        path=path_out2014,
        sep=",",
        index=True,
    )

    print(f"Data written to {config.BUCKET_RAW}/{path_out2014}")


######################################################################
#
#                     Extration Data from S3 2015
######################################################################


def extract_load_data2015():
    print(f"Getting data from {config.BUCKET_RAW}...")
    raw_path2015 = f"s3://{config.BUCKET_RAW}/raw/2015.csv"
    raw_df2015 = wr.s3.read_csv(path=raw_path2015)
    print(raw_df2015)

    print(f"Writing data to {config.DB_NAME}...")

    ######################################################################
    #                          Tranformation data 2015
    #     calcular promedio del tiempo de salida por dia por aeropuerto
    ######################################################################
    #    raw_ave_delay = raw_df['DEP_DELAY'], raw_df['ORIGIN'], raw_df['FL_DATE']
    raw_ave_delay2015 = raw_df2015.groupby(["ORIGIN", "FL_DATE"])["DEP_DELAY"].mean()
    print(f"The average delay by airport for day is")
    print(raw_ave_delay2015)

    ######################################################################
    #              Load data to Postgres 2015
    #               insersion en la DB
    ######################################################################
    raw_ave_delay2015.to_sql(
        name=config.TBL_NAME2015,
        con=config.engine,
        schema="public",
        if_exists="replace",
        index=True,
    )
    print(f"Data written to {config.DB_NAME}")

    ######################################################################
    #              Guardado en S3 como csv 2015
    #
    ######################################################################

    path_out2015 = f"s3://{config.BUCKET_RAW}/raw-out/2015.csv"
    wr.s3.to_csv(
        df=raw_ave_delay2015,
        path=path_out2015,
        sep=",",
        index=True,
    )

    print(f"Data written to {config.BUCKET_RAW}/{path_out2015}")


######################################################################
#
#                     Extration Data from S3 2016
######################################################################


def extract_load_data2016():
    print(f"Getting data from {config.BUCKET_RAW}...")
    raw_path2016 = f"s3://{config.BUCKET_RAW}/raw/2016.csv"
    raw_df2016 = wr.s3.read_csv(path=raw_path2016)
    print(raw_df2016)

    print(f"Writing data to {config.DB_NAME}...")

    ######################################################################
    #                          Tranformation data 2016
    #     calcular promedio del tiempo de salida por dia por aeropuerto
    ######################################################################
    #    raw_ave_delay = raw_df['DEP_DELAY'], raw_df['ORIGIN'], raw_df['FL_DATE']
    raw_ave_delay2016 = raw_df2016.groupby(["ORIGIN", "FL_DATE"])["DEP_DELAY"].mean()
    print(f"The average delay by airport for day is")
    print(raw_ave_delay2016)

    ######################################################################
    #              Load data to Postgres 2016
    #               insersion en la DB
    ######################################################################
    raw_ave_delay2016.to_sql(
        name=config.TBL_NAME2016,
        con=config.engine,
        schema="public",
        if_exists="replace",
        index=True,
    )
    print(f"Data written to {config.DB_NAME}")

    ######################################################################
    #              Guardado en S3 como csv 2016
    #
    ######################################################################

    path_out2016 = f"s3://{config.BUCKET_RAW}/raw-out/2016.csv"
    wr.s3.to_csv(
        df=raw_ave_delay2016,
        path=path_out2016,
        sep=",",
        index=True,
    )

    print(f"Data written to {config.BUCKET_RAW}/{path_out2016}")


######################################################################
#
#                     Extration Data from S3 2017
######################################################################


def extract_load_data2017():
    print(f"Getting data from {config.BUCKET_RAW}...")
    raw_path2017 = f"s3://{config.BUCKET_RAW}/raw/2017.csv"
    raw_df2017 = wr.s3.read_csv(path=raw_path2017)
    print(raw_df2017)

    print(f"Writing data to {config.DB_NAME}...")

    ######################################################################
    #                          Tranformation data 2017
    #     calcular promedio del tiempo de salida por dia por aeropuerto
    ######################################################################
    #    raw_ave_delay = raw_df['DEP_DELAY'], raw_df['ORIGIN'], raw_df['FL_DATE']
    raw_ave_delay2017 = raw_df2017.groupby(["ORIGIN", "FL_DATE"])["DEP_DELAY"].mean()
    print(f"The average delay by airport for day is")
    print(raw_ave_delay2017)

    ######################################################################
    #              Load data to Postgres 2017
    #               insersion en la DB
    ######################################################################
    raw_ave_delay2017.to_sql(
        name=config.TBL_NAME2017,
        con=config.engine,
        schema="public",
        if_exists="replace",
        index=True,
    )
    print(f"Data written to {config.DB_NAME}")

    ######################################################################
    #              Guardado en S3 como csv 2017
    #
    ######################################################################

    path_out2017 = f"s3://{config.BUCKET_RAW}/raw-out/2017.csv"
    wr.s3.to_csv(
        df=raw_ave_delay2017,
        path=path_out2017,
        sep=",",
        index=True,
    )

    print(f"Data written to {config.BUCKET_RAW}/{path_out2017}")


######################################################################
#
#                     Extration Data from S3 2018
######################################################################


def extract_load_data2018():
    print(f"Getting data from {config.BUCKET_RAW}...")
    raw_path2018 = f"s3://{config.BUCKET_RAW}/raw/2018.csv"
    raw_df2018 = wr.s3.read_csv(path=raw_path2018)
    print(raw_df2018)

    print(f"Writing data to {config.DB_NAME}...")

    ######################################################################
    #                          Tranformation data 2018
    #     calcular promedio del tiempo de salida por dia por aeropuerto
    ######################################################################
    #    raw_ave_delay = raw_df['DEP_DELAY'], raw_df['ORIGIN'], raw_df['FL_DATE']
    raw_ave_delay2018 = raw_df2018.groupby(["ORIGIN", "FL_DATE"])["DEP_DELAY"].mean()
    print(f"The average delay by airport for day is")
    print(raw_ave_delay2018)

    ######################################################################
    #              Load data to Postgres 2018
    #               insersion en la DB
    ######################################################################
    raw_ave_delay2018.to_sql(
        name=config.TBL_NAME2018,
        con=config.engine,
        schema="public",
        if_exists="replace",
        index=True,
    )
    print(f"Data written to {config.DB_NAME}")

    ######################################################################
    #              Guardado en S3 como csv 2018
    #
    ######################################################################

    path_out2018 = f"s3://{config.BUCKET_RAW}/raw-out/2018.csv"
    wr.s3.to_csv(
        df=raw_ave_delay2018,
        path=path_out2018,
        sep=",",
        index=True,
    )

    print(f"Data written to {config.BUCKET_RAW}/{path_out2018}")


DAG_DEFAULT_ARGS = {
    "owner": "MG",
    "depends_on_past": False,
    "start_date": datetime.utcnow(),
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

with DAG(
    "extract_load_data",
    default_args=DAG_DEFAULT_ARGS,
    schedule_interval="@yearly",
    catchup=False,
) as dag:

    from_s3_to_postgres2009 = PythonOperator(
        task_id="extract_load_data2009", python_callable=extract_load_data2009
    )
    from_s3_to_postgres2010 = PythonOperator(
        task_id="extract_load_data2010", python_callable=extract_load_data2010
    )
    from_s3_to_postgres2011 = PythonOperator(
        task_id="extract_load_data2011", python_callable=extract_load_data2011
    )
    from_s3_to_postgres2012 = PythonOperator(
        task_id="extract_load_data2012", python_callable=extract_load_data2012
    )
    from_s3_to_postgres2013 = PythonOperator(
        task_id="extract_load_data2013", python_callable=extract_load_data2013
    )
    from_s3_to_postgres2014 = PythonOperator(
        task_id="extract_load_data2014", python_callable=extract_load_data2014
    )
    from_s3_to_postgres2015 = PythonOperator(
        task_id="extract_load_data2015", python_callable=extract_load_data2015
    )
    from_s3_to_postgres2016 = PythonOperator(
        task_id="extract_load_data2016", python_callable=extract_load_data2016
    )
    from_s3_to_postgres2017 = PythonOperator(
        task_id="extract_load_data2017", python_callable=extract_load_data2017
    )
    from_s3_to_postgres2018 = PythonOperator(
        task_id="extract_load_data2018", python_callable=extract_load_data2018
    )

    (
        from_s3_to_postgres2009
        >> from_s3_to_postgres2010
        >> from_s3_to_postgres2011
        >> from_s3_to_postgres2012
        >> from_s3_to_postgres2013
        >> from_s3_to_postgres2014
        >> from_s3_to_postgres2015
        >> from_s3_to_postgres2016
        >> from_s3_to_postgres2017
        >> from_s3_to_postgres2018
    )

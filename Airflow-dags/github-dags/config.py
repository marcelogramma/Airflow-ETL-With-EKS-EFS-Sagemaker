import sqlalchemy.exc
import psycopg2
from sqlalchemy import create_engine

DB_USER = "postgres"
DB_PASS = "postgres"
IP = "ml-rds-postgres.cjbnjbp2plfh.us-east-1.rds.amazonaws.com"
DB_PORT = "5432"
DB_NAME = "ml-rds-postgresfrom-s3"
DB_NAME_BASE = "postgres"
TBL_NAME2009 = "ml_table_from_s32009"
TBL_NAME2010 = "ml_table_from_s32010"
TBL_NAME2011 = "ml_table_from_s32011"
TBL_NAME2012 = "ml_table_from_s32012"
TBL_NAME2013 = "ml_table_from_s32013"
TBL_NAME2014 = "ml_table_from_s32014"
TBL_NAME2015 = "ml_table_from_s32015"
TBL_NAME2016 = "ml_table_from_s32016"
TBL_NAME2017 = "ml_table_from_s32017"
TBL_NAME2018 = "ml_table_from_s32018"
BUCKET_RAW = "ml-dataset-raw-s3"
## conn_db = "postgresql://{DB_USER}:{DB_PASS}@{IP}:{DB_PORT}/{DB_NAME_BASE}"
engine = create_engine(f"postgresql://{DB_USER}:{DB_PASS}@{IP}:{DB_PORT}/{DB_NAME}")
engine2 = create_engine(
    f"postgresql://{DB_USER}:{DB_PASS}@{IP}:{DB_PORT}/{DB_NAME_BASE}"
)

## engine_pg8000 = create_engine(f"postgresql+pg8000://{DB_USER}:{DB_PASS}@{IP}:{DB_PORT}/{DB_NAME}")

if __name__ == "__main__":
    ()
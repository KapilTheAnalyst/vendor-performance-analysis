import pandas as pd
import os 
from sqlalchemy import create_engine
import logging

logging.basicConfig(
    filename ="logs/ingestion_db.log",
    level = logging.DEBUG,
    format="%(asctime)s - %(levelname)s -%(message)s",
    filemode="a"
)
engine = create_engine('sqlite:///inventory.db')
def ingest_df(df , table_name , engine):
    ''' This function insert a data into a database '''
    df.to_sql(table_name, con = engine , if_exists = 'replace' , index = False )
def load_raw_data():
    ''' This function helps to insert file in the  data base by iterate a for loop for file on  ingest function'''
    start = time.time()
    for file in os.listdir('data'):
        if'.csv' in file:
            df = pd.read_csv('data/'+file)
            logging.info(f'Ingesting {file} in db')
            ingest_df(df,file[:-4],engine)
    end = time.time()
    total_time = (end-start0/60
    logiing.info('---------------Ingestion complete--------------')
    logging.info(f"\nTotal time taken: {total_time} minutes')

if __name__ == '__main__':
    load_raw_data()
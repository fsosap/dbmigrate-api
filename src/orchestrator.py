from src import file_handler as handler
from src import db_operations as dbops
from src import orchestrator
from src import loader 
import os

def ingest_data():
    # check if the files are available on landing zone
    files_path = "landingzone/"
    file_list = os.listdir(files_path)
    # only select .csv files to upload to db
    file_list = handler.filter_file_list(file_list, '.csv')

    for file_name in file_list:
        if file_name:
            df = loader.read_from_csv(files_path + file_name)
            table_name = file_name.split('.')[0]

            # load df to sqlite
            dbops.write_table_from_df(table_name, df)
            print(f"Sucessful upload of {file_name} table to sqlite!")
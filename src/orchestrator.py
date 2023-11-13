from src import file_handler as handler
from src import db_operations as dbops

import pandas as pd
import os

HEADERS = {
    'hired_employees': ['id', 'name', 'datetime', 'department_id', 'job_id'],
    'departments': ['id', 'department'],
    'jobs': ['id', 'job']
}

def ingest_data():
    # check if the files are available on landing zone
    files_path = "landingzone/"
    file_list = os.listdir(files_path)
    # only select .csv files to upload to db
    file_list = handler.filter_file_list(file_list, '.csv')

    for file_name in file_list:
        if file_name:
            table_name = file_name.split('.')[0]
            df = pd.read_csv(filepath_or_buffer = files_path + file_name,\
                                       names = HEADERS[table_name])
            # load df to sqlite
            dbops.write_table_from_df(table_name, df)
            print(f"Sucessful upload of {file_name} table to sqlite!")

def query_head(table_name: str) -> None:
    query = f'SELECT * FROM {table_name} LIMIT 10'
    html_code = dbops.execute_sql_query(query).to_html(header=True, index=False)
    with open(file = f'templates/preview/{table_name}.html', mode="w") as fp:
        fp.write(html_code)
    fp.close()

def check_db() -> bool:
    try:
        table_list = dbops.execute_sql_query("SELECT name FROM sqlite_master WHERE type='table';")
        if len(table_list.index) == 3:
            return True
    except pd.errors.DatabaseError:
        return False
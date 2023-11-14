import pandas as pd
import sqlite3

def write_table_from_df(table_name:str, df:pd.DataFrame):
    conn = sqlite3.connect('db/HR_Admin.sqlite')
    df.to_sql(table_name, conn, if_exists='replace', index=False)
    conn.close()

def execute_sql_query(query:str) -> pd.DataFrame:
    conn = sqlite3.connect('db/HR_Admin.sqlite')
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df

def execute_sql_file(query_path:str) -> pd.DataFrame:
    conn = sqlite3.connect('db/HR_Admin.sqlite')
    
    with open(query_path, 'r') as query:
        df = pd.read_sql_query(query.read(), conn)

    query.close()
    conn.close()

    return df
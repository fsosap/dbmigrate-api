import pandas as pd

def read_from_csv(file_path: str, names: []) -> pd.DataFrame:
    return pd.read_csv(filepath_or_buffer = file_path, delimiter=',', names = names)
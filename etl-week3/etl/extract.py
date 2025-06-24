import pandas as pd

def fetch_data(file) -> pd.DataFrame:
    data = pd.read_csv(file)
    #data = pd.DataFrame()
    return data
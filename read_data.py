import pandas as pd
from db import get_engine

def read_machines():
    engine = get_engine()
    return pd.read_sql("SELECT * FROM machines", engine)

def read_mesures():
    engine = get_engine()
    return pd.read_sql("SELECT * FROM mesures", engine)
import os
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv

def load_data(df: pd.DataFrame, table_name: str):
    print(f"Load: Пишем в таблицу {table_name}...")
    load_dotenv()
    
    db_url = f"postgresql+psycopg2://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
    
    engine = create_engine(db_url)
    df.to_sql(name=table_name, con=engine, if_exists="replace", index=False)
    print("Load: Готово")
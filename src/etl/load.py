import os
import pandas as pd
from pathlib import Path
from sqlalchemy import create_engine
from dotenv import load_dotenv

def load_data(df: pd.DataFrame, table_name: str):
    print(f"Load: Пишем в таблицу {table_name}...")
    

    env_path = Path(__file__).resolve().parents[2] / ".env"
    load_dotenv(dotenv_path=env_path)
    
    db_host = os.getenv("DB_HOST")
    db_port = os.getenv("DB_PORT")
    db_name = os.getenv("DB_NAME")
    db_user = os.getenv("DB_USER")
    db_password = os.getenv("DB_PASSWORD")
    
    if not all([db_host, db_port, db_name, db_user, db_password]):
        raise ValueError("Не хватает переменных окружения для БД. Проверьте .env")
        
    db_url = f"postgresql+psycopg2://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
    engine = create_engine(db_url)
    
    df.to_sql(name=table_name, con=engine, if_exists="replace", index=False)
    print("Load: Успешно!")
import sys
import os
from dotenv import load_dotenv
import pandas as pd
from sqlalchemy import create_engine
from pathlib import Path

load_dotenv(dotenv_path=Path(__file__).resolve().parent.parent / ".env")

host = os.getenv("DB_HOST")
port = os.getenv("DB_PORT")
db = os.getenv("DB_NAME")
user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")

if not all([host, port, db, user, password]):
    print("Ошибка: не все переменные найдены в .env")
    sys.exit(1)

df = pd.read_csv(file_path, sep=';', encoding='utf-8-sig')
    
    
first_col = df.columns[0]
if "Длина волны" not in first_col:
    raise ValueError(f"Ожидался столбец 'Длина волны', но найден: '{first_col}'")
    
df = df.rename(columns={first_col: "wavelength_nm"})

df_100 = df.head(100)


conn_str = f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{db}"
engine = create_engine(conn_str)


table_name = "maltsevama"


print(f"Попытка записи {len(df_100)} строк в таблицу {table_name}...")

try:
    df_100.to_sql(
        name=table_name,
        con=engine,
        if_exists="replace",
        index=False
    )
    print(f"Готово, строк: {len(df_100)}. Колонок: {len(df_100.columns)}")
except Exception as e:
    print(f"Ошибка при записи: {e}")
    sys.exit(1)
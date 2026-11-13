import pandas as pd
from sqlalchemy import create_engine


host = "85.193.80.59"
port = "5432"
db = "homeworks"
user = "deexpert"
password = "what_a_Wonderful_Day!" 


df = pd.read_csv("спектры.csv", sep=';', encoding='utf-8-sig')
df = df.rename(columns={df.columns[0]: "wavelength_nm"})
df_100 = df.head(100)


conn_str = f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{db}"


engine = create_engine(conn_str)


table_name = "maltsevama"


df_100.to_sql(
    name=table_name,
    con=engine,
    if_exists="replace",
    index=False
)

print("Готово")
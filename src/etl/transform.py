import pandas as pd

def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    print("Transform: Обрабатываем данные...")
    df = df.rename(columns={df.columns[0]: "wavelength_nm"})
    return df.head(100).copy()
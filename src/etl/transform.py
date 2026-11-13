import pandas as pd

def transform_data(df: pd.DataFrame, max_rows: int = 100) -> pd.DataFrame:
    print("Transform: Обрабатываем данные...")
    
    first_col = df.columns[0]
    if "Длина волны" not in first_col:
        raise ValueError(f"Ожидался столбец 'Длина волны', но найден: '{first_col}'")
        
    df = df.rename(columns={first_col: "wavelength_nm"})
    return df.head(max_rows).copy()
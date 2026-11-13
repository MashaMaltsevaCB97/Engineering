import pandas as pd
from pathlib import Path


def read_data(file_path, sep=';', encoding='utf-8-sig'):
    """Загружает данные спектров из файла."""
    try:
        df = pd.read_csv(file_path, sep=sep, encoding=encoding)
        return df.rename(columns={df.columns[0]: "Длина волны, нм"})
    except FileNotFoundError:
        print(f"Ошибка: Файл {file_path} не найден.")
        return None

def fix_types(df):
    for col in df.columns:
        try:
            df[col] = pd.to_numeric(df[col])
        except ValueError:
            pass
    return df 

if __name__ == '__main__':
    file_name = Path(__file__).parent / 'спектры.csv'
    
    data = read_data(file_name)
    
    if data is not None:
        data = fix_types(data)
        
        print("Вот первые 10 строк:")
        print(data.head(10))
        
        save_path = Path(__file__).parent / 'spectra.parquet'
        data.to_parquet(save_path)
        print(f"Данные сохранены в {save_path.name}")
import pandas as pd
from pathlib import Path


def read_spectra(file_path, sep=';', encoding='utf-8-sig'):
    """Загружает данные спектров из файла."""
    try:
        df = pd.read_csv(file_path, sep=sep, encoding=encoding)
        return df.rename(columns={df.columns[0]: "Длина волны, нм"})
    except FileNotFoundError:
        print(f"Ошибка: Файл {file_path} не найден.")
        return df


def clean_spectra(df):
    
    df_clean = df.copy()

    for col in df.columns:
        try:
            df[col] = pd.to_numeric(df[col])
        except ValueError:
            print(f"Столбец {col} оставлен как есть")

    return df_clean 


if __name__ == '__main__':
    file_name = Path(__file__).parent / 'спектры.csv'

    try:
        data = read_spectra(file_name)
        
        data = clean_spectra(data)
        print("первые 10 строк:")
        print(data.head(10))
        print("\n Типы данных:")
        print(data.dtypes)
        
        
        save_path = Path(__file__).parent / 'spectra.parquet'
        data.to_parquet(save_path)
        print(f"\n Данные сохранены в {save_path.name}")
    
    except FileNotFoundError:
        print(f"Ошибка: {file_name} не найден. Убедитесь, что он лежит в корне папки.")
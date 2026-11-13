import pandas as pd
from pathlib import Path


def load_spectra(file_path, sep=';', encoding='utf-8-sig'):
    """Загружает данные спектров из файла."""
    try:
        df = pd.read_csv(file_path, sep=sep, encoding=encoding)
        return df.rename(columns={df.columns[0]: "Длина волны, нм"})
    except FileNotFoundError:
        print(f"Ошибка: Файл {file_path} не найден.")
        return None


if __name__ == '__main__':
    file_name = Path(__file__).parent / 'спектры.csv'
    data = load_spectra(file_name)
    
    if data is not None:
        print(data.head(10))
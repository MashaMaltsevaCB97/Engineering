import pandas as pd
from pathlib import Path

def extract_data(file_path: str) -> pd.DataFrame:
    print(f"Extract: Читаем {file_path}")
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"Файл {path} не найден")
    return pd.read_csv(path, sep=';', encoding='utf-8-sig')
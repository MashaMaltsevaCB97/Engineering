import requests
import pandas as pd
from pathlib import Path


DATA_DIR = Path(__file__).parent.parent / "data"
DATA_DIR.mkdir(exist_ok=True)

url = 'https://shikimori.io/api/mangas'
params = {'limit': 20, 'order': 'popularity'}
headers = {'User-Agent': 'StudentHomework/1.0'}

print("Запрос к Shikimori...")
try:
    response = requests.get(url, params=params, headers=headers, timeout=15)
    response.raise_for_status()
    data = response.json()
    
    df = pd.DataFrame(data)[['id', 'name', 'russian', 'score', 'kind', 'status']]
    
    save_path = DATA_DIR / "shikimori_manga.csv"
    df.to_csv(save_path, index=False, encoding='utf-8-sig')
    
    print(f"Данные сохранены в {save_path}")
    print(df.head())

except Exception as e:
    print(f"Ошибка: {e}")
import requests
import pandas as pd
import os


if not os.path.exists('data'):
    os.makedirs('data')


url = 'https://shikimori.io/api/mangas'


params = {
    'limit': 20,
    'order': 'popularity'
}


headers = {
    'User-Agent': 'StudentHomework/1.0'
}

print("Запрос Shikimori...")
response = requests.get(url, params=params, headers=headers)


if response.status_code == 200:
    data = response.json()
    
    
    manga_list = []
    for item in data:
        manga_list.append({
            'id': item.get('id'),
            'name': item.get('name'),
            'russian': item.get('russian'),
            'score': item.get('score'),
            'kind': item.get('kind'),
            'status': item.get('status')
        })
        
    
    df = pd.DataFrame(manga_list)
    df.to_csv('data/shikimori_manga.csv', index=False, encoding='utf-8-sig')
    
    print("Данные сохранены в data/shikimori_manga.csv")
    print(df.head())
else:
    print(f"Ошибка: {response.status_code}")
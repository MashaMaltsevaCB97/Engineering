import pandas as pd
def print_first_lines(file_path):
    df= pd.read_csv(file_path, sep=';', encoding='utf-8-sig')
    print("Первые 10 строк")
    print(df.head(10))
if __name__ == '__main__':
    file_name = 'спектры.csv'
    print_first_lines(file_name)
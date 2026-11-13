import argparse
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

from etl.extract import extract_data
from etl.transform import transform_data
from etl.load import load_data

def main():
    parser = argparse.ArgumentParser(description="ETL процесс")
    parser.add_argument("--file-path", required=True, help="Путь к CSV")
    parser.add_argument("--table-name", required=True, help="Имя таблицы")
    
    args = parser.parse_args()
    
    try:
        raw = extract_data(args.file_path)
        clean = transform_data(raw)
        load_data(clean, args.table_name)
    except Exception as e:
        print(f"Ошибка: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
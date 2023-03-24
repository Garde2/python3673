from pathlib import Path
from parameters import *

def write_element(op: str, data: str, name_file_db: str):
    # file_path = Path(name_file_db, name_file_db)
    with open('phonabase/db.txt', op, encoding="utf-8") as data_write:
        data_write.write(f'{data}')

def read_element(name_file: str) -> str:
    # file_path = Path(name_file_db, name_file_db)
    with open('phonabase/db.txt', 'r', encoding="utf-8") as data_read:
        return data_read.read().splitlines()
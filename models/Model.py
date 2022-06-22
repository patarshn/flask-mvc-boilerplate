import sqlite3
import env
import os

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

ModelConnect = sqlite3.connect(os.getenv('DB_NAME'),check_same_thread=False)
ModelConnect.row_factory = dict_factory
ModelCursor = ModelConnect.cursor()
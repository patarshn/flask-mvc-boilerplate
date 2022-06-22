import sqlite3 as sql
from models.Model import ModelConnect, ModelCursor

TABLE = 'users'
def get():
    ModelCursor.execute(f"SELECT * FROM {TABLE}")
    res = ModelCursor.fetchall()
    return res

def getById(id):
    ModelCursor.execute(f"SELECT * FROM {TABLE} WHERE id='{id}'")
    res = ModelCursor.fetchone()
    return res
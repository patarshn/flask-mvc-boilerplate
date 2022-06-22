import sqlite3
import env
import os

ModelConnect = sqlite3.connect(os.getenv('DB_NAME'))
ModelCursor = ModelConnect.cursor()

#Drop users table if already exsist.
ModelCursor.execute("DROP TABLE IF EXISTS users")

#Create users table  in db_web database
sql ="""CREATE TABLE "users" (
	"id"	INTEGER PRIMARY KEY AUTOINCREMENT,
	"name"	TEXT,
	"phone"	TEXT,
    "region" TEXT
)"""

ModelCursor.execute(sql)

#Create users table  in db_web database
sql ="""INSERT INTO "users" VALUES
    (NULL,'Patar','+62 821 693 821','Indonesia'),
    (NULL,'Martua','+32 112 903 712','Belgium'),
    (NULL,'Doli','+62 883 053 133','Australia'),
    (NULL,'Siahaan','+1 900 20 314','United States');"""

ModelCursor.execute(sql)

#commit changes
ModelConnect.commit()

#close the connection
ModelConnect.close()

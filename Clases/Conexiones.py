from . import *

import pymysql

db = pymysql.connect('localhost', 'root', None, 'python')
print(db)

cursor = db.cursor()

cursor.execute("SELECT VERSION()")

version = cursor.fetchone()

print(version)
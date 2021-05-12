import sqlite3
from sqlite3.dbapi2 import IntegrityError
from typing import final

conn = sqlite3.connect('my_db')
curs = conn.cursor()

# statement to write data into our db
statement = '''
INSERT INTO zoo
VALUES ("duck", 5, 0.30)
'''
try:
    curs.execute(statement)
    conn.commit()
except IntegrityError as err:
    print(err)
    conn.rollback()
finally:
    pass

statement = '''
INSERT INTO zoo
VALUES ("bear", 2, 1500.00)
'''
curs.execute(statement)
statement = '''
INSERT INTO zoo
VALUES ("panda", 1, 10000.00)
'''
curs.execute(statement)

# conn.commit()
conn.rollback()
conn.close()
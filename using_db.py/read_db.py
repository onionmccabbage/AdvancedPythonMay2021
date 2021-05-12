import sqlite3

conn = sqlite3.connect('my_db')
curs = conn.cursor()

# we need a statement to read back from our db
statement = '''
SELECT * FROM zoo
WHERE creature LIKE '%a%'
'''
curs.execute(statement)
# now handle the retrieved data
rows = curs.fetchall()
print(rows)

conn.commit()
conn.close()
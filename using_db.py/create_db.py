import sqlite3

# DB2
# import DB2
# conn = DB2.connect(dsn='ibm-DB', uid='analyst', pwd='db2pwd')

# Sybase
# import Sybase
# conn = Sybase.connect('SYBASE', 'username', 'passwd', 'databasename')

# Oracle
# import cx_Oracle
# conn = cx_Oracle.connect('username', 'passwd', 'hostname:port/SID')
# conn2 = cx_Oracle.connect('username/passwd@hostname:portno/SID')
# dsn_tns = cx_Oracle.makedsn('hostname', portno, 'SID')
# conn3 = cx_Oracle.connect('username', 'passwd', dsn_tns)

# MySQL
# import MySQLdb
# conn = MySQLdb.connect(host = "hostname", user = "username",
# passwd = "password", db = "dbname")

# PySQLite
# from pysqlite2 import dbapi2 as sqlite
# conn = sqlite.connect("mydb", connectionproperties)

# ODBC
# import odbc
# conn = odbc. odbc("myDSN/username/password")

# make a connection to the database
conn = sqlite3.connect('my_db') # create the db if not exist

# create a cursor
curs = conn.cursor() # a cursor allows us to work with the db

# execute an sql statement in order to make a table
statement = '''
CREATE TABLE zoo
(creature VARCHAR(20) PRIMARY KEY,
 count INT,
 cost FLOAT
)
'''
curs.execute(statement)

# commit the changes
conn.commit()

# close our connection
conn.close()
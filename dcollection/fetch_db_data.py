import pandas as pd
from python_mysql_dbconfig import read_db_config
from mysql.connector import MySQLConnection, Error


def create_db_connection(section):
    db_config = read_db_config(section=section)
    print('Connecting to MySQL database ...')
    conn = MySQLConnection(**db_config)
    return conn.cursor()

db_cursor = create_db_connection('mysqllocal')
db_cursor.execute('SELECT * FROM officelean')

table_rows = db_cursor.fetchall()

df = pd.DataFrame(table_rows)


df.columns = db_cursor.column_names

state = 0
columnList = df["r1state"]
timeColumnList = df["ctime"]
for i in range(len(columnList)):
    if columnList[i] != state:
        print(i+1, " .state changed")
        print("old state: ", state, "ctime: ", timeColumnList[i])
        state = columnList[i]
        print("new state: ", state, "ctime: ", timeColumnList[i])





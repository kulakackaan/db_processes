from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config

def iterrow(cursor, size=10):
        while True:
            rows = cursor.fetchmany(size)
            if not rows:
                break
            for row in rows:
                yield row

def connect():
    """ Connect to MySQL database"""

    try:
        db_config = read_db_config(section='mysqllocal')
        print('Connecting to MySQL database ...')
        conn = MySQLConnection(**db_config)
        curs = conn.cursor()
        curs.execute("SELECT * FROM officelean")

        for row in iterrow(cursor=curs, size=10):
            print(row)


    except Error as err:
        print(err)

    finally:
        if conn is not None and conn.is_connected():
            conn.close()
            print('Connection closed.')

if __name__ == '__main__':
    connect()
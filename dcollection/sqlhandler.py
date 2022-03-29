from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config

class sqlhandler():

    def __init__(self, section) -> None:
        self.section = section
        self.db_conf = read_db_config(section= self.section)
        self.__query = ""
        self.__fetchsize = 10
        self.result = []

    def __iterrow(self, cursor, size=10):
        while True:
            rows = cursor.fetchmany(size)
            if not rows:
                break
            for row in rows:
                yield row

    def fetchmany(self):
        """ execute query with fetchsize, return result.
        """
        try:
            #print('Connecting to MySQL database ...') loglama gelecek.
            conn = MySQLConnection(**self.db_conf)
            curs = conn.cursor()
            curs.execute(self.__query)

            for row in self.__iterrow(curs, self.__fetchsize):
                self.result.append(row)
            return self.result, curs.column_names


        except Exception as err:
            #logging gelmelidir.
            print(err)
            raise

        finally:
            if conn is not None and conn.is_connected():
                conn.close()
                #print('Connection closed.') loglama gelecek.

    @property
    def query(self):
        return self.__query
    
    @query.setter
    def query(self, value):
        """value 'nun uygunluğu kontrol edilecek.
        """
        self.__query = value

    @property
    def fetchsize(self):
        return self.__fetchsize

    @fetchsize.setter
    def fetchsize(self, value):
        """value 'nun büyüklüğü kontrol edilecek."""
        self.__fetchsize = value

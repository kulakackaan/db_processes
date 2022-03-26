from sqlhandler import sqlhandler
from datamanager import datamanager

dm = datamanager()
localserver = sqlhandler('mysqllocal')
localserver.fetchsize = 10
localserver.query = ("SELECT * FROM officelean WHERE DAY(ctime) > 20")

def refactor_func(dm, localserver):
    try:
        results = localserver.fetchmany()
        #temp = dm.get_errorlist(results, 21, 23, 17, 18, 19, 20, 22)
        #temp = dm.get_errorlist(results, 6, 23)
        temp = dm.get_stoplist(results, 5, 23)
        for tmp in temp:
            print(tmp)
    except Exception as e:
        print(e)

refactor_func(dm, localserver)
#print(dm.get_errorlist.__doc__)
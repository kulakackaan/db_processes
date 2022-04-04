from sqlhandler import sqlhandler
from datamanager import datamanager
import pandas as pd

dm = datamanager()
localserver = sqlhandler('mysqllocal')
localserver.fetchsize = 10
localserver.query = ("SELECT * FROM officelean")

def refactor_func(dm, localserver):
    try:
        results, cnames = localserver.fetchmany()
        df = pd.DataFrame(results)
        df.columns = cnames
        df.to_csv('C:/Users/Pc/Desktop/DataFrame.csv')
        df = pd.read_csv('C:/USers/Pc/Desktop/DataFrame.csv')
        df.fillna(' ', inplace=True)
        df.drop(columns='Unnamed: 0', inplace=True)
        print(df)
        #temp = dm.get_errorlist(results, 21, 23, 17, 18, 19, 20, 22)
        #temp = dm.get_errorlist(rsults, 6, 23)
        #temp = dm.get_stoplist(results, 5, 23)
        #for tmp in temp:
            #print(tmp)
    except Exception as e:
        print(e)

refactor_func(dm, localserver)
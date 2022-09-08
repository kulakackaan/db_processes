import pandas as pd

class datamanager():
    def __init__(self) -> None:
        pass

    def timediff(self, ftime, stime):
        """ calculate time diff. btw. datetime.datetime objects.
        :param ftime: finish datetime parameter.
        :param stime: start datetime parameter.
        :return: string "hours:minutes:seconds"
        """
        _dif = ftime - stime
        _hours = divmod(_dif.total_seconds(), 3600)[0]
        _mins = divmod(_dif.total_seconds(), 60)[0] - _hours * 60
        _secs = _dif.total_seconds() - ((_hours * 60 + _mins) * 60)
        return f"{str(_hours).split('.')[0]}:{str(_mins).split('.')[0]}:{str(_secs).split('.')[0]}"

    def get_errorlist_df(self, df, rxstring, ctime, shift):
        """ evaluating of given stop type and return them as dataframe.
        :param df: given dataframe(must include rxstring, time and shift).
        :param rxstring: column name of robot stop string at given df.
        :param ctime: column name of time at given df.
        :param shift: column name of shift at given df.
        :return: df as [Id, Ariza Tipi, Baslangic, Bitis, Sure, Vardiya]
        """
        _rsdf = pd.DataFrame(columns=['Id', 'ArizaTipi', 'Baslangic', 'Bitis', 'Sure', 'Vardiya'])
        _errorstate = False
        _oldstate = ' '

        for row in range(df.shape[0]):
            rowact = df.iloc[row] #islem gören satir
            if row==df.shape[0]-1:
                _rsdf.loc[_rsdf.shape[0]-1, 'Bitis'] = rowact[ctime]
                _rsdf.loc[_rsdf.shape[0]-1, 'Sure'] = self.timediff(rowact[ctime], _rsdf.loc[_rsdf.shape[0]-1, 'Baslangic'])
            if rowact[rxstring]=='': continue
            if rowact[rxstring] != _oldstate: #degisiklik varsa
                _oldstate = rowact[rxstring]
                if _errorstate == False: #mevcut hata yakalaması yoksa
                    _errorstate = True
                    _rsdf.loc[_rsdf.shape[0]] = [rowact["id"], rowact[rxstring], rowact[ctime], '', '', rowact[shift]] #cikis df'sine yeni satir olarak ekle
                else: #mevcut hata yakalaması varsa
                    if rowact[rxstring] != ' ': #cikis df'sinin son satirini guncelle ve yeni satir ac.
                        _rsdf.loc[_rsdf.shape[0]-1, 'Bitis'] = rowact[ctime] 
                        _rsdf.loc[_rsdf.shape[0]-1, 'Sure'] = self.timediff(rowact[ctime], _rsdf.loc[_rsdf.shape[0]-1, 'Baslangic'])
                        _rsdf.loc[_rsdf.shape[0]] = [rowact["id"], rowact[rxstring], rowact[ctime], '', '', rowact[shift]]

                    else: #cikis df'sinin son satirini guncelle.
                        _errorstate = False
                        _rsdf.loc[_rsdf.shape[0]-1, 'Bitis'] = rowact[ctime]
                        _rsdf.loc[_rsdf.shape[0]-1, 'Sure'] = self.timediff(rowact[ctime], _rsdf.loc[_rsdf.shape[0]-1, 'Baslangic'])
                                
        return _rsdf


    def get_errorlist(self, results, cstring, ctime):
        """ evaluating of given stop type and returning them as list.
        :param result: list of tuple from sql results. Can be handle by sqlhandler.fetchmany()
        :param cstring: index number of string column in sql result.
        :param ctime: index number of time column in sql result.
        :return: four values list. [error type, err start time, err stop time, err duration] 
        """
        _rslt = []
        _errorstate = False
        _oldstate = ' '

        for result in results:
            if result[cstring] == '': continue
            if result[cstring] != _oldstate:
                _oldstate = result[cstring]
                if _errorstate == False:
                    _errorstate = True
                    _rslt.append([result[cstring], result[ctime]])
                else:
                    if result[cstring] != ' ':
                        _rslt[-1].append(result[ctime])
                        _rslt[-1].append(self.timediff(result[ctime], _rslt[-1][1]))
                        _rslt.append([result[cstring], result[ctime]])
                    else:
                        _errorstate = False
                        _rslt[-1].append(result[ctime])
                        _rslt[-1].append(self.timediff(result[ctime], _rslt[-1][1]))
        
        return _rslt

    def get_stoplist_df(self, df, rxstate, ctime, shift):
        _rsdf = pd.DataFrame(columns=['Id', 'Baslangic', 'Bitis', 'Sure', 'Vardiya'])
        _errorstate = False
        _oldstate = 1

        for row in range(df.shape[0]):
            rowact = df.iloc[row] #islem goren satir
            if rowact[rxstate] != _oldstate:
                _oldstate = rowact[rxstate]
                if _errorstate == False:
                    _errorstate = True
                    _rsdf.loc[_rsdf.shape[0]] = [rowact["id"], rowact[ctime], '', '', rowact[shift]]
                else:
                    _errorstate = False
                    _rsdf.loc[_rsdf.shape[0]-1, 'Bitis'] = rowact[ctime]
                    _rsdf.loc[_rsdf.shape[0]-1, 'Sure'] = self.timediff(rowact[ctime], _rsdf.loc[_rsdf.shape[0]-1, 'Baslangic'])

            if row==df.shape[0]-1:
                _rsdf.loc[_rsdf.shape[0]-1, 'Bitis'] = rowact[ctime]
                _rsdf.loc[_rsdf.shape[0]-1, 'Sure'] = self.timediff(rowact[ctime], _rsdf.loc[_rsdf.shape[0]-1, 'Baslangic'])

        return _rsdf
    
    def get_stoplist(self, results, cstate, ctime):
        """ evaluating of given robot stops and returning them as list.
        :param result: list of tuple from sql results. Can be handle by sqlhandler.fetchmany()
        :param cstate: index number of robot's state column in sql result.
        :param ctime: index number of time column in sql result.
        :return: four values list. [robot stop's start time, robot stop's stop time, robot stop's duration] 
        """
        _rslt = []
        _errorstate = False
        _oldstate = 1

        for result in results:
            if result[cstate] != _oldstate:
                _oldstate = result[cstate]
                if _errorstate == False:
                    _errorstate = True
                    _rslt.append([result[ctime]])
                else:
                    _errorstate = False
                    _rslt[-1].append(result[ctime])
                    _rslt[-1].append(self.timediff(result[ctime], _rslt[-1][0]))

        return _rslt

    def get_shiftlist(self, results, cshiftstate, ctime, cr3count, cr5count, cnetprod, cerrprod, cshift):
        """ evaluating of given shift's start-stop times and product counts.
        :param result: list of tuple from sql results. Can be handle by sqlhandler.fetchmany()
        :param cshiftstate: index number of shiftstate column in sql result.
        :param ctime: index number of time column in sql result.
        :param ctime: index number of 1st polish group's count column in sql result.
        :param ctime: index number of 2nd polish group's count column in sql result.
        :param ctime: index number of netprod column in sql result.
        :param ctime: index number of errprod column in sql result.
        :param ctime: index number of shift column in sql result.
        :return: four values list. [robot stop's start time, robot stop's stop time, robot stop's duration] 
        """
        _rslt = [["starttime", "stoptime", "duration", "p1count", "p2count", "netprod", "errprod", "shiftname"]]
        _shiftstate = False
        _oldstate = 0

        for result in results:
            if result[cshiftstate] != _oldstate:
                _oldstate = result[cshiftstate]
                if _shiftstate == False:
                    _shiftstate = True
                    _rslt.append([result[ctime]])
                else:
                    _shiftstate = False
                    _rslt[-1].append(result[ctime])
                    _rslt[-1].append(self.timediff(result[ctime], _rslt[-1][0]))
                    _rslt[-1].append(result[cr3count])
                    _rslt[-1].append(result[cr5count])
                    _rslt[-1].append(result[cnetprod])
                    _rslt[-1].append(result[cerrprod])
                    _rslt[-1].append(result[cshift])

        return _rslt
from math import exp, sqrt
from datetime import date
from typing import Counter
import mysql.connector
from  mysql.connector  import errorcode
from mysql.connector import (connection)

#pep 249
connectionConfig = {
'user':'u218449937_usr_7',
'password':'n2C?u7@L7',
'host':'auth-db1803.hstgr.io',
'database':'u218449937_db_7',
'raise_on_warnings': True  #  alza anceh i warnings
}
try:
    
    connectionData = connection.MySQLConnection(**connectionConfig)
    print('connessione avvenuta')

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print('nome o pass sbagliati')
    elif  err.errno == errorcode.ER_BAD_DB_ERROR:
        print('database non  esiste')
    else:
        print(err+'errore non gestito')






connectionData.close()

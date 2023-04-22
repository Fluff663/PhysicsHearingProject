#formats DB for main.py

import pyodbc

#inits pyodbc to access database
conn_str = (r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
            r'DBQ=.\data.accdb;')
conn = pyodbc.connect(conn_str)


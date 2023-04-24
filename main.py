#gathers hearing range data 500-1000-2000-4000-6000-8000-10000-15000-16000-180000-20000 hz and writes to data.accdb

from __future__ import division
import pyodbc
import winsound

#inits pyodbc to access data.accdb
conn_str = (r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
            r'DBQ=.\data.accdb;')
conn = pyodbc.connect(conn_str)

userpref = input("Do you like rap? Y/N")
winsound.Beep(500, 1000)  # Beep at 1000 Hz for 100 ms
f500hz = input("Did You hear the tone? Y/N")
winsound.Beep(1000, 1000)  # Beep at 1000 Hz for 100 ms
f1000hz = input("Did You hear the tone? Y/N")
winsound.Beep(2000, 1000)  # Beep at 1000 Hz for 100 ms
f2000hz = input("Did You hear the tone? Y/N")
winsound.Beep(4000, 1000)  # Beep at 1000 Hz for 100 ms
f4000hz = input("Did You hear the tone? Y/N")
winsound.Beep(6000, 1000)  # Beep at 1000 Hz for 100 ms
f6000hz = input("Did You hear the tone? Y/N")
winsound.Beep(8000, 1000)  # Beep at 1000 Hz for 100 ms
f8000hz = input("Did You hear the tone? Y/N")
winsound.Beep(10000, 1000)  # Beep at 1000 Hz for 100 ms
f10000hz = input("Did You hear the tone? Y/N")
winsound.Beep(12000, 1000)  # Beep at 1000 Hz for 100 ms
f12000hz = input("Did You hear the tone? Y/N")
winsound.Beep(14000, 1000)  # Beep at 1000 Hz for 100 ms
f14000hz = input("Did You hear the tone? Y/N")
winsound.Beep(16000, 1000)  # Beep at 1000 Hz for 100 ms
f16000hz = input("Did You hear the tone? Y/N")
winsound.Beep(18000, 1000)  # Beep at 1000 Hz for 100 ms
f18000hz = input("Did You hear the tone? Y/N")
winsound.Beep(20000, 1000)  # Beep at 1000 Hz for 100 ms
f20000hz = input("Did You hear the tone? Y/N")
if userpref == "y":
    buserpref = True
if userpref == "n":
    buserpref = False
if f500hz == "y" :
    b500hz = True
if f500hz == "n" :
    b500hz = False
if f1000hz == "y" :
    b1000hz = True
if f1000hz == "n" :
    b1000hz = False
if f2000hz == "y" :
    b2000hz = True
if f2000hz == "n" :
    b2000hz = False
if f4000hz == "y" :
    b4000hz = True
if f4000hz == "n" :
    b4000hz = False
if f6000hz == "y" :
    b6000hz = True
if f6000hz == "n" :
    b6000hz = False
if f8000hz == "y" :
    b8000hz = True
if f8000hz == "n" :
    b8000hz = False
if f10000hz == "y" :
    b10000hz = True
if f10000hz == "n" :
    b10000hz = False
if f12000hz == "y" :
    b12000hz = True
if f12000hz == "n" :
    b12000hz = False
if f14000hz == "y" :
    b14000hz = True
if f14000hz == "n" :
    b14000hz = False
if f16000hz == "y" :
    b16000hz = True
if f16000hz == "n" :
    b16000hz = False
if f18000hz == "y" :
    b18000hz = True
if f18000hz == "n" :
    b18000hz = False
if f20000hz == "y" :
    b20000hz = True
if f20000hz == "n" :
    b20000hz = False
try:
    buserpref
    b500hz
    b1000hz
    b2000hz
    b4000hz
    b6000hz
    b8000hz
    b10000hz
    b12000hz
    b14000hz
    b16000hz
    b18000hz
    b20000hz
except NameError:
    print("Please use a single y/n for all responses")
    exit()
print("Run Success!")
print("Please wait while we write results to database")
#Code to write to data.accdb
import pyodbc
conn = pyodbc.connect('Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=.\data.accdb;')
cursor = conn.cursor()
cursor.execute('INSERT INTO data (userprefrap, f500hz, f1000hz, f2000hz, f4000hz, f6000hz, f8000hz, f10000hz, f12000hz, f14000hz, f16000hz, f18000hz, f20000hz) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)', buserpref, b500hz, b1000hz, b2000hz, b4000hz, b6000hz, b8000hz, b10000hz, b12000hz, b14000hz, b16000hz, b18000hz, b20000hz)
conn.commit()
conn.close()
print("Results written to database")
print("Thank you for your time!")
print("Press any key to exit")
input()
exit()

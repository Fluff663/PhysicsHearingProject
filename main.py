#gathers hearing range data 500-1000-2000-4000-6000-8000-10000-15000-16000-180000-20000 hz and writes to data.accdb

from __future__ import division
import pyodbc
import math
from pyaudio import PyAudio

#inits pyodbc to access data.accdb
conn_str = (r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
            r'DBQ=.\data.accdb;')
conn = pyodbc.connect(conn_str)

print('yeetus deletus')

#defines func for sine wave

try:
    from itertools import izip
except ImportError: # Python 3
    izip = zip
    xrange = range

def sine_tone(frequency, duration, volume=1, sample_rate=22050):
    n_samples = int(sample_rate * duration)
    restframes = n_samples % sample_rate

    p = PyAudio()
    stream = p.open(format=p.get_format_from_width(1), # 8bit
                    channels=1, # mono
                    rate=sample_rate,
                    output=True)
    s = lambda t: volume * math.sin(2 * math.pi * frequency * t / sample_rate)
    samples = (int(s(t) * 0x7f + 0x80) for t in xrange(n_samples))
    for buf in izip(*[samples]*sample_rate): # write several samples at a time
        stream.write(bytes(bytearray(buf)))

    # fill remainder of frameset with silence
    stream.write(b'\x80' * restframes)

    stream.stop_stream()
    stream.close()
    p.terminate()

#print("end_sine")

userpref = input("Do you like rap? Y/N")
sine_tone(
    # see http://www.phy.mtu.edu/~suits/notefreqs.html
    frequency=500.00, # Hz, waves per second A4
    duration=3, # seconds to play sound
    volume=1, # 0..1 how loud it is
    # see http://en.wikipedia.org/wiki/Bit_rate#Audio
    sample_rate=22050 # number of samples per second
    )
f500hz = input("Did You hear the tone? Y/N")
sine_tone(
    # see http://www.phy.mtu.edu/~suits/notefreqs.html
    frequency=1000.00, # Hz, waves per second A4
    duration=3, # seconds to play sound
    volume=1, # 0..1 how loud it is
    # see http://en.wikipedia.org/wiki/Bit_rate#Audio
    sample_rate=22050 # number of samples per second
    )
f1000hz = input("Did You hear the tone? Y/N")
sine_tone(
    # see http://www.phy.mtu.edu/~suits/notefreqs.html
    frequency=2000.00, # Hz, waves per second A4
    duration=3, # seconds to play sound
    volume=1, # 0..1 how loud it is
    # see http://en.wikipedia.org/wiki/Bit_rate#Audio
    sample_rate=22050 # number of samples per second
    )
f2000hz = input("Did You hear the tone? Y/N")
sine_tone(
    # see http://www.phy.mtu.edu/~suits/notefreqs.html
    frequency=4000.00, # Hz, waves per second A4
    duration=3, # seconds to play sound
    volume=1, # 0..1 how loud it is
    # see http://en.wikipedia.org/wiki/Bit_rate#Audio
    sample_rate=22050 # number of samples per second
    )
f4000hz = input("Did You hear the tone? Y/N")
sine_tone(
    # see http://www.phy.mtu.edu/~suits/notefreqs.html
    frequency=6000.00, # Hz, waves per second A4
    duration=3, # seconds to play sound
    volume=1, # 0..1 how loud it is
    # see http://en.wikipedia.org/wiki/Bit_rate#Audio
    sample_rate=22050 # number of samples per second
    )
f6000hz = input("Did You hear the tone? Y/N")
sine_tone(
    # see http://www.phy.mtu.edu/~suits/notefreqs.html
    frequency=8000.00, # Hz, waves per second A4
    duration=3, # seconds to play sound
    volume=1, # 0..1 how loud it is
    # see http://en.wikipedia.org/wiki/Bit_rate#Audio
    sample_rate=22050 # number of samples per second
    )
f8000hz = input("Did You hear the tone? Y/N")
sine_tone(
    # see http://www.phy.mtu.edu/~suits/notefreqs.html
    frequency=10000.00, # Hz, waves per second A4
    duration=3, # seconds to play sound
    volume=1, # 0..1 how loud it is
    # see http://en.wikipedia.org/wiki/Bit_rate#Audio
    sample_rate=22050 # number of samples per second
    )
f10000hz = input("Did You hear the tone? Y/N")
sine_tone(
    # see http://www.phy.mtu.edu/~suits/notefreqs.html
    frequency=12000.00, # Hz, waves per second A4
    duration=3, # seconds to play sound
    volume=1, # 0..1 how loud it is
    # see http://en.wikipedia.org/wiki/Bit_rate#Audio
    sample_rate=22050 # number of samples per second
    )
f12000hz = input("Did You hear the tone? Y/N")
sine_tone(
    # see http://www.phy.mtu.edu/~suits/notefreqs.html
    frequency=14000.00, # Hz, waves per second A4
    duration=3, # seconds to play sound
    volume=1, # 0..1 how loud it is
    # see http://en.wikipedia.org/wiki/Bit_rate#Audio
    sample_rate=22050 # number of samples per second
    )
f14000hz = input("Did You hear the tone? Y/N")
sine_tone(
    # see http://www.phy.mtu.edu/~suits/notefreqs.html
    frequency=16000.00, # Hz, waves per second A4
    duration=3, # seconds to play sound
    volume=1, # 0..1 how loud it is
    # see http://en.wikipedia.org/wiki/Bit_rate#Audio
    sample_rate=22050 # number of samples per second
    )
f16000hz = input("Did You hear the tone? Y/N")
sine_tone(
    # see http://www.phy.mtu.edu/~suits/notefreqs.html
    frequency=18000.00, # Hz, waves per second A4
    duration=3, # seconds to play sound
    volume=1, # 0..1 how loud it is
    # see http://en.wikipedia.org/wiki/Bit_rate#Audio
    sample_rate=22050 # number of samples per second
    )
f18000hz = input("Did You hear the tone? Y/N")
sine_tone(
    # see http://www.phy.mtu.edu/~suits/notefreqs.html
    frequency=20000.00, # Hz, waves per second A4
    duration=3, # seconds to play sound
    volume=1, # 0..1 how loud it is
    # see http://en.wikipedia.org/wiki/Bit_rate#Audio
    sample_rate=22050 # number of samples per second
    )
f20000hz = input("Did You hear the tone? Y/N")
if userpref == "y":
    buserpref = True
if userpref == "n":
    buserpref = False
if f500hz == "y":
    b500hz = True
if f500hz == "n":
    b500hz = False
if f1000hz == "y":
    b1000hz = True
if f1000hz == "n":
    b1000hz = False
if f2000hz == "y":
    b2000hz = True
if f2000hz == "n":
    b2000hz = False
if f4000hz == "y":
    b4000hz = True
if f4000hz == "n":
    b4000hz = False
if f6000hz == "y":
    b6000hz = True
if f6000hz == "n":
    b6000hz = False
if f8000hz == "y":
    b8000hz = True
if f8000hz == "n":
    b8000hz = False
if f10000hz == "y":
    b10000hz = True
if f10000hz == "n":
    b10000hz = False
if f12000hz == "y":
    b12000hz = True
if f12000hz == "n":
    b12000hz = False
if f14000hz == "y":
    b14000hz = True
if f14000hz == "n":
    b14000hz = False
if f16000hz == "y":
    b16000hz = True
if f16000hz == "n":
    b16000hz = False
if f18000hz == "y":
    b18000hz = True
if f18000hz == "n":
    b18000hz = False
if f20000hz == "y":
    b20000hz = True
if f20000hz == "n":
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
cursor.execute('INSERT INTO data (userpref, f500hz, f1000hz, f2000hz, f4000hz, f6000hz, f8000hz, f10000hz, f12000hz, f14000hz, f16000hz, f18000hz, f20000hz) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)', buserpref, b500hz, b1000hz, b2000hz, b4000hz, b6000hz, b8000hz, b10000hz, b12000hz, b14000hz, b16000hz, b18000hz, b20000hz)
conn.commit()
conn.close()
print("Results written to database")
print("Thank you for your time!")
print("Press any key to exit")
input()
exit()

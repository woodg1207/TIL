#pip install serial
import serial
import sys
import time

ardu = serial.Serial('COM8',9600)
cnt = 0
while 1:

    x = []
    y = []
    z = []
    tm = time.localtime()
    # print(type(tm.tm_sec), cnt)
    # print(tm.tm_sec)
    start = tm.tm_sec
    while start+1>time.localtime().tm_sec:
        a = ardu.readline()
        b = a.decode()[:-2]
        c=list(map(int,b.split(',')))
        x.append(c[0])
        y.append(c[1])
        z.append(c[2])
        # print(tm.tm_sec)
        if start==59 and time.localtime().tm_sec==0:
            break

    x_range = abs(max(x)-min(x))
    y_range = abs(max(y)-min(y))
    z_range = abs(max(z)-min(z))


    # print(x, y, z)
    print(x_range, y_range, z_range)
    print('------')

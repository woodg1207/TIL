
import time
from time import strftime 

def dms_to_dec(value, dir): 
    mPos = value.find(".")-2 
    degree = float(value[:mPos]) 
    minute = float(value[mPos:]) 
    converted_degree = float(degree) + float(minute)/float(60) 
    if dir == "W": 
        converted_degree = -converted_degree 
    elif dir == "S": 
        converted_degree = -converted_degree 
    return "%.9f" % float(round(converted_degree, 8)) 

def lat_long(value):
    return ['lat : ' + dms_to_dec(value[2], value[3]) , 'long : ' + dms_to_dec(value[4], value[5]) ]

gp_data = '$GPGGA,083312.00,3620.89123,N,12717.83332,E,1,06,1.26,124.3,M,19.9,M,,5C'
# gps = '$GPGGA,083312.00,3620.89123,N,12717.83332,E,1,06,1.26,124.3,M,19.9,M,,5C'

arr = gp_data.split(',')

print(lat_long(arr))
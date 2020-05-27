import serial
import sys
def serial_ports():   
    """ Lists serial port names   
       
        :raises EnvironmentError:   
            On unsupported or unknown platforms   
        :returns:   
            A list of the serial ports available on the system   
    """   
    if sys.platform.startswith('win'):   
        ports = ['COM%s' % (i + 1) for i in range(256)]   
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):   
        # this excludes your current terminal "/dev/tty"   
        ports = glob.glob('/dev/tty[A-Za-z]*')   
    elif sys.platform.startswith('darwin'):   
        ports = glob.glob('/dev/tty.*')   
    else:   
        raise EnvironmentError('Unsupported platform')   
       
    result = []   
    for port in ports:   
        try:   
            s = serial.Serial(port)   
            s.close()   
            result.append(port)   
        except (OSError, serial.SerialException):   
            pass   
    return result   
   
   
if __name__ == '__main__':   
    print(serial_ports()) 
# [출처] serial (COM) 포트 찾기|작성자 과객



# ardu = serial.serial.Serial('COM7',115200)
ardu = serial.Serial('COM7',115200)

while 1:
    a = ardu.readline()
    print(a)
    b = a.decode()
    print(b)
    print('------')

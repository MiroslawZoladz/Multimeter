import serial

def commmand(cmd):
    # global comm
   
    comm = serial.Serial('Com56',115200,timeout=1)
    comm.flushInput()
    
    comm.write(cmd.encode('UTF-8')+b'\r\n')
    comm.flushOutput()
    
    comm.readline()
    res = comm.readline()
    
    comm.close()
    
    return res

_ = commmand('o 1.123 0.567 ')

def ai(ch_nr=''):
    res = commmand(f'i {ch_nr}')
    return  list(map(float,res.split()[:-1]))

print(ai(7))

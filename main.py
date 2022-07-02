import sys
sys.path.append('../lib')

from analog_outputs import AnalogOutputs
from analog_inputs import AnalogInputs

HELP = """
FUNCTION    : COMMAND

help        : h

# outputs 0-1

output      : o [v_out0] [v out1]
groud       : ognd
range min   : omin
range max   : omax
callibration: ocal [v_at_min_on_out0] [v_at_min_on_out1] [v_at_max_on_out0] [v_at_max_on_out1]

# inputs 0-11

// measured diferrentially,
// ref->adc*.ch0,
// in 0-6 -> adc0.1-7
// in 7-11 -> adc1.1-5

input         : i [channel count] // if no arg all channels
callibration  : ical [v_at_ch_0] [v_at_ch_6]
"""      
ao = AnalogOutputs()
ai = AnalogInputs()

while True:    
    command = input("?:")
    
    # command preprocessing
    tokens = command.split()
    if not tokens:
        print(HELP)
        continue
    cmd, arg  = tokens[0], [float(s) for s in tokens[1:]]
    
    #  command execution
    if   cmd == 'id':   print('multimeter')
    
    elif cmd == 'o':    ao.voltage(*arg) 
    elif cmd == 'ognd': ao.gnd()
    elif cmd == 'omin': ao.min()
    elif cmd == 'omax': ao.max()
    elif cmd == 'ocal': ao.callib(*arg)
        
    elif cmd == 'i':
        if len(arg)==0:
            arg = (ai.CHANELL_NR,)# all channels
        print(' '.join([f'{v:0.3f}'for v in ai.voltages(*arg)]),end='')
    elif cmd == 'ical':ai.callib(*arg)
    
    else: print(HELP)
    
    print(' OK')
    
#-------------------------
# ocal 0.00349 0.0021 1.213 1.2097
# ical 1.21287 1.2097
        
      
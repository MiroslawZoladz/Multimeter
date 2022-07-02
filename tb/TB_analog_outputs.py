import sys
sys.path.append('../lib')

from analog_outputs import AnalogOutputs

ao = AnalogOutputs()
# ao.gnd()
# ao.min()
# ao.max()

# ao.callib(v0_min=0.00349, v1_min=0.0021, v0_max=1.213, v1_max=1.2097)
ao.voltage(1.00, 1.00)




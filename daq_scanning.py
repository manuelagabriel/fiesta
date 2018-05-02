# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 12:20:32 2017

@author: Administrator
"""

from __future__ import print_function, division
from PyIOTech import daq, daqh

#%% MOVIMIENTO SCANNERS
#"""Output an analog voltage to a single DAC channel."""
import time
from PyIOTech.daq import daqDevice
from PyIOTech.daqh import DddtLocal
import numpy as np

## Device name as registered with the Windows driver.
#   device_name = b'DaqBoard3K0'
## Output channel number.
channel0 = 0 #x
channel1 = 1 #y
## DAC channel location.

dev = daqDevice(b'DaqBoard3K0')
dev.DacWt(deviceType, channel0, 0.0)
dev.DacWt(deviceType, channel1, 0.0)
time.sleep(1)
# Close the connection to the device even if an exception is raised.
dev.Close()

#%% RAMPA
deviceType = DddtLocal
dev = daqDevice(b'DaqBoard3K0')
A = 1 # Amplitude
size = 256 #Pixels*Pixels
for n in range(0, 10):
    #print(n)
    for m in range(0, 10):
        y = A*n/size
        x = A*m/size
        dataVal0 = x
        dataVal1 = y
        print('x = ',x)
        #print('y = ',y)
        # Connect to the device.
        dev.DacWt(deviceType, channel0, dataVal0)
        dev.DacWt(deviceType, channel1, dataVal1)
        #print(n,m)
        time.sleep(0.001)

dev.Close()


#for x in range(0, 100):
#    y = x/10
#    #dataVal = y
#    dataVal0 = x/10
#    dataVal1 = x/10
#    # Connect to the device.
#    dev = daqDevice(b'DaqBoard3K0')
#    # Set the output voltage.
#    dev.DacWt(deviceType, channel0, dataVal0)
#    dev.DacWt(deviceType, channel1, dataVal1)
#    # Wait in seconds.
#    time.sleep(1)
#    dev.Close()

# Reset the output voltage to zero.
dev = daqDevice(b'DaqBoard3K0')
dev.DacWt(deviceType, channel0, 0.0)
dev.DacWt(deviceType, channel1, 0.0)
time.sleep(1)
# Close the connection to the device even if an exception is raised.
dev.Close()

from __future__ import print_function, division
from PyIOTech import daq, daqh

import time
from PyIOTech.daq import daqDevice
from PyIOTech.daqh import DddtLocal
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from pylab import *
from PIL import Image


class Scanner:

    def __init__(self):
        self.amplitude = 0.01
        self.frequency = 10000
        self.size = 128  # Pixels*Pixels
        self.channel0 = 0
        self.channel1 = 1
        self.device = daqDevice(b'DaqBoard3K0')
        self.deviceType = DddtLocal
        self.gain = daqh.DgainX1
        self.flags = daqh.DafAnalog | daqh.DafUnsigned | daqh.DafBipolar | daqh.DafDifferential
        self.max_voltage = 10.0
        self.bit_depth = 16
        self.img= np.zeros((self.size, self.size, 3), dtype=np.uint8)

    def frame_scan(self):
        start = time.time()
        for n in range(0, self.size):
            valor = []
            for m in range(0, self.size):
                value0 = self.amplitude*n/self.size
                value1 = self.amplitude*m/self.size
                self.device.DacWt(self.deviceType, self.channel0, value0)
                self.device.DacWt(self.deviceType, self.channel1, value1)
                data = self.device.AdcRd(self.channel1, self.gain, self.flags)
                valor[m] = data * self.max_voltage * 2 / (2 ** self.bit_depth) - self.max_voltage
                print(data)
                # time.sleep(1/self.frequency)
            self.img[n] = valor
        print("Duracion por frame en segundos:", time.time() - start)


    def x_line_scan(self):
        for n in range(0, self.size):
            value = self.amplitude*n/self.size
            self.device.DacWt(self.deviceType, 0, value)
        # self.device.Close()

    def y_line_scan(self):
        for n in range(0, self.size):
            value = self.amplitude*n/self.size
            self.device.DacWt(self.deviceType, 1, value)
        # self.device.Close()

    def __delete__(self):
        self.device.Close()


if __name__ == '__main__':  # Esto en el futuro va a estar en un Main.py
    tic = time.time()
    s = Scanner()
    s.frame_scan()
    s.__delete__()
    toc = time.time()
    # s.x_line_scan()
    # s.y_line_scan()
    # print("Se movio con amplitud {} V".format(s.amplitude))
    print("Duracion total en segundos:", toc - tic)
    image = plt.imshow(s.img)
    plt.imshow(s.img, interpolation='nearest')
    grid(True)
    image = Image.fromarray(s.img, 'RGB')
    image.save('my.png')
    image.show()
# Esperar unos segundos a que cierre el device para volver a correr
# Por ahora el frame time mas chico que alcanza es 0.3 seg (aprox 18 us por pixel)
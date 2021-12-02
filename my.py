from stats1 import dis
from rgb import  setRGBEffect
import smbus
import time
import os
bus = smbus.SMBus(1)

addr = 0x0d
fan_reg = 0x08
state = 0
temp = 0
level_temp = 0




while True:
      a=dis()
      print(a)
      temp = float(a)
      if temp <= 40:
        bus.write_byte_data(addr, fan_reg, 0x00)
      elif temp >= 45:
        bus.write_byte_data(addr, fan_reg, 0x01)

        time.sleep(1)
      setRGBEffect(2)         
      


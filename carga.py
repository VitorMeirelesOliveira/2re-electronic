
import RPi.GPIO as gpio
import threading
import time
DAT =13
CLK=8
num=0
gpio.setwarnings(False)
gpio.setmode(gpio.BOARD)
gpio.setup(CLK, gpio.OUT)
def weight():
  i=0
  num=0
  gpio.setup(DAT, gpio.OUT)
  gpio.output(DAT,1)
  gpio.output(CLK,0)
  gpio.setup(DAT, gpio.IN)

  while gpio.input(DAT) == 1:
      i=0
  for i in range(24):
        gpio.output(CLK,1)
        num=num<<1

        gpio.output(CLK,0)

        if gpio.input(DAT) == 0:
            num=num+1

  gpio.output(CLK,1)
 # print num
  num=num^0x800000
 # print num
  gpio.output(CLK,0)
  wei=0
  wei=((num)/1406)
  p=((num)/14.06)
  p1=p-59423
 # print p1
 # print p
  PN=(p-594261)
  N=PN/1.503
 # print N,"g"
  quilo=N/1000
 # print quilo,"kg"
 # print PN
 # print wei
 # print ((wei-5943))
 # time.sleep(0.5)
  PESO=(((wei-5943)/15))
  print PESO,"kg"
  time.sleep(0.5)
while True:
 weight()

# 2re-electronic

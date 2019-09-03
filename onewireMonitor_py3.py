#!/usr/bin/python3

#########################################################################################
#
# oneWireMonitor
#
# Written by Simon Kong for the Raspberry Pi
# V1.0 03/09/2019
#
# Monitor onewire temp directory and hard reset power to the DS18B20 if folder is not present.

import signal
import RPi.GPIO as GPIO
import time
import os
import datetime


# handle kill signal
def handle_exit(sig, frame):
  raise(SystemExit)
# Handle kill signal
def setup_OSsignal():
  signal.signal(signal.SIGTERM, handle_exit)


print("\n\n{} - starting OneWire monitor".format(datetime.datetime.now()))
setup_OSsignal()


try:
  GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme
  GPIO.setup(17, GPIO.OUT)
  while True:
    # uncomment the next line, to log when the next cycle is starthing
    print("{} - Starting new cycle".format(datetime.datetime.now()))

    # change this according to the folder / DS18B20 serial to monitor
    #if (os.path.isdir("/sys/bus/w1/devices/28-XXXXXXXXXXXX") == False):
    if (os.path.isdir("/sys/bus/w1/devices/28-030797798892") == False):
      print("{} - Reseting OneWire".format(datetime.datetime.now()))
      GPIO.output(17, GPIO.LOW)
      time.sleep(3)
      GPIO.output(17, GPIO.HIGH)
      #time.sleep(5)

    # sleep for 50 sec
    time.sleep(50)

except KeyboardInterrupt:
  print("Keyboard Inturrupt detected")

except SystemExit:
  print("kill signal detected")

except:
  print("Some other error detected")

finally:
  # eigher way, do this before exit
  print("{} - cleanning up GPIO pins".format(datetime.datetime.now()))
  GPIO.cleanup()
  

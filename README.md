# onewireMonitor
onewireMonitor. For Raspberry Pi. This will **Monitor onewire temp directory and hard reset power to the DS18B20 if folder is not present.**

this is a workaround for when DS18B20 temp sensors keeps disappearing and log showing

octopi kernel: [46102.211560] w1_slave_driver 28-XXXXXXXXXXXX: Read failed CRC check

**it will probably be better to find the cause the issue (wiring/connector/capacitance) than to use this. **


The script [onewireMonitor](https://github.com/SkullKill/onewireMonitor) is design specificly for the Raspberry Pi.

SKaccess by Simon Kong

https://www.skaccess.com

## V 1.0 03/09/2019 - Initial Release




## one wire setup

### software
    rasppi-config
        Interfacing Options >> 1-Wire >> enable yes,
        reboot

### hardware.

data pin to rpi gpio (BCM) #4 [physical pin 7]

ground to rip ground [physical pin 9] using this because it is next to #4

power pin to rpi gpio #17 [physical pin 11]



you can use any other pin, but #17 is what the code is written for, just change the code if using another pin.


## Installation
download the files

copy both onewireMonitor.sh and onewireMonitor_py3.py to /usr/local/sbin and set permission

find out the folder / DS18B20 serial to monitor

change "/sys/bus/w1/devices/28-XXXXXXXXXXXX" to the correct value in onewireMonitor_py3.py

edit /etc/crontab and add the following line at the end of the file

```
# monitor and start onewireMonitor is process is not running
*/1 * * * * root /usr/local/sbin/onewireMonitor.sh > /dev/null 2>&1
```

Actual commands

    git clone https://github.com/SkullKill/onewireMonitor
    cd onewireMonitor
    cp onewireMonitor* /usr/local/sbin/
    chmod +x /usr/local/sbin/onewireMonitor*
    ls /sys/bus/w1/devices/
    nano /usr/local/sbin/onewireMonitor_py3.py
    
    nano /etc/crontab
    
```
# monitor and start onewireMonitor is process is not running
*/1 * * * * root /usr/local/sbin/onewireMonitor.sh > /dev/null 2>&1
```

## notes

rpi has a limit of 16mA per gpio, with a total of 51mA for all gpio.

the DS18B20 sink a max of 4mA , so one gpio can technically power a maximum of 4 , although to be safe, might be better to stick to a max of 3



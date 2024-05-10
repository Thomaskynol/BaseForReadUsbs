import usb.core
import usb.util
import time
import os

dev = usb.core.find(idVendor=0x0079, idProduct=0x0006)

if dev is None:
    raise ValueError('Device not found')

ep = dev[0].interfaces()[0].endpoints()[0]
i = dev[0].interfaces()[0].bInterfaceNumber
dev.reset()

dev.default_timeout = 0

if dev.is_kernel_driver_active(i):
    dev.detach_kernel_driver(i)
    
dev.set_configuration()
eaddr = ep.bEndpointAddress 

try:
    while True:
        print(dev.read(eaddr, 1024))
 
except KeyboardInterrupt:
    print("\nInterrupção de teclado detectada. Encerrando o programa.")
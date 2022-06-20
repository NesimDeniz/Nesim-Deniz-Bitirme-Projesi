

import socket

import re

import subprocess
import sys
from datetime import datetime


ip_address_pattern = re.compile("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")



port_range_pattern = re.compile("([0-9]+)-([0-9]+)")



port_min = 0
port_max = 65535

open_ports = []



subprocess.call('cls', shell=True)



while True:
    ip_address_entered = input(" NESIM DENIZ PORT SCANNER \n Lutfen bir IP adresi giriniz... :  ")

    if ip_address_pattern.search(ip_address_entered):

        print(f"\n {ip_address_entered} Girilen IP adresi gecerli.\n")
        break

    else:
        print(f"\n {ip_address_entered} Girilen IP adresi gecersiz.\n")



while True:


    print("\n Lutfen tarama yapacaginiz port araligini yaziniz : (Ornek olarak 60-120)")
    
    port_range = input("\n Girilen port araligi : ")

    port_range_valid = port_range_pattern.search(port_range.replace(" ",""))

    if port_range_valid:

        port_min = int(port_range_valid.group(1))
        port_max = int(port_range_valid.group(2))
        break



print("")
print("_" * 60)
print(" Taraniyor, lutfen bekleyiniz...", ip_address_entered)
print("_" * 60)
print("")


scanStartTime = datetime.now()



for port in range(port_min, port_max + 1):
    
    try:


        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

            s.settimeout(0.5)


            s.connect((ip_address_entered, port))


            
            open_ports.append(port)

            print(f" Port {port}:      Open")

            s.close()
            

    except:

        print(f" Port {port}:      Close or Filtered")



scanEndTime = datetime.now()



totalScanTime = scanEndTime - scanStartTime



print(f"\n Tarama tamamlandi : {totalScanTime} \n")

for port in open_ports:

    print(f" Port {port} is open on {ip_address_entered}.")

print("")

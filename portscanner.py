#!/usr/bin/env python3

import socket
import subprocess
import sys
from datetime import datetime

subprocess.call('cls', shell=True)
remoteServer = input('Enter a remote host to scan\n')
remoteServerIP = socket.gethostbyname(remoteServer)
portRange = input('Enter a port number to scan for, or a range of ports.\nE.g. 80 or 1-1025\n')

timeStart = datetime.now()

if '-' in portRange:
    portRange = portRange.replace("-", " ").split()
    portRangeA = int(portRange[0])
    portRangeB = int(portRange[1]) + 1
else:
    portRangeA = int(portRange)
    portRangeB = int(portRange) + 1

def portinfo(currentport):
    return {
        1: '1 (TCPMUX)',
        5: '5 (RJE)',
        7: '7 (ECHO)',
        20: '20 (FTP-data)',
        21: '21 (FTP)',
        22: '22 (SSH)',
        23: '23 (TELNET)',
        25: '25 (SMTP)',
        42: '42 (NameServer)',
        80: '80 (HTTP)',
        115: '115 (SFTP)',
        443: '443 (HTTPS)',
        6667: '6667 (IRC)',
        8333: '8333 (Bitcoin)',
    }.get(currentport, currentport)

try:
    for port in range(portRangeA, portRangeB):
        print('Scanning remote host:', remoteServerIP, 'on port {} ... '.format(portinfo(port)), end="")
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((remoteServerIP, port))

        if result == 0:
            print("open!")
        else:
            print("closed.")
        sock.close()

except KeyboardInterrupt:
    print('You pressed Ctrl+C')
    sys.exit()

except socket.gaierror:
    print('Hostname could not be resolved.')
    sys.exit()

except socket.error:
    print("Couldn't connect to server")
    sys.exit()

timeEnd = datetime.now()
timeTotal = timeEnd - timeStart
print("\nScan completed in:", timeTotal)


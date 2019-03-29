# PortScanner
Simple port scanning tool written for usage in Python 3+.
  
Usage:  

$ portscanner.py  
  
Enter a remote host to scan  
$ www.simpan.se  
  
Enter a port number to scan for, or a range of ports.  
E.g. 80 or 1-1025  
$ 20-25  
  
Scanning remote host: 104.248.175.144 on port 20 (FTP-data) ... closed.  
Scanning remote host: 104.248.175.144 on port 21 (FTP) ... closed.  
Scanning remote host: 104.248.175.144 on port 22 (SSH) ... open!  
Scanning remote host: 104.248.175.144 on port 23 (TELNET) ... closed.  
Scanning remote host: 104.248.175.144 on port 24 ... closed.  
Scanning remote host: 104.248.175.144 on port 25 (SMTP) ... closed.  
  
Scan completed in: 0:01:45.218956

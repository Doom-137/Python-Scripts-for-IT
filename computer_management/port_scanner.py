import socket
import subprocess
import sys
from datetime import datetime

subprocess.call('clear', shell=True)

# Enter the IP address to scan
hostName    = raw_input("IP address: ")
hostNameIP  = socket.gethostbyname(hostName)

print "Scanning host", hostNameIP
timex = datetime.now()

try:
    for port in range(1,52000):  
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((hostNameIP, port))
        if result == 0:
            print "Port {}: \t Open".format(port)
        elif result == 10060:
            print "Port {}: \t Closed".format(port)
        sock.close()
		
except KeyboardInterrupt:
    sys.exit()
except socket.gaierror:
    print 'Hostname could not be resolved.'
    sys.exit()
except socket.error:
    print "Could not connect to host."
    sys.exit()
	
swatch = datetime.now()
total =  swatch - timex
print 'Scanning completed in: ', total

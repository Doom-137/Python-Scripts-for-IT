import socket
import struct
import urllib2
import os
"""
from urllib2 import Request, urlopen, URLError
"""
def wake_on_lan(macaddress):
    if len(macaddress) == 12:
        pass
    elif len(macaddress) == 12 + 5:
        sep = macaddress[2]
        macaddress = macaddress.replace(sep, '')
    else:
        raise ValueError('Incorrect MAC address format')
    data = ''.join(['FFFFFFFFFFFF', macaddress * 20])
    send_data = '' 
    for i in range(0, len(data), 2):
        send_data = ''.join([send_data,
                             struct.pack('B', int(data[i: i + 2], 16))])
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    sock.sendto(send_data, ('<broadcast>', 7))

	
#========================================================================
#PORT = 31337
#mgrossport = socket.socket()
#mgrossport.connect((IPADDRESS, PORT))
#========================================================================
i = 0
j = 0
iterList = []
loopDeeLoop = True
"""
DICTIONARY SETUP
[

['COMPUTERNAME', 'MAC ADDRESS', ['USER1', 'USER2', 'USER3']],
['COMPUTERNAME', 'MAC ADDRESS', ['USER1', 'USER2', 'USER3'], 'SERIALNUMBER', ]

]
"""
computerList = [


]
while loopDeeLoop:
	computerName = raw_input('$ command in << ')
	computerNameList = computerName.split()
	if computerName.lower() == 'exit':
		loopDeeLoop = False
	if (computerName.lower() == 'listall') or ((('list' in computerNameList) or ('LIST' in computerNameList)) and (('all' in computerNameList) or ('ALL' in computerNameList))) or (computerName.upper() == 'LAC'):
		print '$ comp >> Listing all computers...'
		while i < len(computerList):
			print '$ computer name out: %s' % (computerList[i][0])
			i += 1
		i = 0
	if computerName.lower() == 'wakeall':
		print '$ comp >> Waking all computers on the network...'
		while i < len(computerList):
			wake_on_lan(computerList[i][1])
			i += 1
		i = 0
	if (('list' in computerNameList) or ('LIST' in computerNameList)) and (('users' in computerNameList) or ('USERS' in computerNameList)):
		i = 0
		print '$ comp >> Listing all users on %s...' % (computerNameList[-1])
		while i < len(computerList):
			if computerNameList[-1] == computerList[i][0]:
				j = 0
				while j < len(computerList[i][2]):
					print '$ user >> %s' % (computerList[i][2][j])
					j += 1
			i += 1
		i = 0
	if (('serial' in computerNameList) or ('SERIAL' in computerNameList)) and (('number' in computerNameList) or ('NUMBER' in computerNameList)):
		i = 0
		print '$ comp >> Retrieving serial number...'
		while i < len(computerList):
			if computerNameList[-1] == computerList[i][0]:
				print '$ comp >> Computer Name: %s\n$ comp >> S/N: %s' % (computerNameList[-1], computerList[i][3])
			i += 1
	elif computerNameList[0] == 'users':
		i = 0
		while i < len(computerList):
			if computerNameList[1] == computerList[i][0]:
				j = 0
				while j < len(computerList[i][2]):
					print computerList[i][2][j]
					j += 1
			i += 1
	elif computerName.upper() == '':
		wake_on_lan('')
		
"""if __name__ == '__main__':
    wake_on_lan('0F0FDF0FBFEF')

    """

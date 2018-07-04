#!/usr/bin/env python
import socket
import struct
import sys

MCAST_GRP = sys.argv[1]
MCAST_PORT = sys.argv[2]
MCAST_PORT = int(MCAST_PORT)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind((MCAST_GRP, MCAST_PORT))  # use MCAST_GRP instead of '' to listen only
# to MCAST_GRP, not all groups on MCAST_PORT
mreq = struct.pack("4sl", socket.inet_aton(MCAST_GRP), socket.INADDR_ANY)

sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

sock.settimeout(3)

receive = 0
for i in range(0,4):
    try:
        data, address = sock.recvfrom(1024)
        #ip = address[0]
        #port = address[1]
        receive = receive+len(data)
        #print (len(data), ip, port, MCAST_GRP, MCAST_PORT)
    except socket.error, e:
        err = e.args[0]


if receive >= 3000:
    print ('UP')
else:
    print ('DOWN')


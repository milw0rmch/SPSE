"""
www.binarytides.com/python-packet-sniffer-code-linux/

x >> y returns x with the bits shifted to the right by y places. 
"""

#PF_PACKET operates on layer 2
#Ethernet header 14 bytes
#IP header 20-40 bytes

import socket
import struct
import binascii

#htons tells the kernel the desired protocol
rawSocket = socket.socket(socket.PF_PACKET,socket.SOCK_RAW,socket.htons(0x0800))

pkt = rawSocket.recvfrom(2048) #recv from method enables to read a packet

##<<====--- ETHERNET HEADER ====--->> 
ethernetHeader=pkt[0][0:14]

#https://docs.python.org/2/library/struct.html
# check above link for exclamation and s
eth_hdr = struct.unpack("!6s6s2s",ethernetHeader)
print eth_hdr

#hexlify will print all the above in hex

print binascii.hexlify(eth_hdr[0])
print binascii.hexlify(eth_hdr[1])
print binascii.hexlify(eth_hdr[2])

##<<====--- IP HEADER ---====>>
ipHeader=pkt[0][14:34]
ip_hdr = struct.unpack("!HHLLBBHHH", ipHeader)
#ntoa is network to ascii
version_ihl = ip_hdr[0]
version = version_ihl >> 4
ihl = version_ihl & 0xF
     
iph_length = ihl * 4
ttl = ip_hdr[5]
protocol = ip_hdr[6]
s_addr = socket.inet_ntoa(ip_hdr[8]);
d_addr = socket.inet_ntoa(ip_hdr[9]);
     
print 'Version : ' + str(version) + ' IP Header Length : ' + str(ihl) + ' TTL : ' + str(ttl) + ' Protocol : ' + str(protocol) + ' Source Address : ' + str(s_addr) + ' Destination Address : ' + str(d_addr)
     

##<<====--- TCP HEADER ---====>>
tcpHeader=pkt[0][34:54]
#www.binarytides.com/python-packet-sniffer-code-linux/
#www.stackoverflow/questions/20768107/regarding-struct-unpack-in-python
tcp_hdr=struct.unpack("!HH16s",tcpHeader)

sourcePort=tcp_hdr[0]
destinationPort=tcp_hdr[1]
print "Source Port: " + str(sourcePort)
print "Destination Port: " + str(destinationPort)
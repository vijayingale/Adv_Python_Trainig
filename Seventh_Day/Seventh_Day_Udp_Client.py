import socket

msgc = "hello udp"

byttos = str.encode(msgc)

serAddPort = ('127.0.0.1',20001)

buffsize =1024

ucs = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
ucs.sendto(byttos,serAddPort)
msgfser = ucs.recvfrom((buffsize))
msgfrc = "message from client{}".format(msgfser)
print(msgfrc)
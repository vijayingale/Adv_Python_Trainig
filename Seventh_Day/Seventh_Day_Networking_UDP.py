import socket

localIp = '127.0.0.1'

localport = 20001

bufferSize = 1024

msgFromServer = "Hello UPD Client"

bytesToString = str.encode(msgFromServer)

UDPSERVERSOCKET = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
UDPSERVERSOCKET.bind((localIp, localport))

print("UDP Server Up And Listening ......")

while True:
    byteAddressPair = UDPSERVERSOCKET.recvfrom(bufferSize)
    message = byteAddressPair[0]
    address = byteAddressPair[1]
    clientmsg = "Message From Client{}".format(message)
    clientIp = "client IP address:{}".format(address)

    print(clientmsg)
    print(clientIp)
    UDPSERVERSOCKET.sendto(bytesToString,address)

import socket

s= socket.socket()

host = '127.0.0.1'
port = 45454


with socket.socket(socket.AF_INET, socket.SOCK_STREAM):

    s.connect((host,port))
    s.sendall(b'hello world')
    data = s.recv(1024)
print( "Reseved From Server",repr(1024))


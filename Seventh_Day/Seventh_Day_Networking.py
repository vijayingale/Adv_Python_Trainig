import socket
host ='127.0.0.1'
port = 45454
with socket.socket(socket.AF_INET ,socket.SOCK_STREAM) as s:
    s.bind((host, port))
    s.listen()
    con, addr = s.accept()
    with con:
        print("connection done",addr)
        while True:
            data = con.recv(1024)
            print("Reseve From Client =>", data)
            if not data:
                break
            con.sendall(data)

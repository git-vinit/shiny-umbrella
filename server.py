import socket
s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(("localhost",8000))
s.listen(5)

while True:
    clientsocket,address=s.accept()
    print("connection from",address,"has been established !")
    clientsocket.send(bytes("welcome to the server","utf-8"))
    clientsocket.close()

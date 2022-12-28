import socket
s=socket.socket()
print("socket created successfully")
port =40674
s.bind(('',port))
print("socket binded to %s" %(port))
s.listen(5)
print("socket is listenning")
while True:
    c,addr=s.accept()
    print("got connection",addr)
    c.send(b'Thank you for connecting')
    c.close()
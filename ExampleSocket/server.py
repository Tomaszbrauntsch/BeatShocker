#EXAMPLE OF SENDING TEXT BACK TO CLIENT AND RECIEVING
#RAN ON THE
#
import socket

HOST = '192.168.50.206'                 # Symbolic name meaning the local host
PORT = 50007              # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept() #accpet requests
print 'Connected by', addr
while 1:
    data = conn.recv(1024) #recieve ip
    if not data: break
    conn.send("we good") #sends data that the client will connect
    print(data) #display information of ip
conn.close()

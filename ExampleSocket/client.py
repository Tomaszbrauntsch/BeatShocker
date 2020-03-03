#EXAMPLE OF SENDING TEXT AND RECIEVING
#RAN ON PC
#
import socket
message="whats up everything good"
HOST = '192.168.50.206'    # The remote host
PORT = 50007              # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.sendto(message.encode(),(HOST, PORT))
data = s.recv(1024) #recieving information from s (socket we are trying to connect prior)
s.close()
print ('Received', repr(data))

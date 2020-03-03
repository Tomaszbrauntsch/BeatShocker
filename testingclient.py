#EXAMPLE OF SENDING TEXT AND RECIEVING
#RAN ON PC
#
import socket
def mySend(text):
    userInput = text
    HOST = '192.168.50.206'    # The remote host
    PORT = 50007              # The same port as used by the server
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    s.sendto(userInput.encode(),(HOST, PORT))#sending the message to a host and port
    data = s.recv(1024) #recieving information from s (socket we are trying to connect prior)
    s.close()
    print (str(data)[2:-1]) #parses data recieved from server to remove extra bits not needed

userInput = input("Enter text or quit: ")
while (userInput != "quit"):
    mySend(userInput)
    userInput = input("Enter text or quit: ")

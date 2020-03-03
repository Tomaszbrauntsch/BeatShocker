#EXAMPLE OF SENDING TEXT BACK TO CLIENT AND RECIEVING
#RAN ON THE
#
import socket #recieve data from client
import RPi.GPIO #using GPIO pins on pi
from time import sleep #wait for a little

GPIO.setmode(GPIO.BCM)
shockPin = 17 #digital pin 17 | physical 11
GPIO.setup(shockPin, GPIO.OUT)
HOST = '192.168.50.206'                 # Symbolic name meaning the local host
PORT = 50007
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
while 1:              # Arbitrary non-privileged port
    s.listen(1)
    conn, addr = s.accept() #accpet requests
    data = conn.recv(1024) #recieve ip
    #if not data: break
    conn.send(data) #sends data that the client will connect
    print("SHOCKING")
    GPIO.output(shockPin, GPIO.HIGH)
    sleep(3)
    GPIO.output(shockPin, GPIO.LOW)
conn.close()

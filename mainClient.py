# import numpy as np
# from PIL import ImageGrab
# import cv2
#
# while(True):
#     printscreen_pil =  ImageGrab.grab()
#     printscreen_numpy =   np.array(printscreen_pil.getdata(),dtype='uint8')\
#     .reshape((printscreen_pil.size[1],printscreen_pil.size[0],3))
#     cv2.imshow('window',printscreen_numpy)
#     if cv2.waitKey(25) & 0xFF == ord('q'):
#         cv2.destroyAllWindows()
#         break
#
#config="tessedit_char_whitelist=-01234567890"
#397,267
#796,339
#bbox=(281,337,517,534)
#Regular
#310% is last time working
#
# import cv2
# import pytesseract
# #import pyscreenshot as ImageGrab
# cap = cv2.VideoCapture('test.mp4')
#
# text = pytesseract.image_to_string(img)
# print(text)

import numpy as np
import pyscreenshot as ImageGrab #Take image in game
import pytesseract #for text in game
import re #parse string
import socket #connect via internet to pi

#6,110
#788,770
#bbox=(6,110,788,770)
def internetShock(myMessage):
    message = myMessage
    HOST = '192.168.50.206'    # The remote host
    PORT = 50007              # The same port as used by the server
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    s.sendto(message.encode(),(HOST, PORT))#sending the message to a host and port
    data = s.recv(1024) #recieving information from s (socket we are trying to connect prior)
    s.close()
    print (str(data)[2:-1])

ComboAmount = 0
print("Starting!")
while True:
    img = ImageGrab.grab()
    img.save("frame.jpg")
    # save frame as JPEG file
    text = pytesseract.image_to_string("frame.jpg") #insert name of file
    digitSearch = re.findall(r'[0-9]+', text)
    if (len(digitSearch) > 0):
        print(digitSearch[0])
        if (int(digitSearch[0]) < ComboAmount):
            ComboAmount = 0
            internetShock("Shock")
        else:
            ComboAmount = int(digitSearch[0]) #NoShock

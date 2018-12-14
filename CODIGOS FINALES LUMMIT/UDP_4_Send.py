import socket
import math
import time
UDP_IP = "192.168.0.104"
UDP_PORT = 4210

sock = socket.socket(socket.AF_INET, # Internet
                      socket.SOCK_DGRAM) # UDP
for i in range(4):   
    
    loopA = int(100*(math.sin(2*math.pi*i/10)+1)/2)
    loopB = int(100*(math.sin(2*math.pi*i/10 + (120/(2*math.pi)))+1)/2)
    loopC = int(100*(math.sin(2*math.pi*i/10 - (120/(2*math.pi)))+1)/2)
    
    print loopA, loopB, loopC
    
    a = '@'
    green1 =50     #azul
    red1 = 50       #verde
    blue1 = 50     #rojo
    green2 = 50     #G
    red2 = 50       #R
    blue2 = 50      #B
    green3 = 50     #G
    red3 = 50     #R
    blue3 = 50      #B
    
    MESSAGE = a+chr(green1)+chr(red1)+chr(blue1)+chr(green2)+chr(red2)+chr(blue2)+chr(green3)+chr(red3)+chr(blue3)
         
#    print "UDP target IP:", UDP_IP
#    print "UDP target port:", UDP_PORT
#    print "message:", MESSAGE
    
    sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
    
    time.sleep(2)
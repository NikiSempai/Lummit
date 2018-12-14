import socket
import cv2 as cv
import numpy as np
import threading
import serial
import time
import math

UDP_IP = "169.254.114.98"
UDP_PORT = 5005


puerto1 = serial.Serial()#nombramos a la serial
puerto1.writeTimeout = 0
puerto1.port="COM5" #definimos puerto
puerto1.baudrate=230400#inicializamos el puerto de serie a 9600 baud
puerto1.open()#abrimos el puerto
time.sleep(1)

puerto2 = serial.Serial()#nombramos a la serial
puerto2.writeTimeout = 0
puerto2.port="COM9" #definimos puerto
puerto2.baudrate=230400#inicializamos el puerto de serie a 9600 baud
puerto2.open()#abrimos el puerto
time.sleep(1)

puerto3 = serial.Serial()#nombramos a la serial
puerto3.writeTimeout = 0
puerto3.port="COM3" #definimos puerto
puerto3.baudrate=230400#inicializamos el puerto de serie a 9600 baud
puerto3.open()#abrimos el puerto
time.sleep(1)

puerto4 = serial.Serial()#nombramos a la serial
puerto4.writeTimeout = 0
puerto4.port="COM6" #definimos puerto
puerto4.baudrate=230400#inicializamos el puerto de serie a 9600 baud
puerto4.open()#abrimos el puerto
time.sleep(1)


leds= [0 ,4 ,8 ,12 ,16 ,20 ,24 ,28 ,32 ,36 ,40 ,44 ,48 ,52 ,56,
      63,67 ,71 ,75 ,79 ,83 ,87 ,91 ,95 ,99 ,103 ,107 ,111 ,115 ,119,
      120, 124, 128, 132, 136, 140, 144, 148, 152, 156, 160, 164, 168, 172, 176, 
      183, 187, 191, 195, 199, 203, 207, 211, 215, 219, 223, 227, 231, 235, 239, 
      240, 244, 248, 252, 256, 260, 264, 268, 272, 276, 280, 284, 288, 292, 296, 
      303, 307, 311, 315, 319, 323, 327, 331, 335, 339, 343, 347, 351, 355, 359, 
      360, 364, 368, 372, 376, 380, 384, 388, 392, 396, 400, 404, 408, 412, 416, 
      423, 427, 431, 435, 439, 443, 447, 451, 455, 459, 463, 467, 471, 475, 479, 
      480, 484, 488, 492, 496, 500, 504, 508, 512, 516, 520, 524, 528, 532, 536, 
      543, 547, 551, 555, 559, 563, 567, 571, 575, 579, 583, 587, 591, 595, 599, 
      600, 604, 608, 612, 616, 620, 624, 628, 632, 636, 640, 644, 648, 652, 656, 
      663, 667, 671, 675, 679, 683, 687, 691, 695, 699, 703, 707, 711, 715, 719, 
      720, 724, 728, 732, 736, 740, 744, 748, 752, 756, 760, 764, 768, 772, 776, 
      783, 787, 791, 795, 799, 803, 807, 811, 815, 819, 823, 827, 831, 835, 839,
      840, 844, 848, 852, 856, 860, 864, 868, 872, 876, 880, 884, 888, 892, 896]







#######CAMBIO DE TAMAÑO########
fil = 15
col = 15
##############################
timeh = 0 

####transformo a arreglo numpy y luego cambio dimensiones para enviar###
def transfoarduino(imgin):
    #invierto columnas pares
    
    impar = imgin[:,1:14:2,:]
    par = imgin[:,0:15:2,:]
    impar = np.flipud(impar)
    
    total = np.zeros((imgin.shape),dtype=imgin.dtype)
    total[:,0:15:2,:] = par
    total[:,1:14:2,:] = impar
    
    total = np.flipud(total)
    return total

def capa1y2(red1, green1, blue1, red2, green2, blue2):
    #ESCRIBO EN PUERTO SERIAL PARA CADA ELEMENTO DE CADA ARRAY
    arroba = '@'
    for i in leds:
        byte1 = int(i/256)
        byte0 = i%256
        stringFin = arroba+chr(byte1)+chr(byte0)+chr(red1[int(math.floor(i/4))])+chr(green1[int(math.floor(i/4))])+chr(blue1[int(math.floor(i/4))])
        puerto1.write (bytes(stringFin))
    
    for i in leds:
        byte1 = int((i+900)/256)
        byte0 = (i+900)%256
        stringFin = arroba+chr(byte1)+chr(byte0)+chr(red2[int(math.floor(i/4))])+chr(green2[int(math.floor(i/4))])+chr(blue2[int(math.floor(i/4))])
        puerto1.write (bytes(stringFin))
        
    time_hilo1 = time.time() - timeh
#    print "time_hilo1:", time_hilo1
    
def capa3y4(red3, green3, blue3, red4, green4, blue4):
    #ESCRIBO EN PUERTO SERIAL PARA CADA ELEMENTO DE CADA ARRAY
    arroba = '@'
    for i in leds:
        byte1 = int(i/256)
        byte0 = i%256
        stringFin = arroba+chr(byte1)+chr(byte0)+chr(red3[int(math.floor(i/4))])+chr(green3[int(math.floor(i/4))])+chr(blue3[int(math.floor(i/4))])
        puerto2.write (bytes(stringFin))
    
    for i in leds:
        byte1 = int((i+900)/256)
        byte0 = (i+900)%256
        stringFin = arroba+chr(byte1)+chr(byte0)+chr(red4[int(math.floor(i/4))])+chr(green4[int(math.floor(i/4))])+chr(blue4[int(math.floor(i/4))])
        puerto2.write (bytes(stringFin))
        
    time_hilo2 = time.time() - timeh
#    print "time_hilo2:", time_hilo2
    
def capa5y6(red5, green5, blue5, red6, green6, blue6):
    #ESCRIBO EN PUERTO SERIAL PARA CADA ELEMENTO DE CADA ARRAY
    arroba = '@'
    for i in leds:
        byte1 = int(i/256)
        byte0 = i%256
        stringFin = arroba+chr(byte1)+chr(byte0)+chr(red5[int(math.floor(i/4))])+chr(green5[int(math.floor(i/4))])+chr(blue5[int(math.floor(i/4))])
        puerto3.write (bytes(stringFin))
    
    for i in leds:
        byte1 = int((i+900)/256)
        byte0 = (i+900)%256
        stringFin = arroba+chr(byte1)+chr(byte0)+chr(red6[int(math.floor(i/4))])+chr(green6[int(math.floor(i/4))])+chr(blue6[int(math.floor(i/4))])
        puerto3.write (bytes(stringFin))
    
    time_hilo3 = time.time() - timeh
#    print "time_hilo3:", time_hilo3

def capa7y8(red7, green7, blue7, red8, green8, blue8):
    #ESCRIBO EN PUERTO SERIAL PARA CADA ELEMENTO DE CADA ARRAY
    arroba = '@'
    for i in leds:
        byte1 = int(i/256)
        byte0 = i%256
        stringFin = arroba+chr(byte1)+chr(byte0)+chr(red7[int(math.floor(i/4))])+chr(green7[int(math.floor(i/4))])+chr(blue7[int(math.floor(i/4))])
        puerto4.write (bytes(stringFin))
    
    for i in leds:
        byte1 = int((i+900)/256)
        byte0 = (i+900)%256
        stringFin = arroba+chr(byte1)+chr(byte0)+chr(red8[int(math.floor(i/4))])+chr(green8[int(math.floor(i/4))])+chr(blue8[int(math.floor(i/4))])
        puerto4.write (bytes(stringFin))
    
    time_hilo4 = time.time() - timeh
#    print "time_hilo4:", time_hilo4
        
sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))


while 1:
   
#    vid1 = cv.VideoCapture("video4.mp4")
#    vid2 = cv.VideoCapture("video4.mp4")
#    vid3 = cv.VideoCapture("video4.mp4")
#    vid4 = cv.VideoCapture("video4.mp4")
#    vid5 = cv.VideoCapture("video4.mp4")
#    vid6 = cv.VideoCapture("video4.mp4")
#    vid7 = cv.VideoCapture("video4.mp4")
#    vid8 = cv.VideoCapture("video4.mp4")
    vid1 = cv.VideoCapture("2.mp4")
    vid2 = cv.VideoCapture("1.mp4")
    vid3 = cv.VideoCapture("3.mp4")
    vid4 = cv.VideoCapture("4.mp4")
    vid5 = cv.VideoCapture("5.mp4")
    vid6 = cv.VideoCapture("6.mp4")
    vid7 = cv.VideoCapture("7.mp4")
    vid8 = cv.VideoCapture("8.mp4") 
    
    MAXFRAME = 750
    frame = 0
    while 1:
        time0 = time.time()
        data, addr = sock.recvfrom(20) # buffer size is 1024 bytes
        time_udp_lecutre_sin_send = time.time()-time0
#        print "time_udp_lecutres sin send:", time_udp_lecutre_sin_send
#        print "received message:", data
        ledstracking = data.split(',') #array con los numeros de led del tracking
        
        for i in range(0,5):
            
            
            byte0 = int((int(ledstracking[i])/256))
            byte1 = (int(ledstracking[i]))%256
            byte2 = int(((int(ledstracking[i])+900)/256))
            byte3 = int((int(ledstracking[i])+900)%256)
            stringFin = "@"+chr(byte0)+chr(byte1)+chr(0)+chr(0)+chr(220)
            stringFin2 = "@"+chr(byte2)+chr(byte3)+chr(0)+chr(0)+chr(220)
            puerto1.write (bytes(stringFin))
            puerto1.write (bytes(stringFin2))
            puerto2.write (bytes(stringFin))
            puerto2.write (bytes(stringFin2))
            puerto3.write (bytes(stringFin))
            puerto3.write (bytes(stringFin2))
            puerto4.write (bytes(stringFin))
            puerto4.write (bytes(stringFin2))
            
            
        puerto1.write (bytes("Send !"))
        puerto2.write (bytes("Send !"))
        puerto3.write (bytes("Send !"))
        puerto4.write (bytes("Send !"))
        
        time_udp_lecutre_mas_send = time.time()-time0
#        print "time_udp_lecutre+send:", time_udp_lecutre_mas_send
          
        time1 = time.time()
        
        ret, frame1 = vid1.read()
        ret, frame2 = vid2.read()
        ret, frame3 = vid3.read()
        ret, frame4 = vid4.read()
        ret, frame5 = vid5.read()
        ret, frame6 = vid6.read()
        ret, frame7 = vid7.read()
        ret, frame8 = vid8.read()
        
        framelow1 = cv.resize(frame1,(col,fil))
        framelow2 = cv.resize(frame2,(col,fil))
        framelow3 = cv.resize(frame3,(col,fil))
        framelow4 = cv.resize(frame4,(col,fil))
        framelow5 = cv.resize(frame5,(col,fil))
        framelow6 = cv.resize(frame6,(col,fil))
        framelow7 = cv.resize(frame7,(col,fil))
        framelow8 = cv.resize(frame8,(col,fil))
        #cv.imshow('low1',framelow1)
#        cv.imshow('low2',framelow2)
#        cv.imshow('low3',framelow3)
#        cv.imshow('low4',framelow4)
        
        matrizPronta1 = transfoarduino(framelow1) #matriz con las columnas invertidas
        matrizPronta2 = transfoarduino(framelow2) #matriz con las columnas invertidas
        matrizPronta3 = transfoarduino(framelow3) #matriz con las columnas invertidas
        matrizPronta4 = transfoarduino(framelow4) #matriz con las columnas invertidas
        matrizPronta5 = transfoarduino(framelow5) #matriz con las columnas invertidas
        matrizPronta6 = transfoarduino(framelow6) #matriz con las columnas invertidas
        matrizPronta7 = transfoarduino(framelow7) #matriz con las columnas invertidas
        matrizPronta8 = transfoarduino(framelow8) #matriz con las columnas invertidas
        red1 = np.ravel(matrizPronta1[:,:,0],order="F")
        green1 = np.ravel(matrizPronta1[:,:,1],order="F")
        blue1 = np.ravel(matrizPronta1[:,:,2],order="F")
        
        red2 = np.ravel(matrizPronta2[:,:,0],order="F")
        green2 = np.ravel(matrizPronta2[:,:,1],order="F")
        blue2 = np.ravel(matrizPronta2[:,:,2],order="F")
        
        red3 = np.ravel(matrizPronta3[:,:,0],order="F")
        green3 = np.ravel(matrizPronta3[:,:,1],order="F")
        blue3 = np.ravel(matrizPronta3[:,:,2],order="F")
        
        red4 = np.ravel(matrizPronta4[:,:,0],order="F")
        green4 = np.ravel(matrizPronta4[:,:,1],order="F")
        blue4 = np.ravel(matrizPronta4[:,:,2],order="F")
        
        red5 = np.ravel(matrizPronta5[:,:,0],order="F")
        green5 = np.ravel(matrizPronta5[:,:,1],order="F")
        blue5 = np.ravel(matrizPronta5[:,:,2],order="F")
        
        red6 = np.ravel(matrizPronta6[:,:,0],order="F")
        green6 = np.ravel(matrizPronta6[:,:,1],order="F")
        blue6 = np.ravel(matrizPronta6[:,:,2],order="F")
        
        red7 = np.ravel(matrizPronta5[:,:,0],order="F")
        green7 = np.ravel(matrizPronta5[:,:,1],order="F")
        blue7 = np.ravel(matrizPronta5[:,:,2],order="F")
        
        red8 = np.ravel(matrizPronta8[:,:,0],order="F")
        green8 = np.ravel(matrizPronta8[:,:,1],order="F")
        blue8 = np.ravel(matrizPronta8[:,:,2],order="F")
        
        time_video_a_RGB = time.time() - time1
        print "time_video_a_RGB:", time_video_a_RGB

        
        time2 =time.time()
        
        hilo1 = threading.Thread(target=capa1y2(red1, green1, blue1, red2, green2, blue2))
        hilo2 = threading.Thread(target=capa3y4(red3, green3, blue3, red4, green4, blue4))
        hilo3 = threading.Thread(target=capa5y6(red5, green5, blue5, red6, green6, blue6))
        hilo4 = threading.Thread(target=capa7y8(red7, green7, blue7, red8, green8, blue8))
        
        inicializacion_hilos = time.time() - time2
#        print "inicializacion_hilos:", inicializacion_hilos
        
        timeh =time.time()
        
        #hilo1.start()
#        hilo2.start()
#        hilo3.start()
#        hilo4.start()
        
        time_picado_enviado = time.time() - time2
#        print "time_picado_enviado:", time_picado_enviado
        
        frame = frame +1
        if frame == MAXFRAME : break
    
        time_tot = time.time() - time0
        print "time_tot:", time_tot
    vid1.release()




cv.destroyAllWindows()

cv.waitKey(0)
cv.destroyAllWindows()


#########CERRAR PUERTOS#######
puerto1.close()
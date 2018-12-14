from imutils import contours
from skimage import measure
import imutils
import cv2
import cv2 as cv
import numpy as np
import time
import socket
UDP_IP = "169.254.114.98"
UDP_PORT = 5005

cap = cv2.VideoCapture(0)
arraytrackeo = np.array([[0 ,4 ,8 ,12 ,16 ,20 ,24 ,28 ,32 ,36 ,40 ,44 ,48 ,52 ,56],
      [119,115 ,111 ,107 ,103 ,99 ,95 ,91 ,87 ,83 ,79 ,75 ,71 ,67 ,63],
      [120, 124, 128, 132, 136, 140, 144, 148, 152, 156, 160, 164, 168, 172, 176], 
      [239, 235, 231, 227, 223, 219, 215, 211, 207, 203, 199, 195, 191, 187, 283], 
      [240, 244, 248, 252, 256, 260, 264, 268, 272, 276, 280, 284, 288, 292, 296], 
      [359, 355, 351, 347, 343, 339, 335, 331, 327, 323, 319, 315, 311, 307, 303], 
      [360, 364, 368, 372, 376, 380, 384, 388, 392, 396, 400, 404, 408, 412, 416], 
      [479, 475, 471, 467, 463, 459, 455, 451, 447, 443, 439, 435, 431, 427, 423], 
      [480, 484, 488, 492, 496, 500, 504, 508, 512, 516, 520, 524, 528, 532, 536], 
      [599, 595, 591, 587, 587, 583, 579, 575, 571, 567, 563, 559, 555, 551, 547], 
      [600, 604, 608, 612, 616, 620, 624, 628, 632, 636, 640, 644, 648, 652, 656], 
      [719, 715, 711, 707, 703, 699, 695, 691, 687, 683, 679, 675, 671, 667, 663], 
      [720, 724, 728, 732, 736, 740, 744, 748, 752, 756, 760, 764, 768, 772, 776], 
      [839, 835, 831, 827, 823, 819, 815, 811, 807, 803, 799, 795, 791, 787, 783],
      [840, 844, 848, 852, 856, 860, 864, 868, 872, 876, 880, 884, 888, 892, 896]])

x_map=0
y_map=0
count = 0
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

while(True):
    
    ##############TRACKING#################
    #Leemos lo que llega de la cámara
    (grabbed, image) = cap.read()
    #pprint (grabbed)
	# if we are viewing a video and we did not grab a frame,
	# then we have reached the end of the video
    if not grabbed:
        print ("No hay video")
        break
    
    # convertimos el frame a escala de grises y le hacemos blur
    
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (11, 11), 0)
    
    # seteamos un threshold en la imagen para revelar las zonas de la imagen 
    # blureada que tienen luz 
    thresh = cv2.threshold(blurred, 210, 255, cv2.THRESH_BINARY)[1]
    
    # perform a series of erosions and dilations to remove
    # any small blobs of noise from the thresholded image
    thresh = cv2.erode(thresh, None, iterations=2)
    thresh = cv2.dilate(thresh, None, iterations=4)
    
    # perform a connected component analysis on the thresholded
    # image, then initialize a mask to store only the "large"
    # components
    labels = measure.label(thresh, neighbors=8, background=0)
    mask = np.zeros(thresh.shape, dtype="uint8")
    
    # loop over the unique components
    for label in np.unique(labels):
    	# if this is the background label, ignore it
    	if label == 0:
    		continue
    
    	# otherwise, construct the label mask and count the
    	# number of pixels 
    	labelMask = np.zeros(thresh.shape, dtype="uint8")
    	labelMask[labels == label] = 255
    	numPixels = cv2.countNonZero(labelMask)
    
    	# if the number of pixels in the component is sufficiently
    	# large, then add it to our mask of "large blobs"
    	if numPixels > 450:
    		mask = cv2.add(mask, labelMask)
    
    # find the contours in the mask, then sort them from left to
    # right
    cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
    	cv2.CHAIN_APPROX_SIMPLE)
    
    
    cnts = cnts[0] if imutils.is_cv2() else cnts[1]

    
    if len( cnts ) > 0:    
        
        cnts = contours.sort_contours(cnts)[0]
        
        # loop over the contours
        for (i, c) in enumerate(cnts):
            # draw the bright spot on the image
            (x, y, w, h) = cv2.boundingRect(c)
            ((cX, cY), radius) = cv2.minEnclosingCircle(c)
#            print('cX:')
#            print(i+1 , cX)
#            print('cY:')
#            print(i+1 , cY)
            
            cv2.circle(image, (int(cX), int(cY)), int(radius),
        		(0, 0, 255), 3)
            cv2.putText(image, "#{}".format(i + 1), (x, y - 15),
                     
        		cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 0, 255), 2)
            
            #Convierto los valores de x e y a enteros 
            # y los mapeo de 1 a 15 para mandarlos ¡¡¡FALTA ESTO!!!
            
            xt = int(cX)
            yt = int(cY)
            
                ###MAPEO######
            y_map=abs(int((round(yt * 14 / 480)))-14)
            if xt>0 and xt<111:
                x_map=14
            elif xt>529 and xt<640:
                x_map=0
            else:
                x_map=abs(int((round((xt - 111) * 14 / 418))-14))
        
        
    # show the output image
    
    cv2.imshow("image", image)
    
    
    key = cv2.waitKey(1) & 0xFF
    led = int(arraytrackeo[x_map,y_map])
    if x_map == 0:
#        led5 = int(arraytrackeo[x_map,y_map])
        led2 = int(arraytrackeo[x_map,y_map])
#        led3 = int(arraytrackeo[x_map,y_map-1])
#        led4 = int(arraytrackeo[x_map,y_map+1])
    else:
        led2 = int(arraytrackeo[x_map-1,y_map])
    if x_map == 14:
#        led2 = int(arraytrackeo[x_map,y_map])
        led3 = int(arraytrackeo[x_map,y_map])
#        led4 = int(arraytrackeo[x_map,y_map+1])
#        led5 = int(arraytrackeo[x_map+1,y_map])
    else:
        led3 = int(arraytrackeo[x_map+1,y_map])
    if y_map == 0:
        led4 = int(arraytrackeo[x_map,y_map])
#        led2 = int(arraytrackeo[x_map-1,y_map])
#        led3 = int(arraytrackeo[x_map,y_map-1])
#        led5 = int(arraytrackeo[x_map+1,y_map])
    else:
        led4 = int(arraytrackeo[x_map,y_map-1])
    if y_map == 14:
#        led3 = int(arraytrackeo[x_map,y_map])
#        led4 = int(arraytrackeo[x_map,y_map+1])
         led5 = int(arraytrackeo[x_map,y_map])
#        led2 = int(arraytrackeo[x_map-1,y_map])
    else:
         led5 = int(arraytrackeo[x_map,y_map+1])
        
        
    
    #ledstracking = [led ,led2 ,led3 ,led4 ,led5]
    
    time0 = time.time()
    MESSAGE = str(led)+","+str(led2)+","+str(led3)+","+str(led4)+","+str(led5)
    print(MESSAGE)
    sock = socket.socket(socket.AF_INET, # Internet
                          socket.SOCK_DGRAM) # UDP
    count = count + 1
    if count==3:
        sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
        time_enviado_udp= time.time() - time0
        print "time_enviado_udp:" , time_enviado_udp
        count=0
        print(led)
    #s.close()
    
    if key == ord("q"):
        break
       
cv.waitKey(0)
cv.destroyAllWindows()
s.close()
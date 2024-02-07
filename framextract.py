import cv2
import os
# Create a VideoCapture object and read from input file
# If the input is the camera, pass 0 instead of the video file name
filename="1.mp4"
cam = cv2.VideoCapture(filename)
filename=filename[:-4]
if not os.path.exists(filename):
    os.mkdir(filename)
c=0;
w=150
h=150


class CoordinateStore:
    def __init__(self):
        self.points = [0,0]

    def select_point(self,event,x,y,flags,param):
            if event == cv2.EVENT_MOUSEMOVE:
                self.points[0]=x
                self.points[1]=y               
#                cv2.circle(frame,(x,y),100,(255,0,0),3)
#                self.points.append((x,y))


#instantiate class
coordinateStore1 = CoordinateStore()


# Check if camera opened successfully
if (cam.isOpened()== False): 
  print("Error opening video stream or file")
wk=int(cam.get(5))
# Read until video is completed
flag=0
big=0
a={1:'On',0:'Off'}
while(cam.isOpened()):
  # Capture frame-by-frame
  ret, frame = cam.read()
  if ret == True:
    k=cv2.waitKey(1)
    # Display the resulting frame
#    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#    cv2.imshow('Frame',gray)
#    frame = cv2.resize(frame, (1350,680))
    frame = cv2.resize(frame, (720,480))
    frame = cv2.transpose(frame);
    frame =cv2.flip( frame, 1 )
    cv2.rectangle(frame,(coordinateStore1.points[0]-h,coordinateStore1.points[1]-w),(coordinateStore1.points[0]+w,coordinateStore1.points[1]+h),(225,0,0),2)
    cv2.putText(frame, "Small Capture= "+a[flag],(10, 680),cv2.FONT_HERSHEY_COMPLEX_SMALL,.8,(225,255,0)) 
    cv2.putText(frame, "Full Capture= "+a[big],(10, 700),cv2.FONT_HERSHEY_COMPLEX_SMALL,.8,(225,255,0)) 
    cv2.imshow('Frame',frame)
    cv2.setMouseCallback('Frame',coordinateStore1.select_point)
    if k ==ord('c'):
        big=0
        if flag==0:
            flag=1
        else:
            flag=0
    elif k ==ord('C'):
        flag=0
        if big==0:
            big=1
        else:
            big=0
#        cv2.imwrite(filename+'/'+str(c)+'.jpg', frame[coordinateStore1.points[1]-h:coordinateStore1.points[1]+h,coordinateStore1.points[0]-w:coordinateStore1.points[0]+w])
#    cv2.imwrite(filename+'/'+str(c)+'.jpg', frame)
#        c += 1
    elif k == ord('u'):
        h+=10
        w+=10
    elif k == ord('d'):
        h-=10
        w-=10
    elif k == 32:
        cv2.waitKey(0)==32
#        ret=True
    # Press Q on keyboard to  exit
    elif k & 0xFF == ord('q'):
      break
    y1=coordinateStore1.points[1]-h
    y2=coordinateStore1.points[1]+h
    x1=coordinateStore1.points[0]-w
    x2=coordinateStore1.points[0]+w
    if y1<0:
        y1=0
    if x1<0:
        x1=0
#    if y2>680:
#        y2=680
#    if x2<1350:
#        x2=1350
    if flag==1:
#        print(y1,y2,x1,x2)
        cv2.imwrite(filename+'/'+str(c)+'.jpg', frame[y1:y2,x1:x2])
        c+=1
    elif big==1:
        cv2.imwrite(filename+'/'+str(c)+'.jpg', frame)
        c+=1
  # Break the loop
  else: 
    break
# When everything done, release the video capture object
cam.release()
# Closes all the frames
cv2.destroyAllWindows()


#Upkey : 2490368
#DownKey : 2621440
#LeftKey : 2424832
#RightKey: 2555904
#Space : 32
#Delete : 3014656





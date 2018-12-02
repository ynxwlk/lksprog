from numpy import *
import cv2
from matplotlib import pyplot as plt
from pylab import *

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
img=zeros((4960,3508,3))    #A3 4960*3508 A4 2480*3508
#cv2.line(img,(0,0),(512,512),(0,255,255))#起点（0,0）终点(512，512)颜色（0,255,255）
#cv2.rectangle(img,(150,150),(350,350),(255,255,0),2)#左上角（0,0）右下角(512，512)颜色（255,255,0）
#cv2.ellipse(img,(255,350),(100,50),0,0,360,(255,255,0),2)#椭圆
#cv2.circle(img,(255,255),60,(0,255,255),2)#圆
#pts=array([[50,100],[150,150],[170,120],[250,210],[250,310]])#多边形
#cv2.polylines(img,[pts],True,(255,0,255),2)
font=cv2.FONT_HERSHEY_SIMPLEX#文字
cv2.putText(img,"建设单位hahaha.....",(0,455),font,2,(255,255,255),2)

cv2.imshow("image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

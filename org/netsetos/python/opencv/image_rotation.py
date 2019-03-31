import cv2
import numpy as np
pic=cv2.imread('/home/tanu/Downloads/IMG-20180204-WA0023.jpg')
cols=pic.shape[0]
rows=pic.shape[1]
center=(cols/2,rows/2)
angle=360

M=cv2.getRotationMatrix2D(center,angle,1)

rotate=cv2.warpAffine(pic,M,(cols,rows))
cv2.imshow('Rotated',rotate)

cv2.waitKey(0)
cv2.destroyAllWindows()

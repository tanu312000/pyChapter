import cv2

#load test iamge
test1 = cv2.imread('/home/tanu/imagecv/pp1.jpeg')
#convert the test image to gray image as opencv face detector expects gray images
gray_img = cv2.cvtColor(test1, cv2.COLOR_BGR2GRAY)
1
2
3
4
#load test iamge
test1 = cv2.imread('/home/tanu/imagecv/pp1.jpeg')
#convert the test image to gray image as opencv face detector expects gray images
gray_img = cv2.cvtColor(test1, cv2.COLOR_BGR2GRAY)

cv2.imwrite('/home/tanu/imagecv/gray_image.png', gray_img)




# or display the gray image using OpenCV
cv2.imshow('Test Imag', gray_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

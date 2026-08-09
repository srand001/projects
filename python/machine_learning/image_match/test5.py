#https://www.tutorialspoint.com/how-to-compare-two-images-in-opencv-python

# import required libraries
import cv2 as cv
import numpy as np

# load the input images
img1 = cv.imread("images/1/image1.png", cv.IMREAD_GRAYSCALE)    # queryImage

#img2 = cv.imread("images/1/image1.png", cv.IMREAD_GRAYSCALE)    #

#img2 = cv.imread("images/1/image2a.png", cv.IMREAD_GRAYSCALE)

#img2 = cv.imread("images/1/image2b1.png", cv.IMREAD_GRAYSCALE)
#img2 = cv.imread("images/1/image2b2.png", cv.IMREAD_GRAYSCALE)
#img2 = cv.imread("images/1/image2b3.png", cv.IMREAD_GRAYSCALE)

#img2 = cv.imread("images/1/image3a.png", cv.IMREAD_GRAYSCALE)

img2 = cv.imread("images/1/image4a.png", cv.IMREAD_GRAYSCALE)    #

#img2 = cv.imread("images/1/image100a.png", cv.IMREAD_GRAYSCALE) 


# define the function to compute MSE between two images
def mse(img1, img2):
   h, w = img1.shape
   diff = cv.subtract(img1, img2)
   err = np.sum(diff**2)
   mse = err/(float(h*w))
   return mse, diff

error, diff = mse(img1, img2)
print("Image matching Error between the two images:",error)

cv.imshow("difference", diff)
cv.waitKey(0)
cv.destroyAllWindows()
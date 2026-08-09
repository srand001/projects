
import cv2

# https://www.youtube.com/watch?v=PObhsp1pEaQ

image1 = cv2.imread("images/1/image1.png", cv2.IMREAD_COLOR)
image2 = cv2.imread("images/1/image1.png", cv2.IMREAD_COLOR)

if image1.shape == image2.shape:
  difference = cv2.subtract(image1, image2)
  b,g,r = cv2.split(difference)
	
  if cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0:
    print("Same match")
  else:
    print("Different")

print("End")

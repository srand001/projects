
# Display an image

import cv2

print("Test1")

img = cv2.imread("images/1/image1.png", cv2.IMREAD_COLOR)

# cv2.IMREAD_COLOR - Loads a colour image wihout any transparency
# cv2.IMREAD_GRAYSCALE - Loads in grayscale mode
# cv2.IMREAD_UNCHANGED - Loads image with alpha channel with transparency

cv2.imshow("window title", img)

cv2.waitKey(0)

cv2.destroyAllWindows()

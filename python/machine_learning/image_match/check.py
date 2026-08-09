import cv2 as cv # OpenCV - Open Source Computer Vision
import numpy as np # NumPy - Library for  Python, adding support for large, multi-dimensional arrays and matrices
import os # Operating system
from matplotlib import pyplot as plt

# Simple comparison test
def check1(file1, file2):
	file_location = '/srv/volume1/data/eds/eds_report.csv'
	file_name1 = os.path.basename(file1)
	file_name2 = os.path.basename(file2)

	print("Check {},{} ".format(file_name1, file_name2), end="")
	image1 = cv.imread(file1, cv.IMREAD_COLOR)
	image2 = cv.imread(file2, cv.IMREAD_COLOR)

	ret = 0 # Note: 100 = 100% match
	tolerance1 = 10 # Number of pixels allowed to be different for matching simple images
	tolerance2 = 100 # Number of pixels allowed to be different for matching complex images

	# Resize image has been added
	if image1.shape != image2.shape:
		# interpolation method
		h, w = image1.shape[:2]
		sh, sw = image2.shape[:2]

		if sh > h or sw > w:  # shrinking image
			interp = cv.INTER_AREA
		else:  # stretching image
			interp = cv.INTER_CUBIC

		image2 = cv.resize(image1, (w, h), interpolation=interp)
		print("Image resized", end="")

	# Subtract two images by OpenCV function. Both images should be of same size.
	difference = cv.subtract(image1, image2)

	# Using OpenCV split() to split channels of coloured image
	b, g, r = cv.split(difference)

	print("bgr", cv.countNonZero(b), cv.countNonZero(g), cv.countNonZero(r), end=" ")

	# total number of different pixels between im1 and im2
	print ("PDif", np.sum(image1 != image2), end=" ")

	if cv.countNonZero(b) == 0 and cv.countNonZero(g) == 0 and cv.countNonZero(r) == 0:
		print("SameMatch", end=" ")

		img1 = cv.imread(file1, cv.IMREAD_GRAYSCALE)
		n_white_pix1 = np.sum(img1 == 255)
		print('NumWhite1', n_white_pix1, end=" ")

		img2 = cv.imread(file2, cv.IMREAD_GRAYSCALE)
		n_white_pix2 = np.sum(img2 == 255)
		print('NumWhite2', n_white_pix2, end=" ")

		diffWhite = abs(n_white_pix1 - n_white_pix2)
		print('Diff white', diffWhite, end=" ")

		if (diffWhite == 0):
			ret = 100
		elif ( diffWhite < tolerance2):
			ret = 99
	elif cv.countNonZero(b) < tolerance1 and cv.countNonZero(g) < tolerance1 and cv.countNonZero(r) < tolerance1:
		print("SimilarMatch", end="")
		ret = 99
	elif cv.countNonZero(b) < tolerance2 and cv.countNonZero(g) < tolerance2 and cv.countNonZero(r) < tolerance2:
		print("CloseMatch", end="")
		ret = check2(image1, image2) # More complex test

	print("->", ret)
	return ret

# More complex tests
def check2(image1, image2):
	ret = 0

	finder = cv.ORB_create()

	# find the keypoints and descriptors with SIFT
	kp1, des1 = finder.detectAndCompute(image1, None)
	kp2, des2 = finder.detectAndCompute(image2, None)

	bf = cv.BFMatcher(cv.NORM_HAMMING, crossCheck=True)
	# Match descriptors.
	matches = bf.match(des1, des2)
	# print(matches)
	# Sort them in the order of their distance.
	matches = sorted(matches, key=lambda x: x.distance)

	# Apply ratio test
	good = []

	for m in matches:
		if m.distance < 2.5:
			good.append([m])

	print("Found %d Matches" % (len(good)), end=" ")

	if len(good) >= 6:
		ret = 95

	return ret

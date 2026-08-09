import cv2
import sys
import create_csv
import pandas as pd
import numpy as np
import os, os.path

list_names = [] # List of folder names corresponding to different faces

# This program will try and match a face to a set of known images stored in a data folder 
# called 'training_data'.

# Notes: If you are adding a new face, please delete the folder called 'training_faces' and add
# the new face in the 'training_data' in sub directory with the name of the person.
# Example: Pictures of 'Leo DiCaprio' are stored in folder 'training_data\leo'

# To run the program from a command line to match an image called 'test1.jpg' use:
# python face_recog.py test1.jpg

# Surjit Randhawa 2022

test_file = "test1.jpg";

if len(sys.argv) < 2:
	if (os.path.exists(test_file)):
		test_img =  "test1.jpg";
	else:
		print ("Please add Test Image Path")
	sys.exit()
else:
	test_img = sys.argv[1]

# A Haar-Cascade file is a data file saved in XML format that stores a pre-trained machine learning model
# used for object detection. It holds mathematical values for Haar-like visual features to spot specific
# items like human faces, eyes, or cars in images or video streams

faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

def train():
	
	# Create 'train_faces.csv', which contains the images and their corresponding labels
	create_csv.create()
	
	face_recognizer = cv2.face.LBPHFaceRecognizer_create()

	# Read csv file using pandas
	data = pd.read_csv('train_faces.csv').values
	
	images=[]
	labels=[]
	
	for ix in range(data.shape[0]):
		
		img = cv2.imread(data[ix][0])
		gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
		images.append(gray)
		labels.append(data[ix][1])
	
	face_recognizer.train(images,np.array(labels))
	return face_recognizer
	
	
def test(test_img, face_recognizer):
	
	image = cv2.imread(test_img)
	gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
	
	faces = faceCascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5,minSize=(30, 30),flags = cv2.CASCADE_SCALE_IMAGE)
	
	for (x, y, w, h) in faces:
		
		sub_img = gray[y:y+h,x:x+w]
		cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
		
		# Predict label of detected face
		pred_label = face_recognizer.predict(gray)

		name_id = pred_label[0]
		name_str = list_names[name_id]
		
		cv2.putText(image, name_str, (x,y-5), cv2.FONT_HERSHEY_PLAIN, 2,(0,255,0),1)

		cv2.imshow('Face Recognition',image)
		# Press Esc to Close Window
		cv2.waitKey(0)
	

def dir_list():
	for dirname, dirnames, filenames in os.walk('training_data'):
		for subdirname in dirnames:
			list_names.append(subdirname) 

if __name__ == '__main__':
	face_recog = train()
	dir_list()
	test(test_img, face_recog)
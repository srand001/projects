import os, os.path
import numpy as np
import cv2

def create():

	if not "training_faces" in os.listdir("."):
		os.mkdir("training_faces")
	else:
		return
	
	faceCascade = cv2.CascadeClassifier('haarcascade_face.xml')

	label = 0
	i=1
	arr = []

	for dirname, dirnames, filenames in os.walk('training_data'):

		for subdirname in dirnames:
			subject_path = os.path.join(dirname, subdirname)

			for filename in os.listdir(subject_path):

				if filename.endswith('.jpg') or filename.endswith('.png') or filename.endswith('.jpeg'):

					abs_path = "%s/%s" % (subject_path, filename)
					image=cv2.imread(abs_path)
					faces = faceCascade.detectMultiScale(image,scaleFactor=1.1,minNeighbors=5,minSize=(30, 30),flags = 0)

					for (x, y, w, h) in faces:
						os.chdir("training_faces")
						cv2.imwrite(str(label)+str(i)+".jpg",image[y-15:y+h+15,x-15:x+w+15])
						arr.append( ["training_faces/"+str(label)+str(i)+".jpg",label] )
						os.chdir("../")
						cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
						i+=1
					np.savetxt('train_faces.csv',arr,delimiter=',', fmt='%s')

			label = label + 1

			

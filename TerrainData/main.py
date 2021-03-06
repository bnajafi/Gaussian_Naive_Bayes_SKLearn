#!/usr/bin/python

""" Complete the code in ClassifyNB.py with the sklearn
    Naive Bayes classifier to classify the terrain data.
    
    The objective of this exercise is to recreate the decision 
    boundary found in the lesson video, and make a plot that
    visually shows the decision boundary """

import os
os.chdir("C:/Users/behzad/Dropbox/_7_EduMaterial_PYTHON_MachineLearing/Classification/Gaussian_Naive_Bayes_SKLearn/TerrainData")
from prep_terrain_data import makeTerrainData
from class_vis import prettyPicture, output_image
from classifyNB import classify
from sklearn.metrics import accuracy_score

import numpy as np
import pylab as pl


features_train, labels_train, features_test, labels_test = makeTerrainData()

### the training data (features_train, labels_train) have both "fast" and "slow" points mixed
### in together--separate them so we can give them different colors in the scatterplot,
### and visually identify them
grade_fast = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==0]
bumpy_fast = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==0]
grade_slow = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==1]
bumpy_slow = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==1]


# You will need to complete this function imported from the ClassifyNB script.
# Be sure to change to that code tab to complete this quiz.
clf = classify(features_train, labels_train)

# Here I am just calculating the accuracy of the classifier 
#1: by comparing the results:
pred= clf.predict(features_test)
dif = abs(pred-labels_test)
accuracy=1-sum(dif)/len(labels_test)
print len(labels_test)
print accuracy

# The second Method of accuracy is to use the score function of Sklearn
accuracy2=clf.score(features_test,labels_test)
print("the accuracy using the Sklearn builtin score function is: "+str(accuracy2))

#the 3rd way is using th sklearn metric module and the function accuracy_score
accuracy3 = accuracy_score(pred,labels_test)
print("the accuracy using the Sklearn metric's builtin accuracy_score function is: " + str(accuracy3))


### draw the decision boundary with the text points overlaid
prettyPicture(clf, features_test, labels_test)
output_image("test.png", "png", open("test.png", "rb").read())


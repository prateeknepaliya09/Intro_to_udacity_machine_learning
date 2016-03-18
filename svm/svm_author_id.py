#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess
from sklearn.metrics import accuracy_score


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###
t0 = time()
print "we strating from 0 seconds"
time1 = round(time()-t0, 3)
print "time for fit  = ", time1, "seconds"

from sklearn import svm

#eatures_train = features_train[:len(features_train)/100] 
#labels_train = labels_train[:len(labels_train)/100] 

clf = svm.SVC(kernel="rbf", C=10000.00)

clf.fit(features_train, labels_train)

pred = clf.predict(features_test)


time2 = round(time()-t0, 3)

print "time to predict  = ", time2, "seconds"


accuracy = accuracy_score(labels_test ,pred)
print "accuracy of pred is",accuracy," %"

print pred[0]
print pred[26]
print pred[50]

predd = 0
for i in pred:
     if i == 1:
         predd+=1    

print predd

#########################################################



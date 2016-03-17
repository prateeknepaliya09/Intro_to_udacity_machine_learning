#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 1 (Naive Bayes) mini-project. 

    Use a Naive Bayes Classifier to identify emails by their authors
    
    authors and labels:
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###
clf = GaussianNB()

t0 = time()
print "we strating from 0 seconds"


clf.fit(features_train, labels_train)
time1 = round(time()-t0, 3)
print "time for fit  = ", time1, "seconds"


pred = clf.predict(features_test)
time2 = round(time()-t0, 3)
print "time to predinct  = ", time2, "seconds"

#finding diff bw training time and prediction time
timex = time2 - time1
print "diff bw fit and predict is ",timex
print "prediction time is ", time1*100/time2,"% less then training/fitting time"

accuracy = accuracy_score(labels_test ,pred)
print "accuracy of pred is",accuracy," %"
#########################################################



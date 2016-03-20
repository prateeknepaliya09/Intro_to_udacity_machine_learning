#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))
print "For each person, how many features are available?"
print len(enron_data.values()[1])


d=0

for i in enron_data.values():
    if i["poi"] == True:
        d+=1
                
print d 

with open("poi_names.txt") as foo:
    lines = len(foo.readlines())
    
    
print lines

print "What is the total value of the stock belonging to James Prentice?"

print enron_data["PRENTICE JAMES"]["total_stock_value"]


print "How many email messages do we have from Wesley Colwell to persons of interest?"

print enron_data["COLWELL WESLEY"]["from_this_person_to_poi"]
    

print "What’s the value of stock options exercised by Jeffrey Skilling?"

print enron_data["SKILLING JEFFREY K"]["exercised_stock_options"]


print "How much money did that person get?"

print enron_data["TOTAL"]["total_stock_value"]


print "How many folks in this dataset have a quantified salary? What about a known email address?"
 

quantified_salary = 0
email_add = 0 
for i in enron_data.values():
    if i["salary"] != "NaN":
        quantified_salary+=1
    if i["email_address"] != "NaN" :
        email_add+=1
      
print quantified_salary
print email_add

print "How many people in the E+F dataset (as it currently exists) have “NaN” for their total payments? What percentage of people in the dataset as a whole is this?"
 
 
nana = 0
per = 0
for i in enron_data.values():
    if i["total_payments"] == "NaN":
        nana+=1
print nana       

##per=float(nana)*(100.0/146.0)   
#print per    

print "How many POIs in the E+F dataset have “NaN” for their total payments?What percentage of POI’s as a whole is this?"

poi_enron = 0
#nana = 0
kk=0
for i in enron_data.values():
    if i["total_payments"] == "NaN":
        if i["poi"] == True:
            kk+=1
print kk


per=float(kk)*(100.0/156.0)   
print per 

print "What is the new number of POI’s in the dataset? What percentage of them have “NaN” for their total stock value?"

new_poi = d+10
print new_poi

#Simple mathematics Bitch!
#answer is 10



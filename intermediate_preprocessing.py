# -*- coding: utf-8 -*-
"""
Created on Wed Feb 11 15:14:33 2015

@author: Eloi
"""

import re




arff = open("train_a.arff",'w')
csv = open("train.csv",'r')

arff.write("@RELATION titanic\n\n")

arff.write("@ATTRIBUTE Passengerid NUMERIC\n")
arff.write("@ATTRIBUTE class {0,1}\n")
arff.write("@ATTRIBUTE Pclass NUMERIC\n")
arff.write("@ATTRIBUTE Sex NUMERIC\n")
arff.write("@ATTRIBUTE Age NUMERIC\n")
arff.write("@ATTRIBUTE SibSp NUMERIC\n")
arff.write("@ATTRIBUTE Parch NUMERIC\n")
arff.write("@ATTRIBUTE Fare NUMERIC\n")
arff.write("@ATTRIBUTE familysize NUMERIC\n")
arff.write("@ATTRIBUTE fareperperson NUMERIC\n\n")


arff.write("@DATA\n")

for line in csv:
    match = re.match(r'"(.*),(.*),(.*),"(.*)",(.*),(.*),(.*),(.*),(.*),(.*),(.*),(.*)"', line) 
    newline =  match.group(1) + "," + match.group(2) + "," + match.group(3) + ","   
    if match.group(5) == "male":
        newline += "0,"
    else:
        newline += "1,"
    if match.group(6) == "":
        newline += "?,"
    else:
        newline += match.group(6) + ","
      
    newline += match.group(7) + "," + match.group(8) + "," + match.group(10)
    
    #add familysize
    familysize = int(match.group(7)) + int(match.group(8))

    fareperperson = float(match.group(10)) / (familysize + 1) 
    newline += "," + str(familysize) + "," + str(fareperperson)
    
    
    newline += "\n"
    arff.write(newline)
    
arff.close()
csv
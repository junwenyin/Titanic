# -*- coding: utf-8 -*-
"""
Created on Wed Feb 11 15:14:33 2015

@author: Eloi
"""

import re

arff = open("pandasdeck.arff",'r')
csv = open("pandasdeck.csv",'w')

csv.write("PassengerId,Survived\n")
i = 892
for line in arff:
    if (line == "\n") or re.match('@', line):
        pass
    else:
        csv.write(str(i) + "," + line[0] + "\n")
        i +=1
    
    
arff.close()
csv.close()
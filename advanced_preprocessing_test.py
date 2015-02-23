# -*- coding: utf-8 -*-
"""
Created on Wed Feb 11 15:14:33 2015

@author: Eloi
"""

import numpy as np
import pandas as pd
import re


def substrings_in_string(big_string, title_list):
    decomposed = re.sub("[^\w]", " ",  big_string).split()
    for title in title_list:
        for word in decomposed:
            if word==title: 
                return title
    return np.nan
    
def replace_titles(x):
    title=x['Title']
    if title in ['Don', 'Major', 'Capt', 'Jonkheer', 'Rev', 'Col']:
        return 'Mr'
    elif title in ['Countess', 'Mme']:
        return 'Mrs'
    elif title in ['Mlle', 'Ms']:
        return 'Miss'
    elif title =='Dr':
        if x['Sex']=='Male':
            return 'Mr'
        else:
            return 'Mrs'
    else:
        return title
        

data = pd.read_csv("test.csv")
data = data.drop(["PassengerId","Ticket","Cabin"], axis=1)

title_list=['Mrs', 'Mr', 'Master', 'Miss', 'Major', 'Rev',
                    'Dr', 'Ms', 'Mlle','Col', 'Capt', 'Mme', 'Countess',
                    'Don', 'Jonkheer']
#create title feature
data['Title']=data['Name'].map(lambda x: substrings_in_string(x, title_list))

#replace missing ages with the average age of people with the same title
average_age = data.groupby("Title").aggregate(np.mean)["Age"]
data["Age"] = data.apply(lambda row: average_age[row["Title"]]
                                            if pd.isnull(row["Age"])
                                            else row["Age"],
                                axis=1)


#replacing all titles with mr, mrs, miss, master
data['Title']=data.apply(replace_titles, axis=1)

#remove the name feature
data = data.drop(["Name"], axis = 1)

#add a missing values column for weka
data.insert(0, "Survived", "?")

#add familysize feature (= SibSp + Parch)
data["Familysize"] = data["SibSp"] + data["Parch"]

#add ageclass (= age * Pclass)
data['Age*Class']=data['Age'] * data['Pclass']

#add fareperperson (= fare / familysize)
data['FarePerPerson']=data['Fare']/(data['Familysize']+1)

#change missing values to "?"
data = data.fillna("?")

data.to_csv("test_cleaned.csv",index=False)
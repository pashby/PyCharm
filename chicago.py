import numpy
import os
import pandas as pd
#headers = ['name', 'title', 'department', 'salary']

users = pd.read_csv("uusr.csv",sep='|',names=['user_id','age','gender','zip code'])
print(users.head())





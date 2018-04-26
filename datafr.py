import pandas as pd
import numpy as np

data = {
    'Students':['AJ','Mark','Bob','Rachel','Stephen'],
    'Maths':[98,50,23,72,87],
    'Science':[96,45,76,54,1],
    'Sports':['Basketball','Swimming','TT','Badminton','Tae Kwon Do']
}
students = pd.DataFrame(data,columns = ['Students','Maths','Science','Sports']) #,['Students','Maths','Table Tennis','Science','Sports']
print(students)

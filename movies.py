import pandas as pd
'''
users = pd.read_csv("ml-100k/u.user",sep='|',names=['User_ID','Age','Gender','Occupation','Zip_Code'])

print(users.head())
print(users.tail())
print(users.head(2))
print(users.tail(4))

print(users[10:15])
print(users[9:14])
print(users[:15])
print(users[:-15])

print(users['Zip_Code'].head())
print(users['Gender'].head(10))

cols = ['Occupation','Zip_Code']
print(users[cols].head(5))
print(users[users.Age < 25].head(10))

print(users.Zip_Code.head())
print(users[(users.Age < 40) & (users.Gender == 'M')].head(10))
print(users[(users.Occupation == 'writer') & (users.Gender == 'F')].head(10))
print(users[(users.Gender == 'M')|(users.Age > 40)].head(5))
'''
users = pd.read_csv("ml-100k/u.user",sep='|',names=['user_ID','age','gender','occupation','zip_code'])
print(users.head())
print(users.dtypes)
print(users.describe())
print(users.head())

print(users.set_index('user_ID').head())
print('***********************')
print(users.set_index('user_ID',inplace=True))
#print(users)
print('&&&&&&&&&&&&&&&&&')
print(users.ix[[1,2,3]])



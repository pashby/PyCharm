import pandas as pd
import numpy as np
print(pd.__version__)
s = pd.Series([10,'Namaste',23.5,'Hello'], index = ["a","b","c","d"])
print(s)
d = {'Seattle':100,"San Francisco":500, 'San Jose':150, 'London':1200, 'Tokyo':1600}
cities = pd.Series(d)
print(cities)
print(cities < 1000)
cities['San Francisco'] = 600
print(cities)
cities[cities < 1000]=750
print(cities)
print('London' in cities)
print(cities/10)
print(np.square(cities))
print(cities.isnull())


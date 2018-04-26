import matplotlib
import matplotlib.pyplot as pt
import numpy as np
import pandas as pd
#frame = pd.DataFrame({'key':range(5)})
#frame1 = pd.DataFrame({'key':range(5)})
frame1 = pd.DataFrame({'key':range(5),'frame1':['a','b','c','d','e']})
print(frame1)
frame2 = pd.DataFrame({'key':range(2,7),'frame2': ['t','u','v','w','x']})
print(frame2)
print(pd.merge(frame1,frame2, on="key", how='right'))
print(pd.merge(frame1,frame2, on="key", how='left'))
print(pd.merge(frame1,frame2, on="key", how='inner'))
print(pd.merge(frame1,frame2, on="key", how='outer'))
print(pd.concat([frame1,frame2],axis =1))



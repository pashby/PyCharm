import matplotlib
import matplotlib.pyplot as pt
import numpy as np
from mpl_toolkits.mplot3d import axes3d

fig = pt.figure()
chart = fig.add_subplot(1,1,1,projection='3d')
x = [1,2,3,4,5,6,7,8,9,10]
y = [1,2,3,5,7,9,3,2,1,0]
z = [0,0,0,0,0,0,0,0,0,0]
dx = np.ones(10)
dy = np.ones(10)
dz = [1,4,9,16,25,36,49,64,81,100]

chart.set_xlabel("X axis")
chart.set_ylabel('Y axis')
chart.set_zlabel('Z axis')

chart.bar3d(x,y,z,dx,dy,dz,color="red")



pt._show()




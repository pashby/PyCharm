import matplotlib
import matplotlib.pyplot as pt
import numpy as np
from mpl_toolkits.mplot3d import axes3d

fig = pt.figure()
chart = fig.add_subplot(1,1,1,projection='3d')

x,y,z = axes3d.get_test_data(.02)
#chart.bar3d(x,y,z,dx,dy,dz,color="red")
chart.plot_wireframe(x,y,z,rstride=5,cstride=5)

chart.set_xlabel("X axis")
chart.set_ylabel('Y axis')
chart.set_zlabel('Z axis')





pt._show()




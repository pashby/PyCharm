import matplotlib
import matplotlib.pyplot as pt
import numpy as np

fig = pt.figure()
chart = fig.add_subplot(1,1,1)

pos = np.arange(6) + .5
pt.barh(pos,(4,2,6,8,1,3),align="center",color="red")




pt._show()




import matplotlib
import matplotlib.pyplot as pt

fig = pt.figure()
rec = fig.patch
rec.set_facecolor("green")

x = [3,7,8,12]
y = [5,13,2,8]
x2 = [0,1,2,3]
y2 =[0,1,4,9]
x3 = [0,1,2,3]
y3 = [0,1,8,27]


graph1 = fig.add_subplot(1,1,1,facecolor="black")
graph1.plot(x,y,"red",linewidth=4)
graph1.plot(x2,y2,"yellow",linewidth=3)
graph1.plot(x3,y3,"blue",linewidth=2)


graph1.tick_params(axis='x',color='white')
graph1.tick_params(axis='y',color='white')
graph1.spines['left'].set_edgecolor('white')
graph1.spines['top'].set_edgecolor('white')
graph1.spines['right'].set_edgecolor('white')
graph1.spines['bottom'].set_edgecolor('white')
graph1.set_title("This is a random graph",color="white")
graph1.set_xlabel("This is the X axis")
graph1.set_ylabel("This is the Y axis")


graph2 = fig.add_subplot(2,1,2,facecolor="black")
graph2.plot(x,y,"red",linewidth=4)
graph2.plot(x2,y2,"yellow",linewidth=3)
graph2.plot(x3,y3,"blue",linewidth=2)


graph2.tick_params(axis='x',color='white')
graph2.tick_params(axis='y',color='white')
graph2.spines['left'].set_edgecolor('white')
graph2.spines['top'].set_edgecolor('white')
graph2.spines['right'].set_edgecolor('white')
graph2.spines['bottom'].set_edgecolor('white')
graph2.set_title("This is a random graph",color="white")
graph2.set_xlabel("This is the X axis")
graph2.set_ylabel("This is the Y axis")


pt.show()

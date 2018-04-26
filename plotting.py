import matplotlib
import matplotlib.pyplot as pt
pt.plot([1,2,3,4,5],[3,8,10,25,40])

x = []
y = []

f = open("coordinates.txt","r")
points = f.read().split('\n')

print(points)
for val in points:
    data = val.split(",")
    x.append(int(data[0]))
    y.append(int(data[1]))
print(x,y)

pt.plot(x,y)
pt.show()

'''
pt.title('Rain in December')
pt.xlabel('Days in December')
pt.ylabel('Inches of Rain')


'''


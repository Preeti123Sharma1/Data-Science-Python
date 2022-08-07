from turtle import *

speed('slowest')
pencolor('red')
bgcolor('yellow')

side = 10
size = 50
for i in range(side):
    fd(size)
    lt(360/side)


mainloop()    
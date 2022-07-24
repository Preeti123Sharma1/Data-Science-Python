from turtle import *
speed('slowest')
pencolor('red')
bgcolor('blue')
pensize(10)

side = 15
size = 100
fillcolor('green')
begin_fill()

for i in range(side):
    fd(size)
    lt(90/side)
    rt(size)
    fd(size)
    lt(90/side)
    rt(size)
    fd(size)
    lt(90/side)
    rt(size)
    fd(size)
    lt(90/side)
    rt(size)
    fd(size)
    lt(90/side)
    rt(size)
    fd(size)
    lt(90/side)
    rt(size)
    

end_fill()
mainloop()    
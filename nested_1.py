from turtle import*

size = 100
side = 6
pencolor('blue')
pensize(4)
for i in range(side):
    forward(size)
    pencolor('red')
    for i in range(side):
        pencolor('crimson')
        forward(size)
        pencolor('blue')
        write(i, font =('Arial',14,'normal'),align='left')
        left(360/side)
    left(360/side)        

mainloop()

from turtle import*

pencolor('blue')
pensize(4)
for i in range(4):
    forward(100)
    pencolor('red')
    for i in range(6):
        pencolor('crimson')
        forward(100)
        pencolor('blue')
        write(i, font =('Arial',14,'normal'),align='left')
        left(360/6)
    left(360/4)        

mainloop()

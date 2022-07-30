from turtle import*

speed('fast')
pencolor('blue')
pensize(4)
for i in range(15):
    forward(100)
    pencolor('red')
    for i in range(12):
        forward(50)
        
        left(270/12)
    left(360/15)        

mainloop()

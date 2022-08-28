import pgzrun

HEIGHT = 500
WIDTH = 600

p = Actor('ironman', (100,100))
speed = 3
def draw():
    screen.fill('black')
    #screen.clear()
    p.draw()

def update():
    player_control()

def player_control():
    
    if keyboard.DOWN and not p.bottom > HEIGHT:
        p.y += speed

    if keyboard.UP and not p.top < 0:
        p.y += -speed
    
pgzrun.go() # outside the function
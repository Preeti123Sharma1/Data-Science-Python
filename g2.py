import pgzrun

HEIGHT = 500
WIDTH = 600

p = Actor('ironman', (100,100))
speed = 3
def draw():
    screen.fill('blue')
    #screen.clear()
    p.draw()

def update():
    player_control()

def player_control():
    if keyboard.RIGHT and not p.right > WIDTH:
        p.x += speed

    elif keyboard.LEFT and not p.left < 0:
        p.x += -speed

    elif keyboard.DOWN and not p.bottom > HEIGHT:
        p.y += speed

    elif keyboard.UP and not p.top < 0:
        p.y += -speed
    else:
        p.angle = 0 #  when ironman stop then angle not change



pgzrun.go() # outside the function
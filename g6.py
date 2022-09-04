import pgzrun

HEIGHT = 500
WIDTH = 500

class Player(Actor):
    speed = 3

    def move(self):
        if keyboard.LEFT and self.left > 0:
            self.x += -self.speed
        if keyboard.RIGHT and self.right < WIDTH:
            self.x += self.speed


class Enemy(Actor):
    speed = 1

    def chase(self,player):
        global game_over
        if self.x < player.x :
            self.x += self.speed
        if self.x > player.x:
            self.x += -self.speed

e = Enemy('zombie', pos=(400,400))
p = Player('ironman', pos=(100,100))

def draw():
    screen.clear()
    p.draw()
    e.draw()

def update():
    p.move()
    e.chase(p)

pgzrun.go()
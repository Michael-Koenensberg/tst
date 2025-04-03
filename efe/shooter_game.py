#Создай собственный Шутер!

SpaceY = 0
spaceY2 = -450
from pygame import *
import TouchDetect
from random import randint
import wait
import time
print("ADUEEIIJ")
import json
stats = None
# stats_example = {
#     "Score":0
#     "Skins":[]
# }
mixer.init()
bullets = []
times = {}
# class CFrame():
#     def __init__(self, xp, yp, xs, ys):
#         self.xp = xp
#         self.yp = yp
#         self.xs = xs
#         self.ys = ys

def GetStats():

    with open("Stats.json", "r") as file:
        stats = open(file)


FPS = 60
window = display.set_mode((700, 450))
game = True
space = transform.scale(image.load("galaxy.jpg"), (700, 450))
space2 = transform.scale(image.load("galaxy.jpg"), (700, 450))
class MObject():
    def __init__(self, pos, size, pic):
        self.pos = pos
        self.size = size
        self.pic = pic

class Character(MObject):
    
    def __init__(self, health, speed, kamikadze, damage, bullet_speed, pos, size, pic, transformed):
        self.health = health
        self.speed = speed
        self.kamikadze = kamikadze
        self.damage = damage
        self.bullet_speed = bullet_speed
        self.transformed = transformed
        super().__init__(pos, size, pic)
class Bullet(MObject):
    def __init__(self, speed, explosion, damage, transformed, pos, size, pic, spawn_time, lifetime):
        self.speed = speed
        self.explosion = explosion
        self.damage = damage
        transformed = transform.scale(image.load(pic), size)
        self.transformed = transformed
        self.spawn_time = spawn_time
        self.lifetime = lifetime
        super().__init__(pos, size, pic)
#Player Settings
Player = Character(100, 5, True, 25, 0, [0, 0], [80, 50], "rocket.png")
#end
PlrSprite = transform.scale(image.load(Player.pic), (Player.size))

num = 0
enemies_num = 0
enemies = []
def randx(min, max):
    return randint(min, max)
ESC = 5
last_time_spawn = time.time()
while game:
    if wait.wait(ESC, last_time_spawn):
        for i in range(5):
            enemies.append(Character(25, 50, True, 45, 55, [randx(0, 720), 0], [45, 20], "asteroid.png", transform.scale(self.pic, self.size)))
    window.blit(space, (0, SpaceY))
    window.blit(space2, (0, spaceY2))
    window.blit(PlrSprite, Player.pos)

    for i in enemies:
        window.blit(i.transformed, i.pos)
        i.pos[1] -= i.speed
        if i.pos[1] > 0:
            enemies.pop(enemies_num)
        if i.health < 1:
            enemies.pop(enemies_num)
        enemies_num += 1
    enemies_num = 0
    for i in bullets:
        
        window.blit(i.transformed, i.pos)
        i.pos[1] -= i.speed

        if i.pos[1] < -450:
            bullets.pop(num)
        
        if wait.wait(i.lifetime, i.spawn_time):
            bullets.pop(num)
        num += 1    
        
    num = 0
            
    SpaceY += 1
    spaceY2 += 1
    if spaceY2 == 0:
        spaceY2 = -450
        SpaceY = 0
        
    for e in event.get():
        if e.type == QUIT:
            game = False
            
        # if e.key == K_SPACE:

    
    ButtonsDown = key.get_pressed()
    if ButtonsDown[K_d]:
        Player.pos[0] += Player.speed
    if ButtonsDown[K_s]:
        Player.pos[1] += Player.speed
    if ButtonsDown[K_w]:
        Player.pos[1] -= Player.speed
    if ButtonsDown[K_a]:
        Player.pos[0] -= Player.speed
    if ButtonsDown[K_f]:
        bullet = Bullet(50, True, 100, 0, [Player.pos[0], Player.pos[1]], [20, 40], "bullet.png", time.time(), 5)
        # sus = timer.wait(2)
        bullets.append(bullet)
    display.update()
clock.tick(FPS)
from re import X
from ursina import *
import random

app = Ursina()
window.title = "Kanye VS Pete"
window.borderless = False
window.fullscreen = False
window.exit_button.visible = False
window.fps_counter.enabled = True

camera.orthographic = True

camera.fov = 10

car = Entity(model='quad', texture='p1.jpg', collider='box', scale=(1.5,1), rotation_z=-90, y = -3)

road1 = Entity(model='quad', texture='road.jpg',scale=15, z=1)
road2= duplicate(road1, texture = 'road.jpg', scale = 15, y=15)
pair = [road1, road2]

enemies = []
def newEnemy():
    val = random.uniform(-2,2)
    new = duplicate(car, texture='p2.jpg',x = 2*val, y = 25, color=color.random_color(), rotation_z = 90 if val < 0 else -90)
    enemies.append(new)
    invoke(newEnemy, delay=0.5)
newEnemy()

def update():
    car.x -= held_keys['a']*10*time.dt
    car.x += held_keys['d']*10*time.dt
    car.y += held_keys['w']*5*time.dt
    car.y -= held_keys['s']*5*time.dt
    for road in pair:
        road.y -= 10*time.dt
    if road.y < -1:
        road.y += 2
    for enemy in enemies:
        if enemy.x < 0:
            enemy.y -= 10 * time.dt
        else:
            enemy.y -= 5 * time.dt
        if enemy.y < -10:
            enemies.remove(enemy)
            destroy(enemy)
    if car.intersects().hit:
        car.shake()

app.run()
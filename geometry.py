from ursina import *
from ursina import texture
from ursina import curve
from pynput.keyboard import Listener

app = Ursina()

background = Entity(
    model = 'quad',
    texture = 'assets\BG2',
    scale = 55, z = 10, y = 15
)
camera.orthographic = True 
camera.fov = 18

player = Entity(
    model='quad',
    collider='box',
    texture='asset\square'
)

ground = Entity(
    model='cube',
    color=color.yellow,
    y=-1,origin_y=.5,
    scale=(200,15,1),
    collider='box',
    texture='white_cube'
)
def update():
    if not player.intersects().hit:
        player.y -= time.dt
    player.y = max(-0.5,player.y)

def input(key):
    if key == 'Key.Space':
        if player.intersects().hit:
            player.animate_y(
                player + 3,
                duration = 0.3,
                curve=curve.out_sine
            )
            player.animate_rotation_z(
                player.rotation_z + 180,
                duration=0.5,
                curve=curve.linear
            )

app.run()
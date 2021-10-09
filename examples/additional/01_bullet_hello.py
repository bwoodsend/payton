import random

from payton.scene import Scene
from payton.scene.geometry import Cube, Plane

scene = Scene()
scene.lights[0].position = [50, 50, 50]
ground = Plane(20, 20)
ground.changeDynamics(lateralFriction=1.0, linearDamping=10.0, angularDamping=10.0)
scene.add_object("ground", ground)

for i in range(40):
    x = random.randint(-30, 30) / 10.0
    y = random.randint(-30, 30) / 10.0
    z = random.randint(30, 100) / 10.0
    r = random.randint(0, 255) / 255.0
    g = random.randint(0, 255) / 255.0
    b = random.randint(0, 255) / 255.0
    cube = Cube()
    cube.material.color = [r, g, b]
    cube.position = [x, y, z]
    cube.mass = 1
    scene.add_object("cube_{}".format(i), cube)

scene.run()

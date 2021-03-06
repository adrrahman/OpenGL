import sys
import random
import grafikautils as utils
# import math
from pygame.constants import *
from OpenGL.GLU import *
from ctypes import *
from OBJFileLoader import *

class knalpot():
    def __init__(self):
        self.x = 0.5
        self.y = -2.4
        self.z = 0.5
        self.color = (173, 173, 133)
        self.last_x = 0.5
        self.last_y = -2.4
        self.last_z = 0.5

    def move(self):
        if self.y < -10:
            self.x=self.last_x
            self.y=self.last_y
            self.z=self.last_z
        else:
            self.y-=random.uniform(0, 2)
        self.x+=random.uniform(-0.05, 0.05)

class hujan():
    def __init__(self,z):
        self.x = random.uniform(-10,10)
        self.y = random.uniform(-10,10)
        self.z = random.uniform(1,8)
        self.deltaZ = 0.05
        self.color = (1, 207, 248)

    def move(self):
        self.deltaZ += 0.025
        if (self.z < -0.4):
            self.z = 8
            self.deltaZ = 0.05
        else:
            self.z -= self.deltaZ

ground_surfaces = (0,1,2,3)

ground_vertices = (
    (-10,-10,-0.1),
    (-10,10,-0.1),
    (10,10,-0.1),
    (10,-10,-0.1)
)


def Ground():
    glBegin(GL_QUADS)

    x = 0
    for vertex in ground_vertices:
        x += 1
        glColor3fv((0.37, 0.25, 0.13))
        glVertex3fv(vertex)
    glEnd()

pygame.init()
viewport = (800,600)
hx = viewport[0]/2
hy = viewport[1]/2
srf = pygame.display.set_mode(viewport, OPENGL | DOUBLEBUF)
intensity = 0.1
glLightfv(GL_LIGHT0, GL_POSITION,  (-40, 200, 100, 0.0))
glLightfv(GL_LIGHT0, GL_AMBIENT, (intensity, intensity, intensity, 1.0))
glLightfv(GL_LIGHT0, GL_DIFFUSE, (0.5, 0.5, 0.5, 1.0))
glEnable(GL_LIGHT0)
glEnable(GL_LIGHTING)
glEnable(GL_COLOR_MATERIAL)
glEnable(GL_DEPTH_TEST)
glEnableClientState (GL_VERTEX_ARRAY)
glShadeModel(GL_SMOOTH)
obj = OBJ("Car.obj", swapyz=True)

clock = pygame.time.Clock()

glMatrixMode(GL_PROJECTION)
glLoadIdentity()
width, height = viewport
gluPerspective(90.0, width/float(height), 1, 100.0)
glEnable(GL_DEPTH_TEST)
glMatrixMode(GL_MODELVIEW)

rx, ry = (0,0)
tx, ty = (0,0)
zpos = 5
rotate = move = False

vertices = [ 0.0, 1.0, 0.0,  0.0, 0.0, 0.0,  1.0, 1.0, 0.0 ]
vbo = glGenBuffers (1)
glBindBuffer (GL_ARRAY_BUFFER, vbo)
glBufferData (GL_ARRAY_BUFFER, len(vertices)*4, (c_float*len(vertices))(*vertices), GL_STATIC_DRAW)

px, py = (tx/20, ty/20)

partikel_knalpot = []
partikel_hujan = []

for part in range(40):
    partikel_knalpot.append(knalpot())

for z_hujan in range(50):
    partikel_hujan.append(hujan(z_hujan))

glClearColor(0, 0.07, 0.2, 0.0)
while 1:
    # clock.tick(30)

    for e in pygame.event.get():
        if e.type == QUIT:
            sys.exit()
        elif e.type == KEYDOWN and e.key == K_ESCAPE:
            sys.exit()
        elif e.type == MOUSEBUTTONDOWN:
            if e.button == 4: zpos = max(1, zpos-1)
            elif e.button == 5: zpos += 1
            elif e.button == 1: rotate = True
            elif e.button == 3: move = True
        elif e.type == MOUSEBUTTONUP:
            if e.button == 1: rotate = False
            elif e.button == 3: move = False
        elif e.type == MOUSEMOTION:
            i, j = e.rel
            if rotate:
                rx += i
                ry += j
            if move:
                tx += i
                ty -= j
        elif e.type == KEYDOWN and e.key == K_UP:
            intensity += 0.1
        elif e.type == KEYDOWN and e.key == K_DOWN:
            intensity -= 0.1


    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    glTranslate(tx/20., ty/20., - zpos)
    glLightfv(GL_LIGHT0, GL_AMBIENT, (intensity, intensity, intensity, 1.0))
    glRotate(-90, 1, 0, 0)
    glRotate(ry, 1, 0, 0)
    glRotate(rx, 0, 0, 1)
    glCallList(obj.gl_list)
    Ground()
    for k in partikel_knalpot:
        k.move()
        glColor3f(1, 1, 1)
        utils.draw_cube(k.x, k.y, k.z)

    for butir in partikel_hujan:
        butir.move()
        glColor3f(1, 207, 248)
        utils.draw_cube(butir.x,butir.y,butir.z)

    clock.tick()
    fps = clock.get_fps()
    print(fps)
    pygame.display.flip()
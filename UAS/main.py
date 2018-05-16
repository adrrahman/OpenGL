import sys
import random
import grafikautils as utils
from pygame.constants import *
from pygame.time import *
from OpenGL.GL import *
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
        self.color = (1, 207, 248)
        self.last_x = self.x
        self.last_y = self.y
        self.last_z = z

    def move(self):
        if (self.z < -0.4):
            self.z = 8
        else:
            self.z = self.z - 0.2

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

partikel_knalpot = []
partikel_hujan = []

for part in range(40):
    partikel_knalpot.append(knalpot())

for part in range(50):
    ssz = 0.5 + part
    temp = hujan(ssz)
    partikel_hujan.append(temp)

vertices = [ 0.0, 1.0, 0.0,  0.0, 0.0, 0.0,  1.0, 1.0, 0.0 ]
vbo = glGenBuffers (1)
glBindBuffer (GL_ARRAY_BUFFER, vbo)
glBufferData (GL_ARRAY_BUFFER, len(vertices)*4, (c_float*len(vertices))(*vertices), GL_STATIC_DRAW)

px, py = (tx/20, ty/20)

while 1:
    clock.tick(30)
    
    # srf.fill((255, 255, 255))
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

    # RENDER OBJECT
    glTranslate(tx/20., ty/20., - zpos)
    glLightfv(GL_LIGHT0, GL_AMBIENT, (intensity, intensity, intensity, 1.0))
    glRotate(-90, 1, 0, 0)
    glRotate(ry, 1, 0, 0)
    glRotate(rx, 0, 0, 1)
    glCallList(obj.gl_list)

    for p in partikel_knalpot:
        p.move()
        glColor3f(1, 1, 1)
        utils.draw_cube(p.x, p.y, p.z)

    for part in range(50):
        ptemp = partikel_hujan[part]
        ptemp.move()
        glColor3f(1, 207, 248)
        utils.draw_cube(ptemp.x,ptemp.y,ptemp.z)

    clock.tick()
    fps = clock.get_fps()
    print(fps)
    pygame.display.flip()
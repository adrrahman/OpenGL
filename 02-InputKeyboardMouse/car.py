import pygame
from math import cos, sin
import numpy

from OpenGL.raw.GLUT import glutSolidTorus
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

verticies = (
    (0.2,0.4,0.6),
    (0.6,0.5,0.6),
    (0.6,0.5,0.2),
    (0.2,0.4,0.2),
    (0.2,0.2,0.6),
    (0.6,0.2,0.6),
    (0.6,0.2,0.2),
    (0.2,0.2,0.2),
    (0.2,0.2,0.6),
    (0.2,0.4,0.6),
    (0.2,0.4,0.2),
    (0.2,0.2,0.2),
    (0.6,0.2,0.6),
    (0.6,0.5,0.6),
    (0.6,0.5,0.2),
    (0.6,0.2,0.2),
    (0.2,0.2,0.6),
    (0.6,0.2,0.6),
    (0.6,0.5,0.6),
    (0.2,0.4,0.6),
    (0.2,0.2,0.2),
    (0.6,0.2,0.2),
    (0.6,0.5,0.2),
    (0.2,0.4,0.2),
    (0.7,0.65,0.6),
    (0.7,0.65,0.2),
    (1.7,0.65,0.2),
    (1.7,0.65,0.6),
    (1.8,0.5,0.6),
    (1.8,0.5,0.2),
    (2.1,0.4,0.2),
    (2.1,0.4,0.6),
    (2.1,0.2,0.6),
    (2.1,0.2,0.2),
    (1.8,0.2,0.6),
    (1.8,0.2,0.6),
    (2.1,0.4,0.6),
    (2.1,0.4,0.2),
    (2.1,0.2,0.2),
    (2.1,0.2,0.6),
    (1.8,0.2,0.2),
    (1.8,0.5,0.2),
    (2.1,0.4,0.2),
    (2.1,0.2,0.2),
    (1.8,0.2,0.6),
    (1.8,0.5,0.6),
    (2.1,0.4,0.6),
    (2.1,0.2,0.6),
    (0.6,0.5,0.6),
    (0.6,0.2,0.6),
    (1.8,0.2,0.6),
    (1.8,0.5,0.6),
    (0.6,0.2,0.6),
    (0.6,0.2,0.2),
    (1.8,0.2,0.2),
    (1.8,0.2,0.6),
    (0.6,0.5,0.2),
    (0.6,0.2,0.2),
    (1.8,0.2,0.2),
    (1.8,0.5,0.2),
    (0.77,0.63,0.2),
    (0.75,0.5,0.2),
    (1.2,0.5,0.2),
    (1.22,0.63,0.2),
    (1.27,0.63,.2),
    (1.25,0.5,0.2),
    (1.65,0.5,0.2),
    (1.67,0.63,0.2),
    (0.7,0.65,0.2),
    (0.7,0.5,0.2),
    (0.75,0.5,0.2),
    (0.77,0.65,0.2),
    (1.2,0.65,0.2),
    (1.2,0.5,.2),
    (1.25,0.5,0.2),
    (1.27,0.65,0.2),
    (1.65,0.65,0.2),
    (1.65,0.5,.2),
    (1.7,0.5,0.2),
    (1.7,0.65,0.2),
    (0.75,0.65,0.2),
    (0.75,0.63,0.2),
    (1.7,0.63,0.2),
    (1.7,0.65,0.2),
    (0.75,0.65,0.6),
    (0.75,0.63,0.6),
    (1.7,0.63,0.6),
    (1.7,0.65,0.6),
    (0.77,0.63,0.6),
    (0.75,0.5,0.6),
    (1.2,0.5,0.6),
    (1.22,0.63,0.6),
    (1.27,0.63,0.6),
    (1.25,0.5,0.6),
    (1.65,0.5,0.6),
    (1.67,0.63,0.6),
    (0.7,0.65,0.6),
    (0.7,0.5,0.6),
    (0.75,0.5,0.6),
    (0.77,0.65,0.6),
    (1.2,0.65,0.6),
    (1.2,0.5,.6),
    (1.25,0.5,0.6),
    (1.27,0.65,0.6),
    (1.65,0.65,0.6),
    (1.65,0.5,.6),
    (1.7,0.5,0.6),
    (1.7,0.65,0.6),
)

radius = 0.2
side_num = 16

red = (1, 0, 0)
blue = (0, 0, 1)
color = (red, blue)

def Car():
    glBegin(GL_QUADS)
    for x,y,z in verticies:
        glVertex3f(x,y,z)
    glEnd()

def drawCircle(offset, x, y):
	glBegin(GL_POLYGON)

	colorNow = 1
	for vertex in range(0, side_num):
		# print(vertex)
		colorNow = (colorNow+1)%2
		glColor3f(color[colorNow][0], color[colorNow][1], color[colorNow][2])
		angle = float(vertex) * 2.0 * numpy.pi / side_num + offset
		glVertex3f(numpy.cos(angle)*radius+x, numpy.sin(angle)*radius+y, 0)

	glEnd()

def main():
    pygame.init()
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

    glTranslatef(-1.0,0.0,-5)

    glRotatef(0,0,0,0)

    offset = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    glRotatef(15,0,-1,0)
                if event.key == pygame.K_RIGHT:
                    glRotatef(15,0,1,0)
                if event.key == pygame.K_UP:
                    glRotatef(15,-1,0,0)
                if event.key == pygame.K_DOWN:
                    glRotatef(15,1,0,0)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        Car()
        offset += 2
        drawCircle(offset,0.5,0.25)
        drawCircle(offset,1.8,0.25)
        pygame.display.flip()
        pygame.time.wait(10)

main()

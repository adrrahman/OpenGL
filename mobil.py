import pygame
from pygame.locals import *
import numpy

from OpenGL.GL import *
from OpenGL.GLU import *

radius=1
side_num=16
edge_only=False

red = (1, 0, 0)
blue = (0, 0, 1)

color = (red, blue)


def drawCircle(offset):
	glBegin(GL_POLYGON)

	colorNow = 1
	for vertex in range(0, side_num):
		# print(vertex)
		colorNow = (colorNow+1)%2
		glColor3f(color[colorNow][0], color[colorNow][1], color[colorNow][2])
		angle = float(vertex) * 2.0 * numpy.pi / side_num + offset
		glVertex3f(numpy.cos(angle)*radius, numpy.sin(angle)*radius, 0)

	glEnd()


def main():
	pygame.init()
	display = (800, 600)
	pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

	gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

	glTranslatef(0.0, 0.0, -5)

	offset = 0
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()

		glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
		offset = offset + 2
		drawCircle(offset)
		pygame.display.flip()
		pygame.time.wait(50)

main()
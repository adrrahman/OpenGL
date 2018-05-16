from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

import math

def draw_cube(x, y, z):
	sf = 0.008
	rf = 1/sf

	vertices= (
	    (sf, -sf, -sf),
	    (sf, sf, -sf),
	    (-sf, sf, -sf),
	    (-sf, -sf, -sf),
	    (sf, -sf, sf),
	    (sf, sf, sf),
	    (-sf, -sf, sf),
	    (-sf, sf, sf)
    	)

	edges = (
		(0,1),
		(0,3),
		(0,4),
		(2,1),
		(2,3),
		(2,7),
		(6,3),
		(6,4),
		(6,7),
		(5,1),
		(5,4),
		(5,7)
		)
	glTranslatef(x, y, z)
	glBegin(GL_LINES)
	for edge in edges:
		for vertex in edge:
			glVertex3fv(vertices[vertex])
	glEnd()
	glTranslatef(-x, -y, -z)

def draw_sphere(x, y, z):
	glPushMatrix()
	glTranslatef(x, y, z)
	glutSolidSphere(1.0, 1, 1)
	glPopMatrix()

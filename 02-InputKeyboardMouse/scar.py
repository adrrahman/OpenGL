from OpenGL import GL as gl
from OpenGL import GLUT as glut
from OpenGL.arrays import vbo
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np
import numpy
import pygame


radius = 0.1
side_num = 16

red = (1, 0, 0)
blue = (0, 0, 1)
color = (red, blue)

class VBOJiggle(object):

    #def __init__(self,nvert=100,jiggliness=0.01):
    def __init__(self, nvert=10, jiggliness=0):
        self.nvert = nvert
        self.jiggliness = jiggliness

        #verts = 2*np.random.rand(nvert,2) - 1
        verts = (
            (0.3,0.9),
            (0.7,0.9),
            (0.7,0.6),
            (0.9,0.6),
            (0.9,0.4),
            (0.1,0.4),
            (0.1,0.6),
            (0.3,0.6)
        )
        self.verts = np.require(verts,np.float32,'F')
        self.vbo = vbo.VBO(self.verts)

    def draw(self):

        gl.glClearColor(0,0,0,0)
        gl.glClear(gl.GL_COLOR_BUFFER_BIT)

        gl.glEnableClientState(gl.GL_VERTEX_ARRAY)

        self.vbo.bind()

        gl.glVertexPointer(2,gl.GL_FLOAT,0,self.vbo)
        gl.glColor(0,1,0,1)
        gl.glDrawArrays(gl.GL_POLYGON ,0,self.vbo.data.shape[0])

        gl.glDisableClientState(gl.GL_VERTEX_ARRAY)

        self.vbo.unbind()

        #self.jiggle()


    def jiggle(self):

        # jiggle half of the vertices around randomly
        delta = (np.random.rand(self.nvert//2,2) - 0.5)*self.jiggliness
        self.verts[:self.nvert:2] += delta

        # the data attribute of the vbo is the same as the numpy array
        # of vertices
        assert self.verts is self.vbo.data

        # # Approach 1:
        # # it seems like this ought to work, but it doesn't - all the
        # # vertices remain static even though the vbo's data gets updated
        # self.vbo.copy_data()

        # Approach 2:
        # this works, but it seems unnecessary to copy the whole array
        # up to the GPU, particularly if the array is large and I have
        # modified only a small subset of vertices
        self.vbo.set_array(self.verts)

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

if __name__ == '__main__':
    pygame.init()
    display = (1000,1000)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)

    glTranslatef(0.0, 0.0, -5)

    glRotatef(0, 0, 0, 0)

    offset = 0
    demo = VBOJiggle()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    glTranslatef(-0.5,0,0)
                if event.key == pygame.K_RIGHT:
                    glTranslatef(0.5,0,0)
                if event.key == pygame.K_UP:
                    glTranslatef(0,0.5,0)
                if event.key == pygame.K_DOWN:
                    glTranslatef(0,-0.5,0)

        #glRotatef(1, 3, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        demo.draw()
        offset += 2
        drawCircle(offset,0.25,0.4)
        drawCircle(offset,0.75,0.4)
        pygame.display.flip()
        pygame.time.wait(10)
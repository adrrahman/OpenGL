# coding: utf-8
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import pygame
from pygame.locals import *

##############################################################################
# OpenGL funcs
##############################################################################
def initialize():
    glClearColor(1.0, 1.0, 1.0, 0.0)
    glClearDepth(1.0)
    glDepthFunc(GL_LESS)
    glEnable(GL_DEPTH_TEST)

def resize(Width, Height):
    # viewport
    if Height == 0:
        Height = 1
    glViewport(0, 0, Width, Height)
    # projection
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, float(Width)/float(Height), 0.1, 100.0)

rotateX= 0
rotateZ= 0
offsetX= 0
offsetZ= 0

transZ= -2
offZ= 0

prev_mouse_X= 0
prev_mouse_Y= 0
firstTime= True

def draw():
    global rotateX, offsetX, rotateZ, offsetZ, transZ
    # clear
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # view
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    rotateX+=offsetX
    rotateZ+=offsetZ
    #pitch+=0.27
    transZ+=offZ
    glTranslatef(0.0, 0.0, transZ)
    glRotatef(rotateX, 0, 1, 0)
    glRotatef(rotateZ, 1, 0, 0)
    #glRotatef(pitch, 1, 0, 0)

    # cube
    #draw_cube0()
    #draw_cube1()
    #draw_cube2()
    draw_cube3()

    #glFlush()

##############################################################################
# Shader
##############################################################################
# Checks for GL posted errors after appropriate calls
def printOpenGLError():
    err = glGetError()
    if (err != GL_NO_ERROR):
        print('GLERROR: ', gluErrorString(err))
        #sys.exit()

class Shader(object):

    def initShader(self, vertex_shader_source, fragment_shader_source):
        # create program
        self.program=glCreateProgram()
        print('create program')
        printOpenGLError()

        # vertex shader
        print('compile vertex shader...')
        self.vs = glCreateShader(GL_VERTEX_SHADER)
        glShaderSource(self.vs, [vertex_shader_source])
        glCompileShader(self.vs)
        glAttachShader(self.program, self.vs)
        printOpenGLError()

        # fragment shader
        print('compile fragment shader...')
        self.fs = glCreateShader(GL_FRAGMENT_SHADER)
        glShaderSource(self.fs, [fragment_shader_source])
        glCompileShader(self.fs)
        glAttachShader(self.program, self.fs)
        printOpenGLError()

        print('link...')
        glLinkProgram(self.program)
        printOpenGLError()

    def begin(self):
        if glUseProgram(self.program):
            printOpenGLError()

    def end(self):
        glUseProgram(0)


##############################################################################
# vertices
##############################################################################
s=0.5
# vertices=[
#         -s, -s, -s,
#          s, -s, -s,
#          s,  s, -s,
#         -s,  s, -s,
#         -s, -s,  s,
#          s, -s,  s,
#          s,  s,  s,
#         -s,  s,  s,
#         ]
vertices=[
        0.1, 0.4, 0.1,
0.1, 0.1, 0.1,
0.9, 0.1, 0.1,
0.9, 0.4, 0.1,
0.8, 0.4, 0.1,
0.7, 0.9, 0.1,
0.4, 0.9, 0.1,
0.3, 0.4, 0.1,
0.1, 0.4, 0.7,
0.1, 0.1, 0.7,
0.9, 0.1, 0.7,
0.9, 0.4, 0.7,
0.8, 0.4, 0.7,
0.7, 0.9, 0.7,
0.4, 0.9, 0.7,
0.3, 0.4, 0.7,
#roda 1
0.3, 0.1, 0.1,
0.25, 0.2, 0.1,
0.35, 0.2, 0.1,
0.4, 0.1, 0.1,
0.35, 0, 0.1,
0.25, 0, 0.1,
0.2, 0.1, 0.1,
#roda 2
0.3, 0.1, 0.7,
0.25, 0.2, 0.7,
0.35, 0.2, 0.7,
0.4, 0.1, 0.7,
0.35, 0, 0.7,
0.25, 0, 0.7,
0.2, 0.1, 0.7,
#roda 3
0.7, 0.1, 0.7,
0.65, 0.2, 0.7,
0.75, 0.2, 0.7,
0.8, 0.1, 0.7,
0.75, 0, 0.7,
0.65, 0, 0.7,
0.6, 0.1, 0.7,
#roda 4
0.7, 0.1, 0.1,
0.65, 0.2, 0.1,
0.75, 0.2, 0.1,
0.8, 0.1, 0.1,
0.75, 0, 0.1,
0.65, 0, 0.1,
0.6, 0.1, 0.1
        ]
# colors=[
#         0, 0, 0,
#         1, 0, 0,
#         0, 1, 0,
#         0, 0, 1,
#         0, 1, 1,
#         1, 0, 1,
#         1, 1, 1,
#         1, 1, 0,
#         ]
colors=[
        1, 0, 0,
        1, 0, 0,
        1, 0, 0,
        1, 0, 0,
        1, 0, 0,
        1, 0, 0,
        1, 0, 0,
        1, 0, 0,
        1, 0, 0,
        1, 0, 0,
        1, 0, 0,
        1, 0, 0,
        1, 0, 0,
        1, 0, 0,
        1, 0, 0,
        1, 0, 0,
        #roda 1
        0, 0, 0,
        0, 0, 0,
        0, 0, 0,
        0, 0, 0,
        0, 0, 0,
        0, 0, 0,
        0, 0, 0,
        #roda 2
        0, 0, 0,
        0, 0, 0,
        0, 0, 0,
        0, 0, 0,
        0, 0, 0,
        0, 0, 0,
        0, 0, 0,
        #roda 3
        0, 0, 0,
        0, 0, 0,
        0, 0, 0,
        0, 0, 0,
        0, 0, 0,
        0, 0, 0,
        0, 0, 0,
        #roda 4
        0, 0, 0,
        0, 0, 0,
        0, 0, 0,
        0, 0, 0,
        0, 0, 0,
        0, 0, 0,
        0, 0, 0
        ]
# indices=[
#         0, 1, 2, 2, 3, 0,
#         0, 4, 5, 5, 1, 0,
#         1, 5, 6, 6, 2, 1,
#         2, 6, 7, 7, 3, 2,
#         3, 7, 4, 4, 0, 3,
#         4, 7, 6, 6, 5, 4,
#         ]
indices=[
0, 1, 2, 2, 3, 0,
6, 7, 4, 4, 5, 6,
8, 9, 10, 10, 11, 8,
14, 15, 12, 12, 13, 14,
8, 9, 1, 1, 0, 8,
15, 8, 0, 0, 7, 15,
14, 15, 7, 7, 6, 14,
13, 14, 6, 6, 5, 13,
12, 13, 5, 5, 4, 12,
11, 12, 4, 4, 3, 11,
10, 11, 3, 3, 2, 10,
#roda 1
16, 17, 18, 16, 18, 19,
16, 19, 20, 16, 20, 21,
16, 21, 22, 16, 22, 17,
#roda 2
23, 24, 25, 23, 25, 26,
23, 26, 27, 23, 27, 28,
23, 28, 29, 23, 24, 29,
#roda 3
30, 31, 32, 30, 32, 33,
30, 33, 34, 30, 34, 35,
30, 35, 36, 30, 31, 36,
#roda 4
37, 38, 39, 37, 39, 40,
37, 40, 41, 37, 41, 42,
37, 42, 43, 37, 38, 43
        ]

buffers=None
def create_vbo():
    buffers = glGenBuffers(3)
    glBindBuffer(GL_ARRAY_BUFFER, buffers[0])
    glBufferData(GL_ARRAY_BUFFER, 
            len(vertices)*4,  # byte size
            (ctypes.c_float*len(vertices))(*vertices), 
            GL_STATIC_DRAW)
    glBindBuffer(GL_ARRAY_BUFFER, buffers[1])
    glBufferData(GL_ARRAY_BUFFER, 
            len(colors)*4, # byte size 
            (ctypes.c_float*len(colors))(*colors), 
            GL_STATIC_DRAW)
    glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, buffers[2])
    glBufferData(GL_ELEMENT_ARRAY_BUFFER, 
            len(indices)*4, # byte size
            (ctypes.c_uint*len(indices))(*indices), 
            GL_STATIC_DRAW)
    return buffers

def draw_vbo():
    glEnableClientState(GL_VERTEX_ARRAY);
    glEnableClientState(GL_COLOR_ARRAY);
    glBindBuffer(GL_ARRAY_BUFFER, buffers[0]);
    glVertexPointer(3, GL_FLOAT, 0, None);
    glBindBuffer(GL_ARRAY_BUFFER, buffers[1]);
    glColorPointer(3, GL_FLOAT, 0, None);
    glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, buffers[2]);
    glDrawElements(GL_TRIANGLES, len(indices), GL_UNSIGNED_INT, None);
    glDisableClientState(GL_COLOR_ARRAY)
    glDisableClientState(GL_VERTEX_ARRAY);

shader=None
def draw_cube3():
    global shader, buffers
    if shader==None:
        shader=Shader()
        shader.initShader('''
void main()
{
    gl_Position = gl_ModelViewProjectionMatrix * gl_Vertex;
    gl_FrontColor = gl_Color;
}
        ''',
        '''
void main()
{
    gl_FragColor = gl_Color;
}
        ''')
        buffers=create_vbo()

    shader.begin()
    draw_vbo()
    shader.end()

##############################################################################
def reshape_func(w, h):
    resize(w, h == 0 and 1 or h)

def disp_func():
    draw()
    glutSwapBuffers()

def keyboard_down(key, x, y):
    if (key=='a'):
        global offsetX
        offsetX= 0.1
    elif (key=='d'):
        global offsetX
        offsetX= -0.1
    elif (key=='w'):
        global offsetZ
        offsetZ= 0.1
    elif (key=='s'):
        global offsetZ
        offsetZ= -0.1

def keyboard_up(key, x, y):
    if (key=='a'):
        global offsetX
        offsetX= 0
    elif (key=='d'):
        global offsetX
        offsetX= 0
    elif (key=='w'):
        global offsetZ
        offsetZ= 0
    elif (key=='s'):
        global offsetZ
        offsetZ= 0

def callback_mouse_button(button, state, x, y):
    # printf ("%d, %d\n", button, state);
    # Note: if it GLUT_LEFT_BUTTON isn't defined use
    # 0 for the left mouse button
    # 1 for the middle mouse button
    # 2 for the right mouse button
    if (button == 0 and state == GLUT_DOWN):
        print("left button")
        print("pressed")
        global offZ
        offZ= 0.01
    elif (button == 0 and state == GLUT_UP):
        print("left button")
        print("released")
        global offZ
        offZ= 0
    elif (button == 2 and state == GLUT_DOWN):
        print("right button")
        print("pressed")
        global offZ
        offZ= -0.01
    elif (button == 2 and state == GLUT_UP):
        print("right button")
        print("released")
        global offZ
        offZ= 0

if __name__=="__main__":
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
    glutInitWindowSize(512, 512)
    glutCreateWindow(b"vbo")
    glutDisplayFunc(disp_func)
    glutIdleFunc(disp_func)
    glutReshapeFunc(reshape_func)
    glutKeyboardFunc(keyboard_down)
    glutKeyboardUpFunc(keyboard_up)
    glutMouseFunc (callback_mouse_button)

    initialize()

    glutMainLoop()
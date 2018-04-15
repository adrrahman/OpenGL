import glfw
from OpenGL.GL import *
import OpenGL.GL.shaders
import numpy
import pyrr
from PIL import Image

rotateX= 0

def main():

	if not glfw.init():
		return

	window = glfw.create_window(800, 600, "My OpenGL window", None, None)
	glfw.set_key_callback(window, keyCallback)

	if not window:
		glfw.terminate()
		return

	glfw.make_context_current(window)

	# cube = [
	# 		-0.5, -0.5,  0.5,  1.0, 0.0, 0.0,  0.0, 0.0,
 #             0.5, -0.5,  0.5,  0.0, 1.0, 0.0,  1.0, 0.0,
 #             0.5,  0.5,  0.5,  0.0, 0.0, 1.0,  1.0, 1.0,
 #            -0.5,  0.5,  0.5,  1.0, 1.0, 1.0,  0.0, 1.0,

 #            -0.5, -0.5, -0.5,  1.0, 0.0, 0.0,  0.0, 0.0,
 #             0.5, -0.5, -0.5,  0.0, 1.0, 0.0,  1.0, 0.0,
 #             0.5,  0.5, -0.5,  0.0, 0.0, 1.0,  1.0, 1.0,
 #            -0.5,  0.5, -0.5,  1.0, 1.0, 1.0,  0.0, 1.0,

 #             0.5, -0.5, -0.5,  1.0, 0.0, 0.0,  0.0, 0.0,
 #             0.5,  0.5, -0.5,  0.0, 1.0, 0.0,  1.0, 0.0,
 #             0.5,  0.5,  0.5,  0.0, 0.0, 1.0,  1.0, 1.0,
 #             0.5, -0.5,  0.5,  1.0, 1.0, 1.0,  0.0, 1.0,

 #            -0.5,  0.5, -0.5,  1.0, 0.0, 0.0,  0.0, 0.0,
 #            -0.5, -0.5, -0.5,  0.0, 1.0, 0.0,  1.0, 0.0,
 #            -0.5, -0.5,  0.5,  0.0, 0.0, 1.0,  1.0, 1.0,
 #            -0.5,  0.5,  0.5,  1.0, 1.0, 1.0,  0.0, 1.0,

 #            -0.5, -0.5, -0.5,  1.0, 0.0, 0.0,  0.0, 0.0,
 #             0.5, -0.5, -0.5,  0.0, 1.0, 0.0,  1.0, 0.0,
 #             0.5, -0.5,  0.5,  0.0, 0.0, 1.0,  1.0, 1.0,
 #            -0.5, -0.5,  0.5,  1.0, 1.0, 1.0,  0.0, 1.0,

 #             0.5,  0.5, -0.5,  1.0, 0.0, 0.0,  0.0, 0.0,
 #            -0.5,  0.5, -0.5,  0.0, 1.0, 0.0,  1.0, 0.0,
 #            -0.5,  0.5,  0.5,  0.0, 0.0, 1.0,  1.0, 1.0,
 #             0.5,  0.5,  0.5,  1.0, 1.0, 1.0,  0.0, 1.0
	# ]
	cube = [
        0.1, 0.4, 0.1, 1, 0, 0, 0.1, 0.4,
        0.1, 0.1, 0.1, 1, 0, 0, 0.1, 0.1,
        0.9, 0.1, 0.1, 1, 0, 0, 0.9, 0.1,
        0.9, 0.4, 0.1, 1, 0, 0, 0.9, 0.4,
        0.8, 0.4, 0.1, 1, 0, 0, 0.8, 0.4,
        0.7, 0.9, 0.1, 1, 0, 0, 0.7, 0.9,
        0.4, 0.9, 0.1, 1, 0, 0, 0.4, 0.9,
        0.3, 0.4, 0.1, 1, 0, 0, 0.3, 0.4,
        0.1, 0.4, 0.7, 1, 0, 0, 0.1, 0.4,
        0.1, 0.1, 0.7, 1, 0, 0, 0.1, 0.1,
        0.9, 0.1, 0.7, 1, 0, 0, 0.9, 0.1,
        0.9, 0.4, 0.7, 1, 0, 0, 0.9, 0.4,
        0.8, 0.4, 0.7, 1, 0, 0, 0.8, 0.4,
        0.7, 0.9, 0.7, 1, 0, 0, 0.7, 0.9,
        0.4, 0.9, 0.7, 1, 0, 0, 0.4, 0.9,
        0.3, 0.4, 0.7, 1, 0, 0, 0.3, 0.4,
        #roda 1
        0.3, 0.1, 0.1, 0, 0, 0, 0.0, 0.0,
        0.25, 0.2, 0.1, 0, 0, 0, 0.0, 0.0,
        0.35, 0.2, 0.1, 0, 0, 0, 0.0, 0.0,
        0.4, 0.1, 0.1, 0, 0, 0, 0.0, 0.0,
        0.35, 0, 0.1, 0, 0, 0, 0.0, 0.0,
        0.25, 0, 0.1, 0, 0, 0, 0.0, 0.0,
        0.2, 0.1, 0.1, 0, 0, 0, 0.0, 0.0,
        #roda 2
        0.3, 0.1, 0.7, 0, 0, 0, 0.0, 0.0,
        0.25, 0.2, 0.7, 0, 0, 0, 0.0, 0.0,
        0.35, 0.2, 0.7, 0, 0, 0, 0.0, 0.0,
        0.4, 0.1, 0.7, 0, 0, 0, 0.0, 0.0,
        0.35, 0, 0.7, 0, 0, 0, 0.0, 0.0,
        0.25, 0, 0.7, 0, 0, 0, 0.0, 0.0,
        0.2, 0.1, 0.7, 0, 0, 0, 0.0, 0.0,
        #roda 3
        0.7, 0.1, 0.7, 0, 0, 0, 0.0, 0.0,
        0.65, 0.2, 0.7, 0, 0, 0, 0.0, 0.0,
        0.75, 0.2, 0.7, 0, 0, 0, 0.0, 0.0,
        0.8, 0.1, 0.7, 0, 0, 0, 0.0, 0.0,
        0.75, 0, 0.7, 0, 0, 0, 0.0, 0.0,
        0.65, 0, 0.7, 0, 0, 0, 0.0, 0.0,
        0.6, 0.1, 0.7, 0, 0, 0, 0.0, 0.0,
        #roda 4
        0.7, 0.1, 0.1, 0, 0, 0, 0.0, 0.0,
        0.65, 0.2, 0.1, 0, 0, 0, 0.0, 0.0,
        0.75, 0.2, 0.1, 0, 0, 0, 0.0, 0.0,
        0.8, 0.1, 0.1, 0, 0, 0, 0.0, 0.0,
        0.75, 0, 0.1, 0, 0, 0, 0.0, 0.0,
        0.65, 0, 0.1, 0, 0, 0, 0.0, 0.0,
        0.6, 0.1, 0.1, 0, 0, 0, 0.0, 0.0
	]

	cube = numpy.array(cube, dtype = numpy.float32)

	indices = [
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

	indices = numpy.array(indices, dtype= numpy.uint32)

	vertex_shader = """
    #version 330
    in layout(location = 0) vec3 position;
    in layout(location = 1) vec3 color;
    in layout(location = 2) vec2 textureCoords;
    uniform mat4 transform;
    out vec3 newColor;
    out vec2 newTexture;
    void main()
    {
        gl_Position = transform * vec4(position, 1.0f);
        newColor = color;
        newTexture = textureCoords;
    }
    """

	fragment_shader = """
    #version 330
    in vec3 newColor;
    in vec2 newTexture;
    out vec4 outColor;
    uniform sampler2D samplerTexture;
    void main()
    {
        outColor = texture(samplerTexture, newTexture) * vec4(newColor, 1.0f);
    }
    """
	shader = OpenGL.GL.shaders.compileProgram(OpenGL.GL.shaders.compileShader(vertex_shader, GL_VERTEX_SHADER),
                                              OpenGL.GL.shaders.compileShader(fragment_shader, GL_FRAGMENT_SHADER))

	VBO = glGenBuffers(1)
	glBindBuffer(GL_ARRAY_BUFFER, VBO)
	glBufferData(GL_ARRAY_BUFFER, cube.itemsize * len(cube), cube, GL_STATIC_DRAW)

	EBO = glGenBuffers(1)
	glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, EBO)
	glBufferData(GL_ELEMENT_ARRAY_BUFFER, indices.itemsize * len(indices), indices, GL_STATIC_DRAW)
	#position
	glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, cube.itemsize * 8, ctypes.c_void_p(0))
	glEnableVertexAttribArray(0)
	#color
	glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, cube.itemsize * 8, ctypes.c_void_p(12))
	glEnableVertexAttribArray(1)
	#texture
	glVertexAttribPointer(2, 2, GL_FLOAT, GL_FALSE, cube.itemsize * 8, ctypes.c_void_p(24))
	glEnableVertexAttribArray(2)

	texture = glGenTextures(1)
	glBindTexture(GL_TEXTURE_2D, texture)
	# Set the texture wrapping parameters
	glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
	glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
	# Set texture filtering parameters
	glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
	glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
	# load image
	image = Image.open("index.jpg")
	img_data = numpy.array(list(image.getdata()), numpy.uint8)
	glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, image.width, image.height, 0, GL_RGB, GL_UNSIGNED_BYTE, img_data)
	glEnable(GL_TEXTURE_2D)

	glUseProgram(shader)

	glClearColor(0.2, 0.3, 0.2, 1.0)
	glEnable(GL_DEPTH_TEST)

	#glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)

	while not glfw.window_should_close(window):
		glfw.poll_events()

		glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

		rot_x = pyrr.Matrix44.from_x_rotation(0.5 * glfw.get_time() )
		rot_y = pyrr.Matrix44.from_y_rotation(0.5 * glfw.get_time() )

		transformLoc = glGetUniformLocation(shader, "transform")
		glUniformMatrix4fv(transformLoc, 1, GL_FALSE, rot_x * rot_y)

		glDrawElements(GL_TRIANGLES, len(indices), GL_UNSIGNED_INT, None)

		glfw.swap_buffers(window)

	glfw.terminate()

def keyCallback(window, key, scancode, action, mods):
	print(key)

if __name__ == "__main__":
	main()
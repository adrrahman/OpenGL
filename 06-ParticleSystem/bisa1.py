import glfw
from OpenGL.GL import *
from PIL import Image
from collections import namedtuple
import OpenGL.GL.shaders
import numpy
import pyrr
from ctypes import *
# import particle

rotateX = 0
rotateY = 0
MaxParticles = 100000
Particle = namedtuple('Particle',['position', 'speed', 'r', 'g', 'b', 'a', 'size', 'angle', 'weight', 'life'])

def main():

	if not glfw.init():
		return

	window = glfw.create_window(800, 600, "My OpenGL window", None, None)
	glfw.set_key_callback(window, keyCallback)

	if not window:
		glfw.terminate()
		return

	glfw.make_context_current(window)

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

	g_vertex_buffer_data = [
	-0.5, -0.5, 0.0,
	0.5, -0.5, 0.0,
	-0.5, 0.5, 0.0,
	0.5, 0.5, 0.0
	]

	indices = numpy.array(indices, dtype= numpy.uint32)
	g_vertex_buffer_data = numpy.array(g_vertex_buffer_data, dtype = numpy.float32)

	vertex_shader = """
	#version 330
	in layout(location = 0) vec3 position;
	in layout(location = 1) vec3 color;
	in layout(location = 2) vec2 textureCoords;
	in layout (location = 3) vec3 vertNormal;
//	in layout (location = 4) vec3 billboard;
	in layout (location = 5) vec3 positionParticle;
	in layout (location = 6) vec3 colorParticle;

	uniform mat4 transform;
	out vec3 newColor;
	out vec2 newTexture;
	out vec3 fragNormal;

	uniform mat4 light;

	void main()	
	{
		newColor = color;
		newTexture = textureCoords;
		fragNormal = (light * vec4(vertNormal, 0.0f)).xyz;
		gl_Position = transform * vec4(position, 1.0f);
	}
	"""

	fragment_shader = """
	#version 330
	in vec3 newColor;
	in vec2 newTexture;
	in vec3 fragNormal;

	out vec4 outColor;
	uniform sampler2D samplerTexture;
	
	void main()
	{
		vec3 ambientLightIntensity = vec3(0.3f, 0.2f, 0.4f);
	    vec3 sunLightIntensity = vec3(0.9f, 0.9f, 0.9f);
	    vec3 sunLightDirection = normalize(vec3(-2.0f, -2.0f, 0.0f));

	    vec4 texel = texture(samplerTexture, newTexture);

	    vec3 lightIntensity = ambientLightIntensity + sunLightIntensity * max(dot(fragNormal, sunLightDirection), 0.0f);

	    outColor = vec4(texel.rgb * lightIntensity, texel.a);
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

	ParticlesCount = 1000
	LastUsedParticle = 0
	delta = 1.0

	# particle
	billboard_vertex_buffer = glGenBuffers(1)
	glBindBuffer(GL_ARRAY_BUFFER, billboard_vertex_buffer)
	glBufferData(GL_ARRAY_BUFFER, len(g_vertex_buffer_data), g_vertex_buffer_data, GL_STATIC_DRAW)
	# particle position and size
	particles_position_buffer = glGenBuffers(1)
	glBindBuffer(GL_ARRAY_BUFFER, particles_position_buffer)
	glBufferData(GL_ARRAY_BUFFER, MaxParticles * 4 * ctypes.sizeof(GLfloat), None, GL_STREAM_DRAW)
	glBufferSubData(GL_ARRAY_BUFFER, 0, ParticlesCount * ctypes.sizeof(GLfloat) * 4, particles_position_buffer)
	# particle color
	particles_color_buffer = glGenBuffers(1)
	glBindBuffer(GL_ARRAY_BUFFER, particles_color_buffer)
	glBufferData(GL_ARRAY_BUFFER, MaxParticles * 4 * ctypes.sizeof(GLubyte), None, GL_STREAM_DRAW)
	glBufferSubData(GL_ARRAY_BUFFER, 0, ParticlesCount * ctypes.sizeof(GLubyte) * 4, particles_color_buffer)

	#positions
	glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, cube.itemsize * 8, ctypes.c_void_p(0))
	glEnableVertexAttribArray(0)
	#colors
	glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, cube.itemsize * 8, ctypes.c_void_p(12))
	glEnableVertexAttribArray(1)
	#textures
	glVertexAttribPointer(2, 2, GL_FLOAT, GL_FALSE, cube.itemsize * 8, ctypes.c_void_p(24))
	glEnableVertexAttribArray(2)
	#normals
	glVertexAttribPointer(3, 3, GL_FLOAT, GL_FALSE, cube.itemsize * 8, ctypes.c_void_p(36))
	glEnableVertexAttribArray(3)
	# particles vertices
	glEnableVertexAttribArray(4)
	glBindBuffer(GL_ARRAY_BUFFER, billboard_vertex_buffer)
	glVertexAttribPointer(4, 3, GL_FLOAT, GL_FALSE, 0, ctypes.c_void_p(48))
	# particles position
	glEnableVertexAttribArray(5)
	glBindBuffer(GL_ARRAY_BUFFER, particles_position_buffer)
	glVertexAttribPointer(5, 4, GL_FLOAT, GL_FALSE, 0, ctypes.c_void_p(60))
	# particles color
	glEnableVertexAttribArray(6)
	glBindBuffer(GL_ARRAY_BUFFER, particles_color_buffer)
	glVertexAttribPointer(6, 4, GL_UNSIGNED_BYTE, GL_TRUE, 0, ctypes.c_void_p(72))

	# make another instance particle
	glVertexAttribDivisor(4, 0)
	glVertexAttribDivisor(5, 1)
	glVertexAttribDivisor(6, 1)
	glDrawArraysInstanced(GL_TRIANGLE_STRIP, 0, 4, ParticlesCount)

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

	# glUseProgram(lightingShader)
	glUseProgram(shader)

	glClearColor(0.2, 0.3, 0.2, 1.0)
	glEnable(GL_DEPTH_TEST)

	#glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)

	for i in range (0, MaxParticles):
		ParticleContainer[i] = Particle(position = [0.0, 0.0, 0.0], speed = [0.0, 0.0, 0.0], r = 0x01, g = 0x01, b = 0x01, a = 0x01, size = 0.0, angle = 0.0, weight
			 = 0.0, life = 0.0)

	while not glfw.window_should_close(window):
		glfw.poll_events()

		glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

		rot_x = pyrr.Matrix44.from_x_rotation(0.5 * rotateX )
		rot_y = pyrr.Matrix44.from_y_rotation(0.5 * rotateY )

		transformLoc = glGetUniformLocation(shader, "transform")
		lightLoc = glGetUniformLocation(shader, "light")

		glUniformMatrix4fv(transformLoc, 1, GL_FALSE, rot_x * rot_y)
		glUniformMatrix4fv(lightLoc, 1, GL_FALSE, rot_x * rot_y)

		for i in range(0, MaxParticles):
			P = ParticleContainer[i]

			if(P.life > 0.0):
				P(life = P.life - delta)
				if(P.life > 0.0):
					P(speed = P.speed + ([0.0, -9.81, 0.0] * delta * 0.5))
					P(position = P.position + (P.speed * delta))

					g_particule_position_size_data[4 * ParticlesCount + 0] = P.position[0]
					g_particule_position_size_data[4 * ParticlesCount + 1] = P.position[1]
					g_particule_position_size_data[4 * ParticlesCount + 2] = P.position[2]

					g_particule_position_size_data[4 * ParticlesCount + 3] = P.size

					g_particule_color_data[4 * ParticlesCount + 0] = P.r
					g_particule_color_data[4 * ParticlesCount + 1] = P.g
					g_particule_color_data[4 * ParticlesCount + 2] = P.b
					g_particule_color_data[4 * ParticlesCount + 3] = P.a

			ParticlesCount = ParticlesCount + 1

		glDrawElements(GL_TRIANGLES, len(indices), GL_UNSIGNED_INT, None)

		glfw.swap_buffers(window)

	glfw.terminate()

def keyCallback(window, key, scancode, action, mods):
	global rotateX, rotateY
	print(key)
	print(rotateY)
	if (key==262):
		rotateY+=0.5
	elif (key==263):
		rotateY-=0.5
	elif (key==264):
		rotateX+=0.5
	elif (key==265):
		rotateX-=0.5

def FindUnUsedParticle():
	for i in range (LastUsedParticle, MaxParticles):
		if(ParticleContainer[i].life < 0):
			LastUsedParticle = i
			return i
	for i in range(0, LastUsedParticle):
		if(ParticleContainer[i].life < 0):
			LastUsedParticle = i
			return i
	return 0


if __name__ == "__main__":
	main()
class Particle(object):
	def __init__(self):
		self.position = [0.0, 0.0, 0.0]
		self.speed = [0.0, 0.0, 0.0]
		self.r, self.g, self.b, self.a = 0x01
		self.size, self.angle, self.weight, self.life = 0.0

	def position(self):
		return self.position

	def position(self, x, y, z):
		self.position = [x,y,z]

	def speed(self):
		return self.speed

	def speed(self, x, y, z):
		self.speed = [x,y,z]

	def r(self):
		return self.r

	def r(self, r):
		self.r = r

	def g(self):
		return self.g

	def g(self, g):
		self.g = g

	def b(self):
		return self.b

	def b(self, b):
		self.b = b

	def a(self):
		return self.a

	def a(self, a):
		self.a = a

	def size(self):
		return self.size

	def size(self, size):
		self.size = size

	def angle(self):
		return self.angle

	def angle(self, angle):
		self.angle = angle

	def weight(self):
		return  self.weight

	def weight(self, weight):
		self.weight = weight

	def life(self):
		return self.life

	def life(self, life):
		self.life = life	
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

# Визначимо функцію для створення куба
def draw_cube(vertices, edges):
	for edge in edges:
		glBegin(GL_LINES)
		for vertex in edge:
			glVertex3fv(vertices[vertex])
		glEnd()

# Визначимо функцію для спавну куба
def spawn_cube(position, color, cubes):
	size = 1
	x, y, z = position
	x = x-(x % 2)
	y = y-(y % 2)
	z = z-(z % 2)
	cubes.append(((x, z, y), size, (color)))

# Визначимо функцію для відображення кубів
def draw_cubes(cubes, vertices, edges):
	for cube in cubes:
		position, size, color = cube
		r, g, b = color
		glColor4f(r, g, b, 1)
		glPushMatrix()
		glTranslatef(*position)
		draw_cube(vertices, edges)
		glPopMatrix()

def main():
	pygame.init()
	window_size = (600, 300)
	screen = pygame.display.set_mode(window_size, DOUBLEBUF | OPENGL)

	glEnable(GL_DEPTH_TEST)
	glEnable(GL_LIGHTING)
	glShadeModel(GL_SMOOTH)
	glEnable(GL_COLOR_MATERIAL)
	glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)

	glEnable(GL_LIGHT0)
	glLightfv(GL_LIGHT0, GL_AMBIENT, [0.5, 0.5, 0.5, 1])
	glLightfv(GL_LIGHT0, GL_DIFFUSE, [1.0, 1.0, 1.0, 1])

	sphere_object = gluNewQuadric() 

	glMatrixMode(GL_PROJECTION)
	gluPerspective(45, (window_size[0]/window_size[1]), 0.1, 50.0)

	glMatrixMode(GL_MODELVIEW)
	gluLookAt(0, -8, 0, 0, 0, 0, 0, 0, 1)
	view_matrix = glGetFloatv(GL_MODELVIEW_MATRIX)
	glLoadIdentity()

	window_center = [screen.get_size()[i] // 2 for i in range(2)]

	vertical_angle = 0.0
	is_paused = False
	is_running = True

	# Створимо список для зберігання кубів
	cubes = []
	vertices = [(1, -1, -1), (1, 1, -1), (-1, 1, -1), (-1, -1, -1), (1, -1, 1), (1, 1, 1), (-1, -1, 1), (-1, 1, 1)]
	edges = [(0, 1), (0, 3), (0, 4), (2, 1), (2, 3), (2, 7), (6, 3), (6, 4), (6, 7), (5, 1), (5, 4), (5, 7)]
	ver = []

	while is_running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_r:
					spawn_cube((0, 0, 2), (1, 0, 1), cubes)
					spawn_cube((0, 0, 0), (1, 0, 0), cubes)
					spawn_cube((0, 2, 0), (0, 1, 0), cubes)
					spawn_cube((0, 2, 2), (0, 1, 1), cubes)

					spawn_cube((2, 0, 2), (1, 0, 1), cubes)
					spawn_cube((2, 0, 0), (1, 0, 0), cubes)
					spawn_cube((2, 2, 0), (0, 1, 0), cubes)
					spawn_cube((2, 2, 2), (0, 1, 1), cubes)

		keypress = pygame.key.get_pressed()
		
		glLoadIdentity()

		glPushMatrix()
		glLoadIdentity()

		if keypress[pygame.K_w]:
			glTranslatef(0,0,0.1)
		if keypress[pygame.K_s]:
			glTranslatef(0,0,-0.1)
		if keypress[pygame.K_d]:
			glTranslatef(-0.1,0,0)
		if keypress[pygame.K_a]:
			glTranslatef(0.1,0,0)

		if keypress[pygame.K_LEFT]:
			glRotatef(-1, 0, 1, 0)
		if keypress[pygame.K_RIGHT]:
			glRotatef(1, 0, 1, 0)

		glMultMatrixf(view_matrix)
		view_matrix = glGetFloatv(GL_MODELVIEW_MATRIX)

		glPopMatrix()
		glMultMatrixf(view_matrix)

		glLightfv(GL_LIGHT0, GL_POSITION, [1, -1, 1, 0])

		glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

		#glPushMatrix()

		glColor4f(0.5, 0.5, 0.5, 1)
		glBegin(GL_QUADS)
		glVertex3f(-10, -10, -2)
		glVertex3f(10, -10, -2)
		glVertex3f(10, 10, -2)
		glVertex3f(-10, 10, -2)
		glEnd()

		# Відображаємо куби
		draw_cubes(cubes, vertices, edges)

		pygame.display.flip()
		pygame.time.wait(10)

	pygame.quit()

if __name__ == "__main__":
	main()

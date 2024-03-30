import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

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
while is_running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			  pygame.quit()

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
	if keypress[pygame.K_UP]:
		glRotatef(-1, 1, 0, 0)
	if keypress[pygame.K_DOWN]:
		glRotatef(1, 1, 0, 0)

	glMultMatrixf(view_matrix)
	view_matrix = glGetFloatv(GL_MODELVIEW_MATRIX)

	glPopMatrix()
	glMultMatrixf(view_matrix)

	glLightfv(GL_LIGHT0, GL_POSITION, [1, -1, 1, 0])

	glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

	glPushMatrix()

	glColor4f(0.5, 0.5, 0.5, 1)
	glBegin(GL_QUADS)
	glVertex3f(-10, -10, -2)
	glVertex3f(10, -10, -2)
	glVertex3f(10, 10, -2)
	glVertex3f(-10, 10, -2)
	glEnd()

	glTranslatef(-1.5, 0, 0)
	glColor4f(0.5, 0.2, 0.2, 1)
	gluSphere(sphere_object, 1.0, 32, 16) 

	glTranslatef(3, 0, 0)
	glColor4f(0.2, 0.2, 0.5, 1)
	gluSphere(sphere_object, 1.0, 32, 16) 

	glPopMatrix()

	pygame.display.flip()
	pygame.time.wait(10)

pygame.quit()

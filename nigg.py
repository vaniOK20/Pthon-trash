import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

pygame.init()
display = (800, 600)
pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
clock=pygame.time.Clock()

glMatrixMode(GL_PROJECTION)
gluPerspective(45, (800/600), 0.1, 50.0)

glMatrixMode(GL_MODELVIEW)
gluLookAt(0, -8, 0, 0, 0, 0, 0, 0, 1)# Rotate
view_matrix = glGetFloatv(GL_MODELVIEW_MATRIX)
glLoadIdentity()

while True:
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

    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

    glBegin(GL_QUADS)
    #Floor
    glColor4f(0.5, 0.5, 0.5, 1)
    glVertex3f(-10, -10, -2)
    glVertex3f(10, -10, -2)
    glVertex3f(10, 10, -2)
    glVertex3f(-10, 10, -2)

    #Wall
    glColor4f(1, 0.5, 0.5, 1)
    glVertex3f(10, -10, -2)
    glVertex3f(10, -10, 3)
    glVertex3f(10, 10, 3)
    glVertex3f(10, 10, -2)
    glEnd()

    pygame.display.flip()
    clock.tick(60)

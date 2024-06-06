import pygame
import random as ran

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((800, 600))

black=(0, 0, 0)
white=(255, 255, 255)

blocks=[(0, 0, (0, 0, 0))]

x_cam=0
y_cam=0
MouseUsed=False

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()

	key=pygame.key.get_pressed()
	mouseC=pygame.mouse.get_pressed()
	mouseP=pygame.mouse.get_pos()

	if key[pygame.K_RIGHT]:
		x_cam+=5
	if key[pygame.K_LEFT]:
		x_cam-=5
	if key[pygame.K_UP]:
		y_cam-=5
	if key[pygame.K_DOWN]:
		y_cam+=5

	if not mouseC[0]: MouseUsed=False

	if mouseC[0] and not MouseUsed:
		blocks.append((mouseP[0]+x_cam, mouseP[1]+y_cam, (ran.randint(0, 255), ran.randint(0, 255), ran.randint(0, 255))))
		MouseUsed=True

	screen.fill(white)
	for i in range(len(blocks)):
		pygame.draw.rect(screen, blocks[i][2], ((blocks[i][0]-(blocks[i][0]%50))-x_cam, (blocks[i][1]-(blocks[i][1]%50))-y_cam, 50, 50))

	pygame.display.flip()
	clock.tick(60)

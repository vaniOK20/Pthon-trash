import pygame

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((800, 600))

black=(0, 0, 0)
white=(255, 255, 255)

objects=[[0, 0, 50, 50], [60, 60, 50, 50]]

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()

	key=pygame.key.get_pressed()

	if key[pygame.K_RIGHT]:
		pass
	objects[0][1]=objects[0][1]+1

	screen.fill(white)
	for i in range(len(objects)):
		pygame.draw.rect(screen, black, (objects[i][0], objects[i][1], objects[i][2], objects[i][3]))

	pygame.display.flip()
	clock.tick(60)
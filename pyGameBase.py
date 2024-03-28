import pygame

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((800, 600))

black=(0, 0, 0)
white=(255, 255, 255)

platforms=[[700, 490, 100, 50], [500, 490, 50, 50], [0, 590, 800, 10]]

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()

	key=pygame.key.get_pressed()

	if key[pygame.K_RIGHT]:
		print('sas')

	screen.fill(white)
	pygame.draw.rect(screen, black, (0, 0, 50, 50))

	pygame.display.flip()
	clock.tick(60)
import pygame
#if not ((not (platforms[i][1]-y_camera)-platforms[i][3]-50>=y and not (platforms[i][1]-y_camera)<=y) and ((platforms[i][0]+x_camera)-60<=x and (platforms[i][0]+x_camera)>=x)) and not ((not (platforms[i][1]-y_camera)-platforms[i][3]-50>=y and not (platforms[i][1]-y_camera)<=y) and ((platforms[i][0]+x_camera)+platforms[i][2]<=x and (platforms[i][0]+x_camera)+platforms[i][2]+10>=x)):

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((800, 600))

x=800/2
y=0
y_speed=0
jump=False
platform=600
x_camera=0
y_camera=0
black=(0, 0, 0)
white=(255, 255, 255)

platforms=[[700, 490, 100, 50], [500, 490, 50, 50], [0, 590, 800, 10]]

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()

	key=pygame.key.get_pressed()

	for i in range(len(platforms)):
		if platforms[i][0]-x_camera<=x+50 and platforms[i][2]+platforms[i][0]-x_camera>=x and platforms[i][1]-y_camera>=y+50:
			platform=(platforms[i][1]-y_camera)-50
			break
		else:
			platform=600
			i=i+1

	if not jump:
		if y+50>=platform:
			if key[pygame.K_w] or key[pygame.K_SPACE]:
				jump=True
				y_speed=y_speed+20
	else:
		if y+50>=platform:
			jump=False
			y_speed=0
	if key[pygame.K_a]:
		x=x-5
	if key[pygame.K_d]:
		x=x+5

	if y<platform-50 or jump:
		y_speed=y_speed-1
		y=y-y_speed
	else:
		y_speed=0
		if jump is False: y=platform-50

	if key[pygame.K_RIGHT]:
		x_camera=x_camera+5
		x=x-5

	screen.fill(white)
	pygame.draw.rect(screen, black, (x, y+50, 50, 50))
	for i in range(len(platforms)):
		pygame.draw.rect(screen, black, (platforms[i][0]-x_camera, platforms[i][1]-y_camera, platforms[i][2], platforms[i][3]))
		i=i+1

	pygame.display.flip()
	clock.tick(60)
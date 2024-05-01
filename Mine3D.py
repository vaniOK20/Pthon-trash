import pygame

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((800, 600))

black=(0, 0, 0)
white=(255, 255, 255)
objects = [(50, 0, 1.2), (0, 0, 1.3)]
camera_x=0
camera_y=0

def Draw(x1, y1, x2, y2):
	pygame.draw.rect(screen, black, (x1, y1, 50, 50), 3)

	pygame.draw.line(screen, black, (x1, y1+50), (x2, y2+50), 3)
	pygame.draw.line(screen, black, (x1+50, y1+50), (x2+50, y2+50), 3)

	pygame.draw.line(screen, black, (x1, y1), (x2, y2), 3)
	pygame.draw.line(screen, black, (x1+50, y1), (x2+50, y2), 3)

	pygame.draw.rect(screen, black, (x2, y2, 50, 50), 3)

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()

	key=pygame.key.get_pressed()

	if key[pygame.K_RIGHT]:
		camera_x-=2
	if key[pygame.K_LEFT]:
		camera_x+=2
	if key[pygame.K_UP]:
		camera_y+=2
	if key[pygame.K_DOWN]:
		camera_y-=2

	screen.fill(white)

	x_center=800/2
	y_center=600/2

	for obj in objects:
		obj_x, obj_y, size = obj

		x2=camera_x*size
		y2=camera_y*size

		Draw(camera_x+x_center+obj_x, camera_y+y_center+obj_y, x2+x_center+obj_x, y2+y_center+obj_y)
	pygame.draw.rect(screen, black, (x_center-25, y_center-25, 50, 50))

	pygame.display.flip()
	clock.tick(60)
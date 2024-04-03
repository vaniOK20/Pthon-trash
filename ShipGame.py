import pygame

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((800, 600))

black=(0, 0, 0)
white=(255, 255, 255)

x=0
y=500
xs=0
bom=False
x_b=-100
y_b=-1

score=0

def update():
	global x, xs, bom, x_b, y_b
	if xs<0:
		xs=800
	if key[pygame.K_RIGHT]:
		x+=5
	if key[pygame.K_LEFT]:
		x-=5
	if key[pygame.K_SPACE] and y_b<0:
		x_b=x+(50/2)
		y_b=y-50
		bom=True
	
	screen.fill(white)
	pygame.draw.rect(screen, black, (xs, 0, 50, 50))
	pygame.draw.rect(screen, black, (x, y, 100, 40))
	if bom: pygame.draw.rect(screen, black, (x_b, y_b, 50, 50))
	pygame.display.flip()

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()

	key=pygame.key.get_pressed()

	xs-=5

	if x_b+(50/2)>xs-(50/2) and x_b-(50/2)<xs+(50/2) and y_b<5:
		score+=1
		print(score)
		xs=800

	if bom: y_b-=10

	if y_b<0:
		x_b=-100
		bom=False

	update()

	clock.tick(60)
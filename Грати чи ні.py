import pygame
import math
import sys
import random as ran

pygame.init()
clock=pygame.time.Clock()
screen=pygame.display.set_mode((800, 600))

angle=0
speed=ran.randint(150, 300)

font=pygame.font.Font(None, 25)
text0=font.render('Гулятс', True, (0, 0, 0))
text1=font.render('Піти нахуй', True, (0, 0, 0))

while True:
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			pygame.quit()
			sys.exit()

	angle_rad=math.radians(angle)
	target_x=200+100*math.cos(angle_rad)
	target_y=200+100*math.sin(angle_rad)

	angle+=speed
	if speed>0: speed-=1

	screen.fill((255, 255, 255))
	pygame.draw.line(screen, (255, 0, 0), (200, 200), (target_x, target_y), 5)
	screen.blit(text0, (100, 100))
	screen.blit(text1, (300, 300))

	pygame.display.flip()
	clock.tick(60)
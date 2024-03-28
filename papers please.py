import pygame
import sys

pygame.init()

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

WHITE = (255, 255, 255)

RED = (255, 0, 0)

window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Моя перша гра на Pygame')

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
	elif event.type == pygame.MOUSEBUTTONDOWN:
		if event.button == 1:  # 1 - ліва кнопка миші
			print("Ліва кнопка миші була натиснута")


	mouse_x, mouse_y = pygame.mouse.get_pos()

	window.fill(WHITE)

	pygame.draw.rect(window, RED, (mouse_x-50/2, mouse_y-50/2, 50, 50))

	pygame.display.update()
	pygame.time.Clock().tick(30)

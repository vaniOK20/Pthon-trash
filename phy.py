import pygame
import pymunk
from pymunk.pygame_util import DrawOptions

# Ініціалізуємо Pygame та PyMunk
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
options = DrawOptions(screen)

# Створюємо простий "світ" PyMunk
space = pymunk.Space()
space.gravity = (0, 1000)

# Створюємо статичні та динамічні об'єкти PyMunk
static_line_body = pymunk.Body(body_type=pymunk.Body.STATIC)
static_line = pymunk.Segment(static_line_body, (100, 400), (700, 400), 5)
static_line.friction = 1.0
space.add(static_line_body, static_line)

dynamic_body = pymunk.Body(10, 100)
dynamic_body.position = (400, 100)
dynamic_shape = pymunk.Circle(dynamic_body, 25)
dynamic_shape.friction = 1.0
space.add(dynamic_body, dynamic_shape)

# Основний цикл програми
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Оновлюємо "світ" PyMunk
    space.step(1/60)

    # Очищаємо екран
    screen.fill((255, 255, 255))

    # Малюємо статичні та динамічні об'єкти
    space.debug_draw(options)

    # Оновлюємо відображення
    pygame.display.flip()
    clock.tick(60)

pygame.quit()

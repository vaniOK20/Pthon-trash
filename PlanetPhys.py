import pygame
import math
import random

# Ініціалізація Pygame
pygame.init()

# Визначення кольорів
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Вікно
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Гравітаційна симуляція планет")

# Константи фізики
G = 6.67430e-11  # Гравітаційна стала

# Створення планет
def create_planet(x, y, mass, radius, color, vx, vy):
    return {
        "x": x,
        "y": y,
        "mass": mass,
        "radius": radius,
        "color": color,
        "vx": vx,
        "vy": vy
    }

planets = [
    create_planet((WIDTH // 2)-100, HEIGHT // 2, 1e1, 20, RED, -0.7, 0),
    create_planet(WIDTH // 3, HEIGHT // 3, 1e12, 20, BLUE, 0, 0)
]

# Малювання планети
def draw_planet(screen, planet):
    pygame.draw.circle(screen, planet["color"], (int(planet["x"]), int(planet["y"])), planet["radius"])

# Оновлення положення планет
def update_position(planet, planets):
    ax, ay = 0, 0
    for other in planets:
        if other != planet:
            dx = other["x"] - planet["x"]
            dy = other["y"] - planet["y"]
            distance = math.sqrt(dx**2 + dy**2)
            if distance > 1:  # Щоб уникнути ділення на нуль
                force = G * planet["mass"] * other["mass"] / distance**2
                ax += force * dx / distance / planet["mass"]
                ay += force * dy / distance / planet["mass"]

    planet["vx"] += ax
    planet["vy"] += ay
    planet["x"] += planet["vx"]
    planet["y"] += planet["vy"]

# Основний цикл
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)

    for planet in planets:
        update_position(planet, planets)
        draw_planet(screen, planet)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
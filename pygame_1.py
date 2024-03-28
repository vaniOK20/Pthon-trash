import pygame
import sys
import time

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
LIGHT_BLUE = (100,200,200)
DARK = (0, 0, 0)
RED = (255, 0, 0)
GROUND_HEIGHT = 50

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Platformer")

# Clock to control the frame rate
clock = pygame.time.Clock()

# Player1 settings
player_size = 50
player_x = WIDTH // 2 - player_size // 2
player_y = 10
player_speed = 5
fall_speed = 0
jump_height = 20
is_jumping = False

# Player1 settings
player2_size = 50
player2_x = 250
player2_y = 10
player2_gravity = 0

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Get keys
    keys = pygame.key.get_pressed()

    # Move player
    if keys[pygame.K_a] and player_x > 0:
        if player2_x+player2_size<player_x or player2_x>player_x or player2_y>player_y+player_size-1:
            player_x -= player_speed

    if keys[pygame.K_d] and player_x < WIDTH - player_size:
        if player2_x<player_x or player2_x-player2_size>player_x or player2_y>player_y+player_size-1:
            player_x += player_speed

    if keys[pygame.K_r]:
        player_x = WIDTH // 2 - player_size // 2
        player_y = 10
        fall_speed = 0

    # Jumping
    if not is_jumping:
        if player_y >= 500 or player_y+player_size>player2_y-player2_size/3 and player2_x-player_size<player_x and player2_x+player2_size>player_x:
            if keys[pygame.K_SPACE] or keys[pygame.K_w]:
                is_jumping = True
    else:
        if jump_height >= 0:
            player_y -= jump_height
            jump_height -= 1
        else:
            if player_y <= 500:
                is_jumping = False
                jump_height = 20

    # Apply gravity and fall speed
    #   Player1
    if player_y<HEIGHT-GROUND_HEIGHT-player_size:
        if not player_y>=player2_y-player2_size or player_x>player2_x+player2_size-1 or player_x<player2_x-player2_size+1:
            player_y +=fall_speed+2
            fall_speed += 0.5
        else:
            if player_y+player_size>player2_y-player2_size/4:
                player_y = player2_y-player2_size
                fall_speed = 0
    else:
        fall_speed = 0
        player_y = HEIGHT-GROUND_HEIGHT-player_size

    #   Player2
    if not player2_y>=HEIGHT-GROUND_HEIGHT-player2_size:
        player2_gravity+=1
        player2_y+=player2_gravity
    else:
        player2_y=HEIGHT-GROUND_HEIGHT-player2_size
        player2_gravity=0

    # Drawing
    screen.fill(LIGHT_BLUE)
    pygame.draw.rect(screen, DARK, (player_x, player_y, player_size, player_size))
    pygame.draw.rect(screen, RED, (player2_x, player2_y, player2_size, player2_size))
    pygame.draw.rect(screen, BLUE, (0, HEIGHT - GROUND_HEIGHT, WIDTH, GROUND_HEIGHT))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)

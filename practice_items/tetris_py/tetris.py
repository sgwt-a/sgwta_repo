# pip install pygame
import pygame
from src import tetrominoes  # define tetrominoese block

# Set display size
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Initialize pygame
pygame.init()

# Make display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Initialize tetrominoes position
x, y = 0, 0

# Game loop
running = True
while running:
    # Event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move tetrominoes by keybord
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= 1
    if keys[pygame.K_RIGHT]:
        x += 1

    # Fall tetrominoes by time
    y += 1

    # Display white out
    screen.fill((255, 255, 255))

    # Update display
    pygame.display.flip()

pygame.quit()

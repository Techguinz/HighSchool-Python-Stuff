import pygame
import sys

# Initialize Pygame
pygame.init()

# Game settings
WIDTH, HEIGHT = 800, 600
BG_COLOR = (255, 255, 255)
BUS_COLOR = (0, 0, 255)
BUS_WIDTH, BUS_HEIGHT = 100, 100
BUS_SPEED = 2

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Move the Bus")

bus_x = (WIDTH - BUS_WIDTH) // 2
bus_y = HEIGHT - BUS_HEIGHT - 10

clock = pygame.time.Clock()

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        bus_x -= BUS_SPEED
    if keys[pygame.K_RIGHT]:
        bus_x += BUS_SPEED
    if keys[pygame.K_UP]:
        bus_y -= BUS_SPEED
    if keys[pygame.K_DOWN]:
        bus_y += BUS_SPEED

    bus_x = max(0, min(bus_x, WIDTH - BUS_WIDTH))
    bus_y = max(0, min(bus_y, HEIGHT - BUS_HEIGHT))

    screen.fill(BG_COLOR)

    pygame.draw.rect(screen, BUS_COLOR, (bus_x, bus_y, BUS_WIDTH, BUS_HEIGHT))

    pygame.display.flip()
    clock.tick(60)

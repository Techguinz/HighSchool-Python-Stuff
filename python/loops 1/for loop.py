import pygame
import sys

# Initialize pygame
pygame.init()

# Set up the display
width, height = 1920, 1080
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Bus Drawing")

# Colors
white = (255, 255, 255)
blue = (0, 0, 255)
black = (0, 0, 0)
gray = (169, 169, 169)

# Clear the screen with white color
screen.fill(white)

# Draw the bus body
bus_width, bus_height = 255, 150
bus_x, bus_y = (width - bus_width) / 2, (height - bus_height) / 2
pygame.draw.rect(screen, blue, (bus_x, bus_y, bus_width, bus_height))

# Draw the windows
window_size = 40
window_padding = 10
num_windows =  5
for i in range(num_windows):
    window_x = bus_x + window_padding + (i * (window_size + window_padding))
    window_y = bus_y + window_padding
    pygame.draw.rect(screen, gray, (window_x, window_y, window_size, window_size))

# Draw the wheels
wheel_radius = 20
wheel1_x, wheel1_y = bus_x + 50, bus_y + bus_height
wheel2_x, wheel2_y = bus_x + bus_width - 50, bus_y + bus_height
pygame.draw.circle(screen, black, (wheel1_x, wheel1_y), wheel_radius)
pygame.draw.circle(screen, black, (wheel2_x, wheel2_y), wheel_radius)

# Update the display
pygame.display.flip()

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


















# Clean up
pygame.quit()
sys.exit()

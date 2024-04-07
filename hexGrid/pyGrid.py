import pygame
import math

# Constants for hexagon grid
GRID_WIDTH = 10
GRID_HEIGHT = 10
RADIUS_BIG = 40
RADIUS_SMALL = 20

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (150, 150, 150)

# Initialize Pygame
pygame.init()

# Set up the display
WINDOW_SIZE = (800, 600)
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Hexagon Grid Example")

# Function to calculate hexagon size dynamically based on the extent
def calculate_hex_size(extent):
    width, height = extent[2] - extent[0], extent[3] - extent[1]
    hex_width_big = width / (GRID_WIDTH + 0.5)
    hex_height_big = 2 * hex_width_big / math.sqrt(3)
    hex_width_small = hex_width_big * (RADIUS_SMALL / RADIUS_BIG)
    hex_height_small = 2 * hex_width_small / math.sqrt(3)
    return hex_width_big, hex_height_big, hex_width_small, hex_height_small

# Function to draw a single hexagon
def draw_hexagon(x, y, size):
    points = []
    for i in range(6):
        angle_deg = 60 * i
        angle_rad = math.radians(angle_deg)
        points.append((x + size * math.cos(angle_rad),
                       y + size * math.sin(angle_rad)))
    pygame.draw.polygon(screen, GRAY, points, 1)

# Function to draw the hexagon grid
def draw_grid(extent):
    hex_width_big, hex_height_big, hex_width_small, hex_height_small = calculate_hex_size(extent)
    for row in range(GRID_HEIGHT):
        for col in range(GRID_WIDTH):
            x = col * hex_width_big * 0.75
            y = row * hex_height_big + (col % 2) * (hex_height_big / 2)
            if row % 2 == 0 and col % 2 == 0:
                draw_hexagon(x, y, hex_width_big / 2)
            else:
                draw_hexagon(x, y, hex_width_small / 2)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill(WHITE)
    draw_grid([50, 50, 750, 550])  # Example extent (bounds)
    pygame.display.flip()

pygame.quit()

import pygame
import sys
from tileGui import Tile

pygame.init()

WIDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Monopoly Board - Object Oriented")
clock = pygame.time.Clock()

WHITE = (240, 240, 240)
BLACK = (0, 0, 0)
RED = (200, 50, 50)
BLUE = (50, 50, 200)
GREEN = (50, 200, 50)

BOARD_MARGIN = 80
TILE_SIZE = (WIDTH - 2 * BOARD_MARGIN) // 9

# Create board as a list of Tile objects
tiles = []

# Bottom row
for i in range(9):
    tiles.append(Tile(
        WIDTH - BOARD_MARGIN - (i + 1) * TILE_SIZE,
        HEIGHT - BOARD_MARGIN,
        TILE_SIZE,
        name=f"Tile {i}"
    ))

# Left column
for i in range(1,10):
    tiles.append(Tile(
        BOARD_MARGIN,
        HEIGHT - BOARD_MARGIN - i * TILE_SIZE,
        TILE_SIZE,
        name=f"Tile {len(tiles)}"
    ))

# Top row
for i in range(1,10):
    tiles.append(Tile(
        BOARD_MARGIN + i * TILE_SIZE,
        BOARD_MARGIN,
        TILE_SIZE,
        name=f"Tile {len(tiles)}"
    ))

# Right column
for i in range(1,10):
    tiles.append(Tile(
        WIDTH - BOARD_MARGIN,
        BOARD_MARGIN + i * TILE_SIZE,
        TILE_SIZE,
        name=f"Tile {len(tiles)}"
    ))

# Example players
players = [
    {"color": RED, "name": "Player 1"},
    {"color": BLUE, "name": "Player 2"},
    {"color": GREEN, "name": "Player 3"},
]

# Add players to tiles
tiles[0].add_player(players[0])
tiles[0].add_player(players[1])
tiles[5].add_player(players[2])

running = True
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(WHITE)

    # Draw board outline
    pygame.draw.rect(
        screen, BLACK,
        (BOARD_MARGIN, BOARD_MARGIN,
         WIDTH - 2 * BOARD_MARGIN,
         HEIGHT - 2 * BOARD_MARGIN),
        4
    )

    # Draw all tiles
    for tile in tiles:
        tile.draw(screen)

    pygame.display.flip()

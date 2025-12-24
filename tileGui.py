import pygame

class Tile:
    def __init__(self, x, y, size, name="", tile_type="normal"):
        self.rect = pygame.Rect(x, y, size, size)
        self.name = name
        self.type = tile_type
        self.players = []  # List of players on this tile

    def tile_slots(self):
        """Calculate positions for players on this tile."""
        x, y, w, h = self.rect
        offset = w // 4
        return [
            (x + offset, y + offset),
            (x + w - offset, y + offset),
            (x + offset, y + h - offset),
            (x + w - offset, y + h - offset),
            (x + w // 2, y + h // 2),
        ]

    def add_player(self, player):
        """Add a player to this tile."""
        self.players.append(player)

    def remove_player(self, player):
        """Remove a player from this tile."""
        if player in self.players:
            self.players.remove(player)

    def draw(self, screen):
        """Draw the tile and any players on it."""
        pygame.draw.rect(screen, (0, 0, 0), self.rect, 2)
        slots = self.tile_slots()
        for i, p in enumerate(self.players):
            slot = i % len(slots)  # Avoid overflow if more than 5 players
            pygame.draw.circle(screen, p["color"], slots[slot], 10)

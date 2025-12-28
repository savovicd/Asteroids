import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # must override
        pass

    def update(self, dt):
        # must overridebootdev run 482925e6-e043-43a4-b9c6-9eda414bb9a7
        pass

    def collides_with(self, other):
        distance = self.position.distance_to(other.position)
        length_of_r = self.radius + other.radius
        return distance <= length_of_r

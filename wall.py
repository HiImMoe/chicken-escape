import pygame
import random

from vars import SCREEN_WIDTH

class Wall(pygame.sprite.Sprite):
    def __init__(self, width, height):
        super().__init__()

        self.layer = 1

        self.image = pygame.Surface([width, height])
        self.image.fill('GRAY')

        self.rect = self.image.get_rect()
    
    def moveUp(self, dt, move_speed):
        self.rect.y -= move_speed * dt

class WallLine(pygame.sprite.Group):
    def __init__(self, y):
        super().__init__()
        wall_height = 20

        hole_min_width = 100 + 10
        hole_max_width = 100 + 100
        hole_min_distance = 20
        number_of_holes = random.randint(1,3)
        number_of_walls = number_of_holes + 1

        holes = []
        for i in range(number_of_holes):
            holes.append(random.randint(hole_min_width, hole_max_width))

        holes_rest_width = sum(holes)
        next_wall_start = 0


        for i in range(number_of_walls):
            max_wall_width = SCREEN_WIDTH - holes_rest_width
            wall_width = random.randint(50, max_wall_width)

            wall = Wall(wall_width, wall_height)
            wall.rect.x = next_wall_start
            wall.rect.y = y
            if i < number_of_holes:
                next_wall_start = next_wall_start + wall_width + holes[i]
                holes_rest_width = holes_rest_width - holes[i]
            self.add(wall)
        

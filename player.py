import pygame
from AnimatedSprite import AnimatedSprite

from vars import SCREEN_WIDTH

class Player(AnimatedSprite):
    def __init__(self, position, images):

        size = (45, 90)

        super().__init__(position, images, size)

    def moveRight(self, game_speed, dt, collisions):
        if not "Right" in collisions and self.rect.x + self.rect.width < SCREEN_WIDTH:
            self.rect.x += game_speed * dt

    def moveLeft(self, game_speed, dt, collisions):
        if not "Left" in collisions and self.rect.x > 0:
            self.rect.x -= game_speed * dt

    def moveUp(self, game_speed, dt, collisions):
        if not "Top" in collisions:
            self.rect.y -= game_speed * dt
        else:
            self.rect.y += game_speed * dt

    def moveDown(self, game_speed, dt, collisions):
        if not "Bottom" in collisions:
            self.rect.y += game_speed * dt
        else:
            self.rect.y -= game_speed * dt

    def bounceUp(self, game_speed, dt):
        self.rect.y -= game_speed * dt
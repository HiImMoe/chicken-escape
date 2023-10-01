from typing import Any
import pygame

from AnimatedSprite import AnimatedSprite

def rot_center(image, angle):
    """rotate an image while keeping its center and size"""
    orig_rect = image.get_rect()
    rot_image = pygame.transform.rotate(image, angle)
    rot_rect = orig_rect.copy()
    rot_rect.center = rot_image.get_rect().center
    rot_image = rot_image.subsurface(rot_rect).copy()
    return rot_image

class Saw(AnimatedSprite):
    def __init__(self, position, images):
        size = (64, 64)
        super().__init__(position, images, size)
        self.layer = 3

def create_saw_wall(images):
       group = pygame.sprite.Group()

       for i in range(20):
           saw = Saw(position=(i * 64, -32), images=images)
           group.add(saw)

       return group

       

        

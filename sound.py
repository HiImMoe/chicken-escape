import pygame

def play_game_over(shredder):
    pygame.mixer.Sound.play(shredder)

def stop_game_over(shredder):
    pygame.mixer.Sound.stop(shredder)

def play_speed(speed):
    pygame.mixer.Sound.play(speed)

def stop_speed(speed):
    pygame.mixer.Sound.stop(speed)
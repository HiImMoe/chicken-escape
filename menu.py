import pygame

from vars import SCREEN_HEIGHT, SCREEN_WIDTH

def draw_start_menu(screen):
    screen.fill((0, 0, 0))
    font = pygame.font.SysFont('arial', 40)
    title = font.render('Ludum Dare 54', True, (255, 255, 255))
    start_text = font.render('Press Return to Start', True, (255, 255, 255))
    screen.blit(title, (SCREEN_WIDTH/2 - title.get_width()/2, SCREEN_HEIGHT/2 - title.get_height()/2))
    screen.blit(start_text, (SCREEN_WIDTH/2 - start_text.get_width()/2, SCREEN_HEIGHT/2 + start_text.get_height()/2))
    pygame.display.update()

def draw_game_over_menu(screen, score):
    screen.fill((0, 0, 0))
    font = pygame.font.SysFont('arial', 40)
    score_text = font.render(str(score) + ' Points', True, (255, 255, 255))
    title = font.render('Game Over', True, (255, 255, 255))
    start_text = font.render('Press Return to Start again', True, (255, 255, 255))
    screen.blit(score_text, (SCREEN_WIDTH/2 - score_text.get_width()/2, SCREEN_HEIGHT/2 - score_text.get_height()/2 - title.get_height()))
    screen.blit(title, (SCREEN_WIDTH/2 - title.get_width()/2, SCREEN_HEIGHT/2 - title.get_height()/2))
    screen.blit(start_text, (SCREEN_WIDTH/2 - start_text.get_width()/2, SCREEN_HEIGHT/2 + start_text.get_height()/2))
    pygame.display.update()

import pygame
from AnimatedSprite import load_images
from menu import draw_game_over_menu, draw_start_menu
from particels import draw_particels
from player import Player
from saw_wall import create_saw_wall
from sound import play_game_over, play_speed, stop_game_over, stop_speed
from utils import checkCollision, moveWalls
from vars import PLAYER_WIDTH, SCREEN_HEIGHT, SCREEN_WIDTH
from wall import WallLine
import particlepy

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) 
pygame.display.set_caption("Chicken Escape")
clock = pygame.time.Clock()
running = True
dt = 0

INITIAL_GAME_SPEED = 250

game_speed = INITIAL_GAME_SPEED
wall_distance = 400
score = 0
game_state = "start_menu"
remaining_boosts = 3
boost_time = 0

game_over_animate_counter = 100
shredder = pygame.mixer.Sound('sound/shredder.wav')
speed = pygame.mixer.Sound('sound/speed.wav')
background_sound = pygame.mixer.music.load('sound/background.wav')
images_player = load_images(path='assets/player', size=(45 , 90))
images_saw = load_images(path="assets/saw", size=(64, 64))
player = Player(position=(SCREEN_WIDTH/2 - 20, 100), images=images_player)
saw_group = create_saw_wall(images=images_saw)

particle_system = particlepy.particle.ParticleSystem()

all_sprites_list = pygame.sprite.Group()
wall_line_group = pygame.sprite.Group()

wall_spawn_y = round(SCREEN_HEIGHT / wall_distance) * wall_distance + wall_distance * 5

background_image = pygame.transform.scale(pygame.image.load("assets/assembly-line.svg"), (SCREEN_WIDTH, SCREEN_HEIGHT + 10))
background_y = SCREEN_HEIGHT
scroll_y = 0

def reset_game():
    wall_line_group.empty()
    all_sprites_list.empty()
    player.rect.y = 200
    all_sprites_list.add(player)
    all_sprites_list.add(saw_group)
    pygame.mixer.music.play(-1,0,0)
    for i in range(round(wall_spawn_y / wall_distance) + 1):
        wallLine = WallLine(wall_distance * 2 + i * wall_distance)
        all_sprites_list.add(wallLine)
        wall_line_group.add(wallLine)  


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

   
    keys = pygame.key.get_pressed()
    if game_state == "start_menu":
        draw_start_menu(screen)
        if keys[pygame.K_RETURN]:
           reset_game()
           game_state = "game"
    
    if game_state == "game_over":
        draw_game_over_menu(screen, score)
        if keys[pygame.K_RETURN]:
           reset_game()
           score = 0
           remaining_boosts = 3
           game_over_animate_counter = 100
           game_speed = INITIAL_GAME_SPEED
           game_state = "game"
        
    if game_state == "game" or game_state == "game_over_animate":

        wall_move_speed = game_speed * 0.8

        all_sprites_list.update(dt)
        screen.fill("black")
        
        screen.blit(background_image, (0, scroll_y))
        screen.blit(background_image, (0, background_y))
        if (game_state != "game_over_animate"):
            scroll_y -= dt * wall_move_speed
            background_y -= dt * wall_move_speed

            if scroll_y <= -SCREEN_HEIGHT:
                scroll_y = SCREEN_HEIGHT + 10
            
            if background_y <= -SCREEN_HEIGHT:
                background_y = SCREEN_HEIGHT + 10

            wall_killed = moveWalls(wall_line_group, dt, wall_move_speed)
            if wall_killed:
                wallLine = WallLine(wall_spawn_y)
                all_sprites_list.add(wallLine)
                wall_line_group.add(wallLine)

            # player collision
            collisions = checkCollision(player, wall_line_group)
            if player.rect.y < 0:
                play_game_over(shredder)
                pygame.mixer.music.stop()
                game_state = "game_over_animate"

            if "Bottom" in collisions:
                player.bounceUp(game_speed, dt)

            # player movement
            player_speed = game_speed
            if boost_time > 0:
                player_speed = game_speed + 300

            if keys[pygame.K_a]:
                player.moveLeft(player_speed, dt, collisions)
            if keys[pygame.K_d]:
                player.moveRight(player_speed, dt, collisions)
            if keys[pygame.K_w]:
                player.moveUp(player_speed, dt, collisions)
            if keys[pygame.K_s]:
                player.moveDown(player_speed, dt, collisions) 
            if keys[pygame.K_SPACE] and remaining_boosts > 0 and boost_time <= 0:
                boost_time = 300
                play_speed(speed)
                remaining_boosts -= 1

            # score
            score += 1   
 
        all_sprites_list.draw(screen)

        if game_over_animate_counter > 0 and game_state == "game_over_animate":
            draw_particels(particle_system, dt, player.rect.x + player.rect.width / 2)
            particle_system.render(surface=screen)
            game_over_animate_counter -= 1
        
        if game_over_animate_counter <= 0:
            stop_game_over(shredder)
            game_state = "game_over"

        if boost_time > 0:
            boost_time -= 1
        elif boost_time <= 0:
            stop_speed(speed)
        
        font = pygame.font.SysFont('arial', 40)
        boost_text = font.render('Boosts ' + str(remaining_boosts), True, (255, 255, 255))
        screen.blit(boost_text, (32, 50))
        score_text = font.render('Score ' + str(score), True, (255, 255, 255))
        screen.blit(score_text, (SCREEN_WIDTH - score_text.get_width(), 50))

        if score % 100 == 0:
            game_speed += 10

    pygame.display.flip()
    dt = clock.tick(60) / 1000

pygame.quit()
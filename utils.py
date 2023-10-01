import pygame

def checkCollision(player, wall_line):
    collision_sides = []
    player_left = player.rect.x
    player_top = player.rect.y
    player_right = player.rect.x + player.rect.width
    player_bottom = player.rect.y + player.rect.height
    collision = pygame.sprite.spritecollide(player, wall_line, False)
    if collision:
        for sprite in collision:
            sprite_top = sprite.rect.y
            sprite_left = sprite.rect.x
            sprite_bottom = sprite.rect.y + sprite.rect.height
            sprite_right = sprite.rect.x + sprite.rect.width

            # collision top
            if player_top <= sprite_bottom and player_top >= sprite_bottom - 30:
                collision_sides.append("Top")

            # collision bottom
            if player_bottom >= sprite_top and player_bottom <= sprite_top + 50:
                collision_sides.append("Bottom")
    
            # collision right
            if player_right >= sprite_left and player_right <= sprite_left + 5:
                collision_sides.append("Right")

            # collision left
            if player_left <= sprite_right and player_left >= sprite_right - 5:
                collision_sides.append("Left")

    return collision_sides

def moveWalls(walls, dt, wall_move_speed):
    wall_killed = False
    for wall in walls:
        if (wall.rect.y < -200):
            wall.kill()
            wall_killed = True
        wall.moveUp(dt, wall_move_speed)
    return wall_killed
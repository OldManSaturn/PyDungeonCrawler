import pygame
from player import Player
import spritesheets

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BLACK = (0,0,0)
BACKGROUND = (50,50,50)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Dalton's Dungeon Crawling")

# framerate
clock = pygame.time.Clock()
FPS = 60

# Setup the sprites and animations for the player (currently only the fighter sprite is functional)

# Idle fighter sprite
fighter_idle_spritesheet_file_loaded = pygame.image.load("assets/images/fighter_player_idle.png").convert_alpha()
fighter_idle_sprite_sheet = spritesheets.Spritesheet(fighter_idle_spritesheet_file_loaded)
# Walking fighter sprite
fighter_walk_spritesheet_file_loaded = pygame.image.load("assets/images/fighter_player_walk.png").convert_alpha()
fighter_walk_sprite_sheet = spritesheets.Spritesheet(fighter_walk_spritesheet_file_loaded)

# create animation list for fighter sprite at idle
fighter_idle_animation_list = []
fighter_idle_animation_steps = 5
# create animation list for fighter at walking
fighter_walk_animation_list = []
fighter_walk_animation_steps = 8

# idle animation variables
fighter_idle_animation_cooldown = 100
fighter_idle_animation_frame = 0
# fighter walking animation variables
fighter_walk_animation_cooldown = 100
fighter_walk_animation_frame = 0

last_update = pygame.time.get_ticks()

for x in range(fighter_idle_animation_steps):
    frame = fighter_idle_sprite_sheet.get_image(x, 128, 128, 1, BLACK)
    fighter_idle_animation_list.append(frame)

for x in range(fighter_walk_animation_steps):
    walk_frame = fighter_walk_sprite_sheet.get_image(x, 128, 128, 1, BLACK)
    fighter_walk_animation_list.append(walk_frame)

running = True
while running:
    clock.tick(FPS)

    # background update
    screen.fill(BACKGROUND)

    # Update idle player animation
    now = pygame.time.get_ticks()
    if now - last_update >= fighter_idle_animation_cooldown:
        last_update = now
        fighter_idle_animation_frame += 1
        fighter_walk_animation_frame += 1
        if fighter_idle_animation_frame >= len(fighter_idle_animation_list):
            fighter_idle_animation_frame = 0
        if fighter_walk_animation_frame >= len(fighter_walk_animation_list):
            fighter_walk_animation_frame = 0
        

    # show frame image
    screen.blit(fighter_idle_animation_list[fighter_idle_animation_frame], (0,0))
    screen.blit(fighter_walk_animation_list[fighter_walk_animation_frame], (128,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()
pygame.quit()
import pygame
from player import Player
import spritesheets

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BLACK = (0, 0, 0)
BACKGROUND = (50, 50, 50)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Dalton's Dungeon Crawling")

# Framerate
clock = pygame.time.Clock()
FPS = 60

# Idle fighter sprite
fighter_idle_spritesheet_file_loaded = pygame.image.load("assets/images/fighter_player_idle.png").convert_alpha()
fighter_idle_sprite_sheet = spritesheets.Spritesheet(fighter_idle_spritesheet_file_loaded)
# Walking fighter sprite
fighter_walk_spritesheet_file_loaded = pygame.image.load("assets/images/fighter_player_walk.png").convert_alpha()
fighter_walk_sprite_sheet = spritesheets.Spritesheet(fighter_walk_spritesheet_file_loaded)

# Create animation list for fighter sprite at idle
fighter_idle_animation_list = []
fighter_idle_animation_steps = 5
# Create animation list for fighter at walking
fighter_walk_animation_list = []
fighter_walk_animation_steps = 8

# Idle animation variables
fighter_idle_animation_cooldown = 100
fighter_idle_animation_frame = 0
# Fighter walking animation variables
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
moving = False
direction = "right"

# Starting position at the bottom left of the window
player_x = 0
player_y = SCREEN_HEIGHT - 128  # Assuming sprite height is 128 pixels

while running:
    clock.tick(FPS)

    # Background update
    screen.fill(BACKGROUND)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] or keys[pygame.K_RIGHT]:
        moving = True
        if keys[pygame.K_LEFT]:
            player_x -= 5  # Move left
            direction = "left"
        if keys[pygame.K_RIGHT]:
            player_x += 5  # Move right
            direction = "right"
    else:
        moving = False

    # Update animation
    now = pygame.time.get_ticks()
    if moving:
        if now - last_update >= fighter_walk_animation_cooldown:
            last_update = now
            fighter_walk_animation_frame += 1
            if fighter_walk_animation_frame >= len(fighter_walk_animation_list):
                fighter_walk_animation_frame = 0
        frame = fighter_walk_animation_list[fighter_walk_animation_frame].convert_alpha()
    else:
        if now - last_update >= fighter_idle_animation_cooldown:
            last_update = now
            fighter_idle_animation_frame += 1
            if fighter_idle_animation_frame >= len(fighter_idle_animation_list):
                fighter_idle_animation_frame = 0
        frame = fighter_idle_animation_list[fighter_idle_animation_frame].convert_alpha()

    # Flip the frame if moving left
    if direction == "left":
        frame = pygame.transform.flip(frame, True, False)

    screen.blit(frame, (player_x, player_y))
    pygame.display.update()

pygame.quit()

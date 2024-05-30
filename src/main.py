import pygame
from spritesheets import SpriteSheet, Animation

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

# Load spritesheets
fighter_idle_spritesheet_file_loaded = pygame.image.load("assets/images/fighter_player_idle.png").convert_alpha()
fighter_walk_spritesheet_file_loaded = pygame.image.load("assets/images/fighter_player_walk.png").convert_alpha()

fighter_idle_sprite_sheet = SpriteSheet(fighter_idle_spritesheet_file_loaded)
fighter_walk_sprite_sheet = SpriteSheet(fighter_walk_spritesheet_file_loaded)

# Create animations
fighter_idle_animation = Animation(fighter_idle_sprite_sheet, 5, 128, 1, BLACK)
fighter_walk_animation = Animation(fighter_walk_sprite_sheet, 8, 128, 1, BLACK)

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

    # Get the current frame based on movement
    if moving:
        frame = fighter_walk_animation.get_current_frame(100).convert_alpha()
    else:
        frame = fighter_idle_animation.get_current_frame(100).convert_alpha()

    # Flip the frame if moving left
    if direction == "left":
        frame = pygame.transform.flip(frame, True, False)

    screen.blit(frame, (player_x, player_y))

    pygame.display.update()

pygame.quit()

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
fighter_run_spritesheet_file_loaded = pygame.image.load("assets/images/fighter_player_run.png").convert_alpha()
fighter_jump_spritesheet_file_loaded = pygame.image.load("assets/images/fighter_player_jump.png").convert_alpha()
fighter_attack1_spritesheet_file_loaded = pygame.image.load("assets/images/fighter_player_attack1.png").convert_alpha()
fighter_attack2_spritesheet_file_loaded = pygame.image.load("assets/images/fighter_player_attack2.png").convert_alpha()
fighter_attack3_spritesheet_file_loaded = pygame.image.load("assets/images/fighter_player_attack3.png").convert_alpha()
fighter_block_spritesheet_file_loaded = pygame.image.load("assets/images/fighter_player_block.png").convert_alpha()  # Blocking spritesheet

fighter_idle_sprite_sheet = SpriteSheet(fighter_idle_spritesheet_file_loaded)
fighter_walk_sprite_sheet = SpriteSheet(fighter_walk_spritesheet_file_loaded)
fighter_run_sprite_sheet = SpriteSheet(fighter_run_spritesheet_file_loaded)
fighter_jump_sprite_sheet = SpriteSheet(fighter_jump_spritesheet_file_loaded)
fighter_attack1_sprite_sheet = SpriteSheet(fighter_attack1_spritesheet_file_loaded)
fighter_attack2_sprite_sheet = SpriteSheet(fighter_attack2_spritesheet_file_loaded)
fighter_attack3_sprite_sheet = SpriteSheet(fighter_attack3_spritesheet_file_loaded)
fighter_block_sprite_sheet = SpriteSheet(fighter_block_spritesheet_file_loaded)  # Blocking sprite sheet

# Create animations
fighter_idle_animation = Animation(fighter_idle_sprite_sheet, 5, 128, 1, BLACK)
fighter_walk_animation = Animation(fighter_walk_sprite_sheet, 8, 128, 1, BLACK)
fighter_run_animation = Animation(fighter_run_sprite_sheet, 8, 128, 1, BLACK)
fighter_jump_animation = Animation(fighter_jump_sprite_sheet, 10, 128, 1, BLACK)
fighter_attack1_animation = Animation(fighter_attack1_sprite_sheet, 4, 128, 1, BLACK)
fighter_attack2_animation = Animation(fighter_attack2_sprite_sheet, 3, 128, 1, BLACK)
fighter_attack3_animation = Animation(fighter_attack3_sprite_sheet, 4, 128, 1, BLACK)
fighter_block_animation = Animation(fighter_block_sprite_sheet, 2, 128, 1, BLACK)  # Blocking animation

running = True
moving = False
direction = "right"
jumping = False
attacking = False
blocking = False  # Blocking state
current_attack = None
jump_speed = 15
gravity = 1.5
velocity_y = 0

# Starting position at the bottom left of the window
player_x = 0
player_y = SCREEN_HEIGHT - 128  # Assuming sprite height is 128 pixels
ground_y = player_y

while running:
    clock.tick(FPS)

    # Background update
    screen.fill(BACKGROUND)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not jumping:
                jumping = True
                velocity_y = -jump_speed
            if not attacking:
                if event.key == pygame.K_1:
                    attacking = True
                    current_attack = fighter_attack1_animation
                    current_attack.reset()
                elif event.key == pygame.K_2:
                    attacking = True
                    current_attack = fighter_attack2_animation
                    current_attack.reset()
                elif event.key == pygame.K_3:
                    attacking = True
                    current_attack = fighter_attack3_animation
                    current_attack.reset()
            if event.key == pygame.K_LALT or event.key == pygame.K_RALT:
                blocking = True
                fighter_block_animation.reset()  # Start blocking animation
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LALT or event.key == pygame.K_RALT:
                blocking = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] or keys[pygame.K_RIGHT]:
        moving = True
        if blocking:
            speed = 2.5  # 1/2 walking speed while blocking
        elif keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]:
            speed = 10  # Increased speed when running
        else:
            speed = 5
        if keys[pygame.K_LEFT]:
            player_x -= speed  # Move left
            direction = "left"
        if keys[pygame.K_RIGHT]:
            player_x += speed  # Move right
            direction = "right"
    else:
        moving = False

    # Jumping logic
    if jumping:
        player_y += velocity_y
        velocity_y += gravity
        if player_y >= ground_y:
            player_y = ground_y
            jumping = False
            velocity_y = 0

    # Get the current frame based on movement, jumping, attacking, and blocking
    if blocking:
        frame = fighter_block_animation.get_current_frame(100).convert_alpha()
        if fighter_block_animation.frame_index == len(fighter_block_animation.animation_list) - 1:
            fighter_block_animation.frame_index = 1  # Hold the second frame
    elif attacking:
        frame = current_attack.get_current_frame(100)
        if current_attack.frame_index == len(current_attack.animation_list) - 1:
            attacking = False
            current_attack = None
    elif jumping:
        frame = fighter_jump_animation.get_current_frame(100).convert_alpha()
    elif moving:
        if keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]:
            frame = fighter_run_animation.get_current_frame(100).convert_alpha()
        else:
            frame = fighter_walk_animation.get_current_frame(100).convert_alpha()
    else:
        frame = fighter_idle_animation.get_current_frame(100).convert_alpha()

    # Flip the frame if moving left
    if direction == "left":
        frame = pygame.transform.flip(frame.convert_alpha(), True, False)

    screen.blit(frame, (player_x, player_y))

    pygame.display.update()

pygame.quit()

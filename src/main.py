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

# Function to load sprite sheets
def load_sprite_sheet(file_name):
    return pygame.image.load(file_name).convert_alpha()

# Load all sprite sheets
sprite_sheet_files = {
    "idle": "assets/images/fighter_player_idle.png",
    "walk": "assets/images/fighter_player_walk.png",
    "run": "assets/images/fighter_player_run.png",
    "jump": "assets/images/fighter_player_jump.png",
    "attack1": "assets/images/fighter_player_attack1.png",
    "attack2": "assets/images/fighter_player_attack2.png",
    "attack3": "assets/images/fighter_player_attack3.png",
    "block": "assets/images/fighter_player_block.png"
}

sprite_sheets = {name: SpriteSheet(load_sprite_sheet(file)) for name, file in sprite_sheet_files.items()}

# Create animations
animations = {
    "idle": Animation(sprite_sheets["idle"], 5, 128, 1, BLACK),
    "walk": Animation(sprite_sheets["walk"], 8, 128, 1, BLACK),
    "run": Animation(sprite_sheets["run"], 8, 128, 1, BLACK),
    "jump": Animation(sprite_sheets["jump"], 10, 128, 1, BLACK),
    "attack1": Animation(sprite_sheets["attack1"], 4, 128, 1, BLACK),
    "attack2": Animation(sprite_sheets["attack2"], 3, 128, 1, BLACK),
    "attack3": Animation(sprite_sheets["attack3"], 4, 128, 1, BLACK),
    "block": Animation(sprite_sheets["block"], 2, 128, 1, BLACK)
}

running = True
moving = False
direction = "right"
jumping = False
attacking = False
blocking = False
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
                    current_attack = animations["attack1"]
                    current_attack.reset()
                elif event.key == pygame.K_2:
                    attacking = True
                    current_attack = animations["attack2"]
                    current_attack.reset()
                elif event.key == pygame.K_3:
                    attacking = True
                    current_attack = animations["attack3"]
                    current_attack.reset()
            if event.key == pygame.K_LALT or event.key == pygame.K_RALT:
                blocking = True
                animations["block"].reset()  # Start blocking animation
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
        frame = animations["block"].get_current_frame(100).convert_alpha()
        if animations["block"].frame_index == len(animations["block"].animation_list) - 1:
            animations["block"].frame_index = 1  # Hold the second frame
    elif attacking:
        frame = current_attack.get_current_frame(100)
        if current_attack.frame_index == len(current_attack.animation_list) - 1:
            attacking = False
            current_attack = None
    elif jumping:
        frame = animations["jump"].get_current_frame(100).convert_alpha()
    elif moving:
        if keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]:
            frame = animations["run"].get_current_frame(100).convert_alpha()
        else:
            frame = animations["walk"].get_current_frame(100).convert_alpha()
    else:
        frame = animations["idle"].get_current_frame(100).convert_alpha()

    # Flip the frame if moving left
    if direction == "left":
        frame = pygame.transform.flip(frame.convert_alpha(), True, False)

    screen.blit(frame, (player_x, player_y))

    pygame.display.update()

pygame.quit()

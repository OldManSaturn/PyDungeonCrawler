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

#player = pygame.Rect((300,250,50,50))
#player = Player("crimson", 500, 300)

# create sprite group
#players = pygame.sprite.Group()
#players.add(player)

fighter_idle_spritesheet_file = pygame.image.load("assets/images/fighter_player_idle.png").convert_alpha()
fighter_sprite_sheet = spritesheets.Spritesheet(fighter_idle_spritesheet_file)

# create animation list for fighter sprite at idle
fighter_idle_animation_list = []
fighter_idle_animation_steps = 5

last_update = pygame.time.get_ticks()
fighter_idle_animation_cooldown = 100
fighter_idle_animation_frame = 0

for x in range(fighter_idle_animation_steps):
    frame = fighter_sprite_sheet.get_image(x, 128, 128, 1, BLACK)
    fighter_idle_animation_list.append(frame)

running = True
while running:
    clock.tick(FPS)

    # background update
    screen.fill(BACKGROUND)

    # Update player animation
    now = pygame.time.get_ticks()
    if now - last_update >= fighter_idle_animation_cooldown:
        last_update = now
        fighter_idle_animation_frame += 1
        if fighter_idle_animation_frame >= len(fighter_idle_animation_list):
            fighter_idle_animation_frame = 0
        

    # show frame image
    screen.blit(fighter_idle_animation_list[fighter_idle_animation_frame], (0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()
pygame.quit()
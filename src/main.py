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

running = True
fighter_idle_spritesheet_file = pygame.image.load("assets/images/fighter_player_idle.png").convert_alpha()
fighter_sprite_sheet = spritesheets.Spritesheet(fighter_idle_spritesheet_file)


frame_0 = fighter_sprite_sheet.get_image(0, 128, 128, 1, BLACK)
frame_1 = fighter_sprite_sheet.get_image(1, 128, 128, 1, BLACK)
frame_2 = fighter_sprite_sheet.get_image(2, 128, 128, 1, BLACK)
frame_3 = fighter_sprite_sheet.get_image(3, 128, 128, 1, BLACK)
frame_4 = fighter_sprite_sheet.get_image(4, 128, 128, 1, BLACK)
frame_5 = fighter_sprite_sheet.get_image(5, 128, 128, 1, BLACK)

while running:
    clock.tick(FPS)

    # background update
    screen.fill(BACKGROUND)

    # show frame image
    screen.blit(frame_0, (0,0))
    screen.blit(frame_1, (100,0))
    screen.blit(frame_2, (200,0))
    screen.blit(frame_3, (300,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()
pygame.quit()
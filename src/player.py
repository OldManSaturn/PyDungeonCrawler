import pygame

#fighter_idle_spritesheet = pygame.image.load("assets/images/fighter_player_idle.png").convert_alpha()

class Player(pygame.sprite.Sprite):
    def __init__(self, col, x, y):
        pygame.sprite.Sprite.__init__(self) 
        self.image = pygame.Surface((50,50))
        self.image.fill(col)
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)


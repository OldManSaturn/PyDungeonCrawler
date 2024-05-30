import pygame

class SpriteSheet:
    def __init__(self, image):
        self.sheet = image

    def get_image(self, frame, width, height, scale, color):
        image = pygame.Surface((width, height)).convert_alpha()
        image.blit(self.sheet, (0, 0), ((frame * width), 0, width, height))
        image = pygame.transform.scale(image, (width * scale, height * scale))
        image.set_colorkey(color)
        return image

class Animation:
    def __init__(self, spritesheet, animation_steps, image_size, scale, color):
        self.spritesheet = spritesheet
        self.animation_list = []
        self.animation_steps = animation_steps
        self.image_size = image_size
        self.scale = scale
        self.color = color
        self.load_images()
        self.frame_index = 0
        self.last_update = pygame.time.get_ticks()

    def load_images(self):
        for x in range(self.animation_steps):
            image = self.spritesheet.get_image(x, self.image_size, self.image_size, self.scale, self.color)
            self.animation_list.append(image)

    def get_current_frame(self, cooldown):
        now = pygame.time.get_ticks()
        if now - self.last_update >= cooldown:
            self.last_update = now
            self.frame_index += 1
            if self.frame_index >= len(self.animation_list):
                self.frame_index = 0
        return self.animation_list[self.frame_index]

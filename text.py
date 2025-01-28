import pygame

class Text(pygame.sprite.Sprite):
    def __init__(self, x, y, initial):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.font = pygame.font.SysFont(None, 30)
        self.set_text(initial)
        self.position = (x, y)

    
    def draw(self, screen):
        screen.blit(self.image, self.position)

    def set_text(self, text):
        self.__text = text
        self.image = self.font.render(self.__text, True, "white")
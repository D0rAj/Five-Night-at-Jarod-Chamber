import pygame.image
import game


class Monster(game.Game):

    def __init__(self):
        super().__init__()
        self.cooldown = 0
        self.cadavre = pygame.image.load('assets/CADAVRE.jpg')
        self.cadavre = pygame.transform.scale(self.cadavre, (500, 400))
        self.is_atdoor = False
        self.is_atbed = False

    def update_monster(self, screen):
        if self.at_door and self.is_atdoor:
            screen.blit(self.cadavre, (0, 0))

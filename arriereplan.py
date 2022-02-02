import pygame
import animation
# Arriere plan


class ArrierePlan(animation.AnimateSprite):

    def __init__(self):
        super().__init__('chambre')
        self.image = pygame.image.load('assets/chambre.png')
        self.rect = self.image.get_rect()
        self.velocity = 15
        self.fap = pygame.mixer.Sound('assets/fap.wav')
        self.rect.y = 0
        self.rect.x = 0
        self.horny_bar_width = 300
        self.horny_bar_max_width = 300
        self.is_playing = False

    def update(self, screen, sperme):
        screen.blit(self.image, self.rect)
        if not self.at_door:
            screen.blit(sperme, (0, 0))
        self.update_animation()
        self.update_horny_bar(screen)

    def update_horny_bar(self, surface):
        horny_bar_color = (255, 255, 255)
        back_horny_bar_color = (0, 0, 0)

        horny_bar_position = [250, 550, self.horny_bar_width, 25]
        back_horny_bar_position = [250, 550, self.horny_bar_max_width, 25]

        self.horny_bar_width -= 1
        if not self.at_door:
            if self.horny_bar_width > 300:
                self.horny_bar_width = 300
            if self.horny_bar_width <= 0:
                pygame.quit()
            pygame.draw.rect(surface, back_horny_bar_color, back_horny_bar_position)
            pygame.draw.rect(surface, horny_bar_color, horny_bar_position)

    def up_horny_bar(self):
        self.horny_bar_width += 20

    def update_animation(self):
        self.animate()

    def branlette_down(self):
        self.rect.y -= self.velocity
        self.up_horny_bar()
        self.fap.play()

    def branlette_up(self):
        self.rect.y += self.velocity

    def close_door(self):
        self.image = pygame.image.load('assets/chambre/chambre6.png')

    def open_door(self):
        self.image = pygame.image.load('assets/chambre/chambre7.png')

    def flashlight_on(self):
        self.image = pygame.image.load('assets/chambre/chambre8.png')

    def flashlight_off(self):
        self.image = pygame.image.load('assets/chambre/chambre7.png')

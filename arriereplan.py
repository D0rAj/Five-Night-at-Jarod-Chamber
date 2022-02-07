import pygame
import animation
# Arriere plan


class ArrierePlan(animation.AnimateSprite):

    def __init__(self):
        super().__init__('chambre', 'lit')
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
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if not self.at_door:
                        self.branlette_down()
                    elif self.at_door:
                        self.close_door()
                if event.key == pygame.K_LCTRL:
                    if self.at_door:
                        self.flashlight_on()
                if event.key == pygame.K_d:
                    self.start_animation('porte') #    j'avais peur que sa marche pas mais c bon
                if event.key == pygame.K_a:
                    self.start_animation('lit')   # oui oui c'est des commentaires, c'est pas pris en compte par le code
                    # justement je vais le faire
                    
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    if not self.at_door:
                        self.branlette_up()
                    elif self.at_door:
                        self.open_door()
                if event.key == pygame.K_LCTRL:
                    if self.at_door:
                        self.flashlight_off()

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

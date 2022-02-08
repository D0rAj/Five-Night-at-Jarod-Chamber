import pygame
import animation


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
        self.update_animation()
        self.update_horny_bar(screen, sperme)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if not self.at_door and not self.at_bed:
                        self.branlette_down()
                    elif self.at_door:
                        self.flashlight_on()
                    elif self.at_bed:
                        self.flashlight_on()
                if event.key == pygame.K_LCTRL:
                    if self.at_door:
                        self.close_door()
                if event.key == pygame.K_d:
                    if not self.at_door and not self.at_bed:
                        self.start_animation('porte')
                    elif self.at_bed:
                        self.start_animation('lit')
                if event.key == pygame.K_a:
                    if not self.at_bed and not self.at_door:
                        self.start_animation('lit')
                    elif self.at_door:
                        self.start_animation('porte')
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    if not self.at_door and not self.at_bed:
                        self.branlette_up()
                    elif self.at_door:
                        self.flashlight_off()
                    elif self.at_bed:
                        self.flashlight_off()
                if event.key == pygame.K_LCTRL:
                    if self.at_door:
                        self.open_door()

    def update_horny_bar(self, surface, sperme):
        horny_bar_color = (255, 255, 255)
        back_horny_bar_color = (0, 0, 0)

        horny_bar_position = [250, 550, self.horny_bar_width, 25]
        back_horny_bar_position = [250, 550, self.horny_bar_max_width, 25]

        self.horny_bar_width -= 1
        if not self.at_door and not self.at_bed:
            if self.horny_bar_width > 300:
                self.horny_bar_width = 300
            if self.horny_bar_width <= 0:
                pygame.quit()
            pygame.draw.rect(surface, back_horny_bar_color, back_horny_bar_position)
            pygame.draw.rect(surface, horny_bar_color, horny_bar_position)
            surface.blit(sperme, (0, 0))

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
        if self.at_door:
            self.image = pygame.image.load('assets/chambre/chambre8.png')
        elif self.at_bed:
            self.image = pygame.image.load('assets/lit/lit5.png')

    def flashlight_off(self):
        if self.at_door:
            self.image = pygame.image.load('assets/chambre/chambre7.png')
        elif self.at_bed:
            self.image = pygame.image.load('assets/lit/lit4.png')

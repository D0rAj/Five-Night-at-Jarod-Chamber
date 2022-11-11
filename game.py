import pygame
import animation


class Game(animation.AnimateSprite):

    def __init__(self):
        super().__init__('chambre', 'lit')
        self.image = pygame.image.load('assets/chambre.png')
        self.goute_do = pygame.image.load('assets/goutte_do.png')
        self.rect = self.image.get_rect()
        self.velocity = 15
        self.fap = pygame.mixer.Sound('sound/fap.wav')
        self.rect.y = 0
        self.rect.x = 0
        self.horny_bar_width = 300
        self.horny_bar_max_width = 300
        self.is_playing = False
        self.running = True
        self.hour = 0
        self.size = 50
        self.sleep = 0
        self.cooldown = 280
        self.cadavre = pygame.image.load('assets/CADAVRE.jpg')
        self.cadavre = pygame.transform.scale(self.cadavre, (500, 400))
        self.is_atdoor = False
        self.is_atbed = False
        self.screamer = False
        self.scream = pygame.mixer.Sound('sound/screamer_prout.mp3')
        self.screamtime = self.scream.get_length() * 7
        self.screamed = False
        self.paused = False

    def update(self, screen):
        if self.paused:
            self.pause()
        elif self.screamer:
            self.death_monster(screen)
        else:
            screen.blit(self.image, self.rect)
            self.update_animation()
            self.update_horny_bar(screen, self.goute_do)
            self.update_time(screen)
            self.update_monster(screen)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
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
                    if event.key == pygame.K_ESCAPE:
                        self.is_playing = False
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

    def update_horny_bar(self, surface, goute_do):
        horny_bar_color = (255, 255, 255)
        back_horny_bar_color = (0, 0, 0)

        horny_bar_position = [250, 550, self.horny_bar_width, 25]
        back_horny_bar_position = [250, 550, self.horny_bar_max_width, 25]

        self.horny_bar_width -= .5
        if not self.at_door and not self.at_bed:
            if self.horny_bar_width > 300:
                self.horny_bar_width = 300
            if self.horny_bar_width <= 0:
                self.is_playing = False
            pygame.draw.rect(surface, back_horny_bar_color, back_horny_bar_position)
            pygame.draw.rect(surface, horny_bar_color, horny_bar_position)
            surface.blit(goute_do, (0, 0))

    def update_time(self, screen):
        self.go_time()
        self.write_time(screen)

    def update_animation(self):
        self.animate()

    def update_monster(self, screen):
        if self.cooldown > 0:
            self.cooldown -= 1
        else:
            self.is_atdoor = True
            self.cooldown = 840

    def up_horny_bar(self):
        self.horny_bar_width += 20

    def branlette_down(self):
        self.rect.y += self.velocity
        self.up_horny_bar()
        self.fap.play()

    def branlette_up(self):
        self.rect.y -= self.velocity

    def close_door(self):
        self.image = pygame.image.load('assets/chambre/chambre6.png')

    def open_door(self):
        self.image = pygame.image.load('assets/chambre/chambre7.png')

    def flashlight_on(self):
        if self.at_door:
            if not self.is_atdoor:
                self.image = pygame.image.load('assets/chambre/chambre8.png')
            else:
                self.screamer = True
        elif self.at_bed:
            self.image = pygame.image.load('assets/lit/lit5.png')

    def flashlight_off(self):
        if self.at_door:
            self.image = pygame.image.load('assets/chambre/chambre7.png')
        elif self.at_bed:
            self.image = pygame.image.load('assets/lit/lit4.png')

    def go_time(self):
        if self.hour < 720 and self.sleep > 7:
            self.hour += 1
            self.sleep = 0
        else:
            self.sleep += 1

    def what_hour(self):
        hour = self.hour / 90
        if hour > 7:
            return 6
        elif hour > 6:
            return 5
        elif hour > 5:
            return 4
        elif hour > 4:
            return 3
        elif hour > 3:
            return 2
        elif hour > 2:
            return 1
        elif hour > 1:
            return 0
        elif hour < 1:
            return 12

    def write_time(self, screen):
        if self.what_hour() == 12:
            heure = ' pm'
        else:
            heure = ' am'
        text = pygame.font.Font('font.ttf', self.size).render(str(self.what_hour()) + heure, True, (255, 255, 255))
        screen.blit(text, (0, 0))

    def death_monster(self, screen):
        screen.blit(pygame.transform.scale(self.cadavre, (1500, 1500)), (-750, -200))
        if not self.screamed:
            self.scream.play()
            self.screamed = True
        if self.screamtime > 0:
            self.screamtime -= 1
        else:
            self.screamer = False
            self.is_playing = False

    def death_cum(self):
        pass

    def reset(self):
        self.screamed = False
        self.is_atdoor = False
        self.is_atbed = False
        self.screamtime = self.scream.get_length() * 7
        self.horny_bar_width = 300
        self.screamer = True
        self.paused = False

    def pause(self):
        pass
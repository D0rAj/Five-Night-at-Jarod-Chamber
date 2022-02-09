import pygame


class Time:

    def __init__(self):
        self.hour = 0
        self.size = 50
        self.font = pygame.font.Font('font.ttf', self.size)

    async def go_time(self):
        if self.hour < 720:
            self.hour += 1
            pygame.time.wait(1000)

    def what_hour(self):
        hour = self.hour / 90
        return hour

    def write_time(self, screen):
        text = self.font.render(str(self.what_hour()) + ' pm', True, (255, 255, 255))
        screen.blit(text, (0, 0))
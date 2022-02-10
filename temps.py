import pygame
import time


class Time():

    def __init__(self):
        self.hour = 0
        self.size = 50

    async def go_time(self):
        if self.hour < 720:
            self.hour += 1
            time.sleep(1)

    def what_hour(self):
        hour = self.hour / 90
        return hour

    def write_time(self, screen, size):
        text = pygame.font.Font('font.ttf', size).render(str(self.what_hour()) + ' pm', True, (255, 255, 255))
        screen.blit(text, (0, 0))
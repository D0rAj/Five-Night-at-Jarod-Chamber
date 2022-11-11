import pygame
from game import Game

# settings
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Five Night at Jarod Chamber")
game = Game()

# background
background = pygame.image.load('assets/noir.png')

play_button = pygame.image.load('assets/NEW_GAME.png')
play_button = pygame.transform.scale(play_button, (200, 50))
play_button_rect = play_button.get_rect()
play_button_rect.x = 20
play_button_rect.y = 300

title = pygame.image.load('assets/Titre.png')
cadavre = pygame.image.load('assets/CADAVRE.jpg')
grain = pygame.image.load('assets/GRAIN.png')
clock = pygame.time.Clock()

# game run
running = True
while game.running:

    screen.blit(background, (0, 0))

    if game.is_playing:
        game.update(screen)
    else:
        screen.blit(cadavre, (0, 0))
        screen.blit(title, (0, 0))
        screen.blit(grain, (0, 0))
        screen.blit(play_button, play_button_rect)
        game.reset()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button_rect.collidepoint(pygame.mouse.get_pos()):
                    game.is_playing = True
    pygame.display.flip()
    clock.tick(7)
pygame.quit()
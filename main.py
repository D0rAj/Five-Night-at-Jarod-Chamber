import pygame
from arriereplan import ArrierePlan
# settings
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Five Night at Jarod Chamber")
arriere_plan = ArrierePlan()
# background
background = pygame.image.load('assets/noir.png')
sperme = pygame.image.load('assets/goutte_do.png')
play_button = pygame.image.load('assets/NEW_GAME.png')
play_button = pygame.transform.scale(play_button, (200, 50))
play_button_rect = play_button.get_rect()
play_button_rect.x = 20
play_button_rect.y = 300
clock = pygame.time.Clock()
# game run
running = True
while running:
    screen.blit(background, (0, 0))
    if arriere_plan.is_playing:
        running = arriere_plan.quit_check()
        arriere_plan.update(screen, sperme)
    else:
        screen.blit(play_button, play_button_rect)
        for event in pygame.event.get():
            print(pygame.QUIT)
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button_rect.collidepoint(pygame.mouse.get_pos()):
                    arriere_plan.is_playing = True
    pygame.display.flip()
    clock.tick(7)
pygame.quit()

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
        arriere_plan.update(screen, sperme)
    else:
        screen.blit(play_button, play_button_rect)
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if arriere_plan.is_playing:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if not arriere_plan.at_door:
                        arriere_plan.branlette_down()
                    elif arriere_plan.at_door:
                        arriere_plan.close_door()
                if event.key == pygame.K_LCTRL:
                    if arriere_plan.at_door:
                        arriere_plan.flashlight_on()
                if event.key == pygame.K_w:
                    arriere_plan.start_animation()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    if not arriere_plan.at_door:
                        arriere_plan.branlette_up()
                    elif arriere_plan.at_door:
                        arriere_plan.open_door()
                if event.key == pygame.K_LCTRL:
                    if arriere_plan.at_door:
                        arriere_plan.flashlight_off()
        else:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button_rect.collidepoint(pygame.mouse.get_pos()):
                    arriere_plan.is_playing = True
    clock.tick(7)
pygame.quit()

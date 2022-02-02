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
clock = pygame.time.Clock()
# game run
running = True
while running:
    screen.blit(background, (0, 0))
    if arriere_plan.is_playing:
        arriere_plan.update(screen, sperme)

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
    clock.tick(7)
pygame.quit()

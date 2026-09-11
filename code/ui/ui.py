import pygame

pygame.init()

sinfo = pygame.display.Info()
screen = pygame.display.set_mode((sinfo.current_w, sinfo.current_h), pygame.FULLSCREEN)
surface = pygame.surface.Surface((640, 480))

scale = min(sinfo.current_w/640, sinfo.current_h/480)
def uiloop(running):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    surface.fill((255, 255, 255))




    screen.blit(pygame.transform.scale(surface, (int(640*scale), int(480*scale))), (0, 0))
    pygame.display.flip()

    return running
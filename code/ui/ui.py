import pygame

pygame.init()

sinfo = pygame.display.Info()
screen = pygame.display.set_mode((sinfo.current_w, sinfo.current_h), pygame.FULLSCREEN)
surface = pygame.surface.Surface((640, 480))

appsurf = pygame.surface.Surface((640, 455))
topbar = pygame.surface.Surface((640, 25))

cursortex = pygame.image.load("assets/textures/mouse1.png").convert_alpha()
pygame.mouse.set_cursor(cursortex)


scale = min(sinfo.current_w/640, sinfo.current_h/480)
def uiloop(running):
    mpos = (
        int(pygame.mouse.get_pos()[0] // (sinfo.current_w / scale)),
        int(pygame.mouse.get_pos()[1] // (sinfo.current_h / scale)) 
    )

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # topbar
    topbar.fill((0, 255, 255))
    surface.blit(topbar, (0, 0))

    # appsurf
    appsurf.fill((255, 0, 255))
    surface.blit(appsurf,(0, 25))

    if pygame.mouse.get_pressed()[0]:
        surface.fill((255, 255, 255), (mpos[0], mpos[1], 10, 10))
    
    screen.blit(pygame.transform.scale(surface, (int(640*scale), int(480*scale))), ((sinfo.current_w - int(640*scale))//2, 0))
    pygame.display.flip()

    return running
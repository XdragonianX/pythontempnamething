import pygame

pygame.init()

sinfo = pygame.display.Info()
screen = pygame.display.set_mode((sinfo.current_w, sinfo.current_h), pygame.FULLSCREEN)
surface = pygame.surface.Surface((1920, 1080))

appsurf = pygame.surface.Surface((1920, 1040))
topbar = pygame.surface.Surface((1920, 40))

cursortex = pygame.image.load("assets/textures/mouse1.png").convert_alpha()
cursor = pygame.cursors.Cursor((0, 0), cursortex)
pygame.mouse.set_cursor(cursor)



scale = min(sinfo.current_w/1920, sinfo.current_h/1080)
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
    surface.blit(appsurf,(0, 40))

    screen.blit(pygame.transform.scale(surface, (int(1920*scale), int(1080*scale))), ((sinfo.current_w - int(1920*scale))//2, 0))
    
    pygame.display.flip()

    return running
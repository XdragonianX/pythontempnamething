import pygame
import time

pygame.init()

sinfo = pygame.display.Info()
screen = pygame.display.set_mode((sinfo.current_w, sinfo.current_h), pygame.FULLSCREEN)
surface = pygame.surface.Surface((1920, 1080))

appsurf = pygame.surface.Surface((1920, 1080))
topbar = pygame.surface.Surface((1920, 40), pygame.SRCALPHA)

cursortex = pygame.image.load("assets/textures/mouse1.png").convert_alpha()
cursor = pygame.cursors.Cursor((0, 0), cursortex)
pygame.mouse.set_cursor(cursor)

font1 = pygame.font.Font(None, 32)

currentbg = pygame.image.load("assets/textures/bg1.png").convert()

scale = min(sinfo.current_w/1920, sinfo.current_h/1080)
def uiloop(running):
    mpos = (
        int(pygame.mouse.get_pos()[0] // (sinfo.current_w / scale)),
        int(pygame.mouse.get_pos()[1] // (sinfo.current_h / scale)) 
    )
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    # appsurf
    appsurf.blit(currentbg, (0, 0))
    surface.blit(appsurf,(0, 0))

    # topbar
    topbar.fill((200, 200, 255, 20))
    pygame.draw.rect(topbar, (255, 255, 255), (5, 5, 30, 30))
    pygame.draw.rect(topbar, (255, 255, 255), (1900, 5, 15, 30))
    topbar.blit(font1.render(f"{time.strftime("%a %b %d %H:%M:%S")}", True, (255, 255, 255)), (0, 0))
    surface.blit(topbar, (0, 0))

    screen.blit(pygame.transform.scale(surface, (int(1920*scale), int(1080*scale))), ((sinfo.current_w - int(1920*scale))//2, 0))
    
    pygame.display.flip()

    return running
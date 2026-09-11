# module import
import os
import pygame

# file imports
import internet
import encrdecr
import apps
from ui import ui

import antiwindows # yes yes yes

clock = pygame.time.Clock()

running = True


class Main:
    def __init__(self):
        self.globcount = 0




    def loop(self, running):
        self.globcount += 1
        if self.globcount > 120: # could do == but WHATEVERRRR
            self.globcount = 0

        if self.globcount % 2 == 0:
            running = ui.uiloop(running)

        return running






if __name__ == "__main__":
    main = Main() # run init

    while running:
        running = main.loop(running) # run loop
        clock.tick(120)




# i tried so harddd and got so farrrrrrrrrrrr but in the endd it doesntt even matterrrr, i had to falll to loose it allll but in the end it doesnt even matterrr
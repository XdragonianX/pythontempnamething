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




    def loop(self):
        self.globcount += 1
        if self.globcount > 120: # could do == but WHATEVERRRR
            self.globcount = 0






if __name__ == "__main__":
    main = Main() # run init

    while running:
        main.loop() # run loop
        clock.tick(120)




# i tried so harddd and got so farrrrrrrrrrrr but in the endd it doesntt even matterrrr
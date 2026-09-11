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



"""
[Verse 1: Chester Bennington]
Graffiti decorations, under a sky of dust
A constant wave of tension, on top of broken trust
The lessons that you taught me, I learned were never true

[Pre-Chorus: Chester Bennington, Mike Shinoda]
Now I find myself in question
They point the finger at me again
Guilty by association
You point the finger at me again

[Chorus: Chester Bennington]
I wanna run away, never say goodbye
I wanna know the truth, instead of wondering why
I wanna know the answers, no more lies
I wanna shut the door, and open up my mind

[Verse 2: Chester Bennington]
Paper bags and angry voices, under a sky of dust
Another wave of tension, has more than filled me up
All my talk of taking action, these words were never true

[Pre-Chorus: Chester Bennington, Mike Shinoda]
Now I find myself in question
They point the finger at me again
Guilty by association
You point the finger at me again
You might also like
With You
Linkin Park
Points of Authority
Linkin Park
A Place for My Head
Linkin Park
[Chorus: Chester Bennington]
I wanna run away, never say goodbye
I wanna know the truth, instead of wondering why
I wanna know the answers, no more lies
I wanna shut the door, and open up my mind

[Bridge: Chester Bennington, Mike Shinoda]
I'm gonna run away, and never say goodbye
Gonna run away, gonna run away
Gonna run away, gonna run away
I'm gonna run away, and never wonder why
Gonna run away, gonna run away
Gonna run away, gonna run away
I'm gonna run away, and open up my mind
Gonna run away, gonna run away
Mind (Gonna run away, gonna run away)
Mind (Gonna run away, gonna run away)
Mind (Gonna run away, gonna run away)

[Chorus: Chester Bennington]
I wanna run away, never say goodbye
I wanna know the truth, instead of wondering why
I wanna know the answers, no more lies
I wanna shut the door, and open up my mind

[Outro: Chester Bennington, Chester Bennington & Mike Shinoda]
I wanna run away and open up my mind
I wanna run away and open up my mind
I wanna run away and open up my mind
I wanna run away and open up my mind
"""
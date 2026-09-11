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
LISSTEN TO LINKIN PARK INSTEAD 


[Kanye West and T-Pain:]
Like we always do at this time
I go for mine, I gots to shine
(Now throw your hands up in the sky)
I go go for mine, I gots to shine
(Now throw your hands up in the sky)
I'ma get on this TV momma, I'ma
I'ma put shit down
(Ayy) ayy (Ayy), ayy
(Ayy) ayy (Ayy), I'm good

[Kanye West:]
Welcome to the good life, where niggas who sell D
Won't even get pulled over in they new V
The good life, let's go on a living spree
Shit, they say the best things in life are free
The good life, it feel like Atlanta
It feel like L.A., it feel like Miami
It feel like NY, summertime Chi
Ah! (Now throw your hands up in the sky)
So I roll through good
Y'all pop the trunk, I pop the hood, Ferrari
And she got the goods
And she got that ass, I got to look, sorry!

Yo, it's got to be 'cause I'm seasoned
Haters give me them salty looks, Lawry's
50 told me, "Go 'head, switch the style up
And if they hate then let 'em hate and watch the money pile up"
The good life

[Kanye West and T-Pain:]
Now I, I go for mine, I got to shine
(Now throw your hands up in the sky)
Now I, I go for mine, I got to shine
(Now throw your hands up in the sky)
(I'ma get on this TV momma, I'ma)
(I'ma put shit down)
Ayy (Ayy), ayy (Ayy)
Ayy (Ayy), ayy (I'm good)

[Kanye West (T-Pain):]
Welcome to the good life!
Where we like the girls who ain't on TV
'Cause they got more (Ass than the models)
The good life, so keep it comin' with the bottles
'Cause she feel booze like she bombed at Apollo
The good life, it feel like Houston
It feel like Philly, it feel like D.C
It feel like VA or the Bay or Yay
Ayy, this is the good life (Welcome to the good life)
Homie, tell me what's good
Why I only got a problem when you in the hood (Welcome to the good life)
Like I'm new in the hood
The only thing I wish, I wish a nigga would (Welcome to the good life!)
He probably think he could
But, but, I don't think he should (Welcome to the good life)
50 told me, "Go 'head, switch the style up
And if they hate then let 'em hate and watch the money pile up"
The good life[Kanye West and T-Pain:]
Like we always do at this time
I go for mine, I gots to shine
(Now throw your hands up in the sky)
I go go for mine, I gots to shine
(Now throw your hands up in the sky)
I'ma get on this TV momma, I'ma
I'ma put shit down
(Ayy) ayy (Ayy), ayy
(Ayy) ayy (Ayy), I'm good

[Kanye West:]
Welcome to the good life, where niggas who sell D
Won't even get pulled over in they new V
The good life, let's go on a living spree
Shit, they say the best things in life are free
The good life, it feel like Atlanta
It feel like L.A., it feel like Miami
It feel like NY, summertime Chi
Ah! (Now throw your hands up in the sky)
So I roll through good
Y'all pop the trunk, I pop the hood, Ferrari
And she got the goods
And she got that ass, I got to look, sorry!

Yo, it's got to be 'cause I'm seasoned
Haters give me them salty looks, Lawry's
50 told me, "Go 'head, switch the style up
And if they hate then let 'em hate and watch the money pile up"
The good life

[Kanye West and T-Pain:]
Now I, I go for mine, I got to shine
(Now throw your hands up in the sky)
Now I, I go for mine, I got to shine
(Now throw your hands up in the sky)
(I'ma get on this TV momma, I'ma)
(I'ma put shit down)
Ayy (Ayy), ayy (Ayy)
Ayy (Ayy), ayy (I'm good)

[Kanye West (T-Pain):]
Welcome to the good life!
Where we like the girls who ain't on TV
'Cause they got more (Ass than the models)
The good life, so keep it comin' with the bottles
'Cause she feel booze like she bombed at Apollo
The good life, it feel like Houston
It feel like Philly, it feel like D.C
It feel like VA or the Bay or Yay
Ayy, this is the good life (Welcome to the good life)
Homie, tell me what's good
Why I only got a problem when you in the hood (Welcome to the good life)
Like I'm new in the hood
The only thing I wish, I wish a nigga would (Welcome to the good life!)
He probably think he could
But, but, I don't think he should (Welcome to the good life)
50 told me, "Go 'head, switch the style up
And if they hate then let 'em hate and watch the money pile up"
The good life
"""
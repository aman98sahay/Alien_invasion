import sys 

import pygame 

from settings import Settings
from ship import Ship 

def run_game () :
    # initialize pygame , settings and screen object 
    pygame.init()  
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))

    pygame.display.set_caption("Alien Invasion")

    # Make a ship 
    ship = Ship (screen) 

    # Start the main loop for the game
    while True :
        # Watch for keyboard and mouse events 
        for event in pygame.event.get():
            if event.type == pygame.QUIT :
                sys.exit ()
        
        # Redraw the screen during each pass through the loop
        screen.fill(ai_settings.bg_color)
        ship.blitme()

        # make the most recent drawn screen visible 
        pygame.display.flip()
        
run_game ()


import sys

import pygame

class AlienInvasion:
    'Overall class to manage game assests'
    
    def __init__(self):
        "initializing the game"
        pygame.init()
        
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")
        
    def run_game(self):
        "Start the main loop of the game"
        while True:
            "Key board and mouse events"
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                    
            "Make recently drawn screen visible"
            pygame.display.flip()
            
            
if __name__ == '__main__':
    "Make the game instance and run the game"
    ai = AlienInvasion()
    ai.run_game()
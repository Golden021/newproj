PYGAME_TEMPLATE = {
    'directories': [
        'src',
        'assets',
        'assets/images', 
        'assets/sounds'
    ],
    'files': [
        {
            'path': 'main.py',
            'content': '''import pygame
import sys

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("{project_name}")
        self.clock = pygame.time.Clock()
        self.running = True
    
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
    
    def update(self):
        pass
    
    def draw(self):
        self.screen.fill((0, 0, 0))
        pygame.display.flip()
    
    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)
        
        pygame.quit()
        sys.exit()

def main():
    game = Game()
    game.run()

if __name__ == "__main__":
    main()
'''
        },
        {
            'path': 'requirements.txt',
            'content': 'pygame>=2.0.0'
        },
        {
            'path': 'README.md',
            'content': '''# {project_name}

A Pygame project.

## Installation
pip install -r requirements.txt

## Usage
python main.py
'''
        }
    ]
}

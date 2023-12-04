import pygame

class Item:

    def __init__(self, x, y, health, happiness, image_name):
        self.x = x
        self.y = y
        self.health = health
        self.happiness = happiness
        self.image = pygame.image.load(image_name)
        rect = self.image.get_rect()
        self.image_rect = pygame.Rect(x - rect.width / 2, y - rect.height / 2, rect.width, rect.height)



class Game:
    def __init__(self):
        self.width = 500
        self.height = 500
        self.background_colour = 'white'
        self.buttons_bar_height = 100
        self.buttons_bar_colour = 'blue'

        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Pet')

        self.clock_tick = 60
        self.clock = pygame.time.Clock()

    def draw_everything(self):
        self.screen.fill(self.background_colour)
        pygame.draw.rect(self.screen, self.buttons_bar_colour, pygame.Rect(0, 0, self.width, self.buttons_bar_height))
        pygame.display.update()


    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                
            self.draw_everything()

            self.clock.tick(self.clock_tick)

pygame.init()
game = Game()
game.run()
https://www.youtube.com/watch?v=B5hKmlf5tCY

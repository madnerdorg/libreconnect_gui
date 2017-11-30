#https://stackoverflow.com/questions/14044147/animated-sprite-from-few-images#14044210

import pygame
import sys
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,  128,   0)
GREEN = (  0, 255,   0)
BLUE  = (  0,   0, 255)

loading_animation_count = 7
loading_animation_speed = 15

def load_image(name):
    image = pygame.image.load(name)
    return image

class TestSprite(pygame.sprite.Sprite):
    def __init__(self):
        super(TestSprite, self).__init__()
        self.images = []
        for i in xrange(loading_animation_count):
            self.images.append(load_image('data/sprites/'+str(i)+'loading.png'))

        # assuming both images are 64x64 pixels

        self.index = 0
        self.image = self.images[self.index]
        self.rect = pygame.Rect(200, 200, 200, 200)

    def update(self):
        '''This method iterates through the elements inside self.images and 
        displays the next one each tick. For a slower animation, you may want to 
        consider using a timer of some sort so it updates slower.'''
        self.index += 1
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]

def main():
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((500, 500))
    screen.fill(RED)

    my_sprite = TestSprite()
    my_group = pygame.sprite.Group(my_sprite)

    while True:
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)

        # Calling the 'my_group.update' function calls the 'update' function of all 
        # its member sprites. Calling the 'my_group.draw' function uses the 'image'
        # and 'rect' attributes of its member sprites to draw the sprite.
        my_group.update()
        my_group.draw(screen)
        pygame.display.flip()
        clock.tick(loading_animation_speed)
        

if __name__ == '__main__':
    main()
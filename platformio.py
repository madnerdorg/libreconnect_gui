# coding=utf-8

# Import pygame and libraries
from pygame.locals import *
from random import randrange
import os
import pygame
import subprocess
# Import pygameMenu
import pygameMenu
from pygameMenu.locals import *
import sys
from threading import Thread

platformio_folder = "E:\user\Google Drive\MADNERD\github"
TITLE = "LibreConnect Uploader"
AUTHOR = "madnerd.org"
EMAIL = "remi@madnerd.org"
VER = 0.11
COLOR_BACKGROUND = (0, 0, 0)
COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)
FPS = 60.0
MENU_BACKGROUND_COLOR = (228, 55, 36)
LOADING_ANIMATION_COUNT = 7
LOADING_ANIMATION_SPEED = 15
LOADING_ANIMATION_X = 200
LOADING_ANIMATION_Y = 200
arduino_dirs = []
arduino_inos = []


#####################################
# Search for platformio.ini files   #
#####################################
def searching():
    if os.path.isdir(platformio_folder):
        for root, dirs, files in os.walk(platformio_folder):
            for name in files:
                if name.endswith(("platformio.ini")):
                    print(dirs)
                    arduino_dirs.append(root)
                    arduino_inos_temp = root.split("\\")
                    arduino_inos.append(arduino_inos_temp[len(arduino_inos_temp)-2])

    print(arduino_dirs)
    print(arduino_inos)

##########################
# Sprite Animation
##########################
def load_image(name):
    image = pygame.image.load(name)
    return image

class LoadingSprite(pygame.sprite.Sprite):
    def __init__(self):
        super(LoadingSprite, self).__init__()
        self.images = []
        for i in xrange(LOADING_ANIMATION_COUNT):
            self.images.append(load_image('data/sprites/'+str(i)+'loading.png'))

        # assuming both images are 64x64 pixels
        
        self.index = 0
        self.image = self.images[self.index]
        self.rect = pygame.Rect(center_screen_x - (LOADING_ANIMATION_X * 0.5), center_screen_y - (LOADING_ANIMATION_Y * 0.5), LOADING_ANIMATION_X, LOADING_ANIMATION_Y)

    def update(self):
        '''This method iterates through the elements inside self.images and 
        displays the next one each tick. For a slower animation, you may want to 
        consider using a timer of some sort so it updates slower.'''
        self.index += 1
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]

##########################
# Uploading Screen
##########################

def upload(dir,ino):
    print(dir)
    print(ino)

def loading_function():
    pygame.mixer.music.load('data/music/loading.ogg')
    pygame.mixer.music.play(-1)
    bg_color = MENU_BACKGROUND_COLOR
    loading_sprite = LoadingSprite()
    loading_group = pygame.sprite.Group(loading_sprite)

    searching_thread = Thread(target=searching)
    searching_thread.daemon = True
    searching_thread.start()

    while searching_thread.isAlive():
        clock.tick(LOADING_ANIMATION_SPEED)
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        surface.fill(bg_color)
        pygame.display.flip()
        loading_group.update()
        loading_group.draw(surface)
        pygame.display.flip()
        clock.tick(LOADING_ANIMATION_SPEED)
    

def upload_function(scan_scope, font):
    # Draw random color and text
    bg_color = MENU_BACKGROUND_COLOR

    # Reset main menu and disable
    # You also can set another menu, like a 'pause menu', or just use the same
    # main_menu as the menu that will check all your input.
    main_menu.disable()
    main_menu.reset(1)

    while True:

        # Clock tick
        clock.tick(60)

        # Application events
        playevents = pygame.event.get()
        for e in playevents:
            if e.type == QUIT:
                sys.exit()
            elif e.type == KEYDOWN:
                if e.key == K_ESCAPE:
                    if main_menu.is_disabled():
                        main_menu.enable()

                        # Quit this function, then skip to loop of main-menu on line 197
                        return

        # Pass events to main_menu
        main_menu.mainloop(playevents)

        # Continue playing
        surface.fill(bg_color)
        pygame.display.flip()

##########################
# INIT PYGAME
##########################
# -----------------------------------------------------------------------------
# Init pygame
pygame.init()
pygame.mixer.init(44100, -16, 2, 2048)
sfx_change = 'data/sfx/menu_change.wav'
sfx_ok = 'data/sfx/menu_ok.wav'
sfx_back = 'data/sfx/menu_back.wav'
os.environ['SDL_VIDEO_CENTERED'] = '1'

# Create pygame screen and objects
###################################
# Responsive sizer
###################################
screen_info = pygame.display.Info()
# WINDOW_SIZE = (screen_info.current_w, screen_info.current_h)
WINDOW_SIZE = (320,240) # Simulate TFT Screen
#WINDOW_SIZE = (640,480) # Simulate TFT Screen
#WINDOW_SIZE = (1024,768) # Simulate TFT Screen
#WINDOW_SIZE = (1280,800) # Simulate TFT Screen
#WINDOW_SIZE = (1440,900) # Simulate TFT Screen
#WINDOW_SIZE = (1680,1050) # Simulate TFT Screen
#WINDOW_SIZE = (1920,1080) # Simulate TFT Screen
if WINDOW_SIZE[0] <= 320:
    FONT_SIZE_LARGE = 20
    FONT_SIZE_MEDIUM = 15
    FONT_SIZE_SMALL = 5
elif WINDOW_SIZE[0] <= 640:
    FONT_SIZE_LARGE = 40
    FONT_SIZE_MEDIUM = 30
    FONT_SIZE_SMALL = 10
elif WINDOW_SIZE[0] <= 1024:
    FONT_SIZE_LARGE = 60
    FONT_SIZE_MEDIUM = 50
    FONT_SIZE_SMALL = 20
elif WINDOW_SIZE[0] <= 1280:
    FONT_SIZE_LARGE = 60
    FONT_SIZE_MEDIUM = 50
    FONT_SIZE_SMALL = 30
elif WINDOW_SIZE[0] <= 1440:
    FONT_SIZE_LARGE = 80
    FONT_SIZE_MEDIUM = 70
    FONT_SIZE_SMALL = 40
elif WINDOW_SIZE[0] <= 1680:
    FONT_SIZE_LARGE = 80
    FONT_SIZE_MEDIUM = 70
    FONT_SIZE_SMALL = 50
elif WINDOW_SIZE[0] <= 1920:
    FONT_SIZE_LARGE = 100
    FONT_SIZE_MEDIUM = 80
    FONT_SIZE_SMALL = 50
print(FONT_SIZE_LARGE)
print(FONT_SIZE_MEDIUM)

center_screen_x = WINDOW_SIZE[0] * 0.5
center_screen_y = WINDOW_SIZE[1] * 0.5

print(screen_info)
surface = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption(TITLE)
clock = pygame.time.Clock()
dt = 1 / FPS

##########################
# Main Menu
##########################

def main_background():
    """
    Function used by menus, draw on background while menu is active.
    
    :return: None
    """
    surface.fill(COLOR_BACKGROUND)

# MAIN MENU
main_menu = pygameMenu.Menu(surface,
                            window_width=WINDOW_SIZE[0],
                            window_height=WINDOW_SIZE[1],
                            font=pygameMenu.fonts.FONT_BEBAS,
                            title='Platformio',
                            menu_alpha=100,
                            font_size=FONT_SIZE_SMALL,
                            menu_width=int(WINDOW_SIZE[0]),
                            menu_height=int(WINDOW_SIZE[1]),
                            onclose=PYGAME_MENU_DISABLE_CLOSE,  # ESC disabled
                            bgfun=main_background,
                            menu_color=MENU_BACKGROUND_COLOR,
                            option_shadow=False,
                            font_color=COLOR_BLACK,
                            color_selected=COLOR_WHITE,
                            sound_enable=True,
                            menu_sound_ok=sfx_ok,
                            menu_sound_change=sfx_change,
                            menu_sound_back=sfx_back
                            )

# -----------------------------------------------------------------------------
# Main loop
while True:

    # Tick
    clock.tick(60)



    loading_function()
    i = 0
    for ino in arduino_inos:
        main_menu.add_option(ino,upload,arduino_dirs[i],ino)
        i = i+1

    main_menu.add_option('Quit', PYGAME_MENU_EXIT)

    # Application events
    events = pygame.event.get()
    for event in events:
        if event.type == QUIT:
            sys.exit()

    pygame.mixer.music.stop()
    pygame.mixer.music.load('data/music/menu.ogg')
    pygame.mixer.music.play(-1)
    
    # Main menu
    main_menu.mainloop(events)

    # Flip surface
    pygame.display.flip()


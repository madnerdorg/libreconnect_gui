# coding=utf-8


# Import pygame and libraries
from pygame.locals import *
from random import randrange
import os
import pygame

# Import pygameMenu
import pygameMenu
from pygameMenu.locals import *

VER = 0.1
ABOUT = ['LibreConnect GUI v{0}'.format(VER),
         'Author: {0}'.format("madnerd.org"),
         TEXT_NEWLINE,
         'Email: {0}'.format("remi@madnerd.org")]
COLOR_BACKGROUND = (0, 0, 0)
COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)
FPS = 60.0
MENU_BACKGROUND_COLOR = (228, 55, 36)


# -----------------------------------------------------------------------------
# Init pygame
pygame.init()
pygame.mixer.init(44100, -16, 2, 2048)
sfx_change = 'data/sfx/menu_change.wav'
sfx_ok = 'data/sfx/menu_ok.wav'
sfx_back = 'data/sfx/menu_back.wav'
os.environ['SDL_VIDEO_CENTERED'] = '1'

# Create pygame screen and objects
screen_info = pygame.display.Info()
WINDOW_SIZE = (screen_info.current_w, screen_info.current_h)
#WINDOW_SIZE = (320,240) # Simulate TFT Screen
#WINDOW_SIZE = (640,480) # Simulate TFT Screen
#WINDOW_SIZE = (1024,768) # Simulate TFT Screen
#WINDOW_SIZE = (1280,800) # Simulate TFT Screen
#WINDOW_SIZE = (1440,900) # Simulate TFT Screen
#WINDOW_SIZE = (1680,1050) # Simulate TFT Screen
#WINDOW_SIZE = (1920,1080) # Simulate TFT Screen
if WINDOW_SIZE[0] <= 320:
    FONT_SIZE_LARGE = 20
    FONT_SIZE_MEDIUM = 15
elif WINDOW_SIZE[0] <= 640:
    FONT_SIZE_LARGE = 40
    FONT_SIZE_MEDIUM = 30
elif WINDOW_SIZE[0] <= 1024:
    FONT_SIZE_LARGE = 60
    FONT_SIZE_MEDIUM = 50
elif WINDOW_SIZE[0] <= 1280:
    FONT_SIZE_LARGE = 60
    FONT_SIZE_MEDIUM = 50
elif WINDOW_SIZE[0] <= 1440:
    FONT_SIZE_LARGE = 80
    FONT_SIZE_MEDIUM = 70
elif WINDOW_SIZE[0] <= 1680:
    FONT_SIZE_LARGE = 80
    FONT_SIZE_MEDIUM = 70
elif WINDOW_SIZE[0] <= 1920:
    FONT_SIZE_LARGE = 100
    FONT_SIZE_MEDIUM = 80


print(FONT_SIZE_LARGE)
print(FONT_SIZE_MEDIUM)

print(screen_info)
surface = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption('LibreConnect Scanner')
clock = pygame.time.Clock()
dt = 1 / FPS



# -----------------------------------------------------------------------------
def random_color():
    """
    Return random color.
    
    :return: Color tuple
    """
    return randrange(0, 255), randrange(0, 255), randrange(0, 255)


def scan_function(scan_scope, font):
    """
    Main game function
    
    :param difficulty: Difficulty of the game
    :param font: Pygame font
    :return: None
    """
    # Draw random color and text
    bg_color = random_color()

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
                exit()
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


def main_background():
    """
    Function used by menus, draw on background while menu is active.
    
    :return: None
    """
    surface.fill(COLOR_BACKGROUND)


# -----------------------------------------------------------------------------
# SCAN MENU
scan_menu = pygameMenu.Menu(surface,
                            window_width=WINDOW_SIZE[0],
                            window_height=WINDOW_SIZE[1],
                            font=pygameMenu.fonts.FONT_BEBAS,
                            title='Play menu',
                            menu_alpha=100,
                            font_size=FONT_SIZE_LARGE,
                            menu_width=int(WINDOW_SIZE[0]),
                            menu_height=int(WINDOW_SIZE[1]),
                            bgfun=main_background,
                            menu_color=MENU_BACKGROUND_COLOR,
                            option_shadow=False,
                            font_color=COLOR_BLACK,
                            color_selected=COLOR_WHITE,
                            onclose=PYGAME_MENU_DISABLE_CLOSE
                            )
# When pressing return -> play(DIFFICULTY[0], font)
scan_menu.add_option('Direct', scan_function, "local",
                     pygame.font.Font(pygameMenu.fonts.FONT_FRANCHISE, FONT_SIZE_LARGE))
scan_menu.add_option('Network', scan_function, "network",
                     pygame.font.Font(pygameMenu.fonts.FONT_FRANCHISE, FONT_SIZE_LARGE))
scan_menu.add_option('Return to main menu', PYGAME_MENU_BACK)

# ABOUT MENU
about_menu = pygameMenu.TextMenu(surface,
                                 window_width=WINDOW_SIZE[0],
                                 window_height=WINDOW_SIZE[1],
                                 font=pygameMenu.fonts.FONT_BEBAS,
                                 font_title=pygameMenu.fonts.FONT_8BIT,
                                 title='About',
                                 # Disable menu close (ESC button)
                                 onclose=PYGAME_MENU_DISABLE_CLOSE,
                                 font_color=COLOR_BLACK,
                                 text_fontsize=FONT_SIZE_MEDIUM,
                                 font_size_title=FONT_SIZE_LARGE,
                                 menu_color_title=COLOR_WHITE,
                                 menu_color=MENU_BACKGROUND_COLOR,
                                 menu_width=int(WINDOW_SIZE[0]),
                                 menu_height=int(WINDOW_SIZE[1]),
                                 option_shadow=False,
                                 color_selected=COLOR_WHITE,
                                 text_color=COLOR_BLACK,
                                 bgfun=main_background)
for m in ABOUT:
    about_menu.add_line(m)
about_menu.add_line(TEXT_NEWLINE)
about_menu.add_option('Return to menu', PYGAME_MENU_BACK)

# MAIN MENU
main_menu = pygameMenu.Menu(surface,
                            window_width=WINDOW_SIZE[0],
                            window_height=WINDOW_SIZE[1],
                            font=pygameMenu.fonts.FONT_BEBAS,
                            title='LibreConnect',
                            menu_alpha=100,
                            font_size=FONT_SIZE_LARGE,
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
main_menu.add_option('Scan', scan_menu)
main_menu.add_option('About', about_menu)
main_menu.add_option('Quit', PYGAME_MENU_EXIT)

# -----------------------------------------------------------------------------
# Main loop
while True:

    # Tick
    clock.tick(60)

    pygame.mixer.music.load('data/music/menu.ogg')
    pygame.mixer.music.play(-1)

    # Application events
    events = pygame.event.get()
    for event in events:
        if event.type == QUIT:
            exit()


    # Main menu
    main_menu.mainloop(events)

    # Flip surface
    pygame.display.flip()

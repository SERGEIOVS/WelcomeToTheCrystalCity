# import *
import pygame as pg , datetime , time , random , math , os ,logging
import sys
# from
from PIL import Image
import cv2
import pprint


from pathlib import Path

# путь к Scripts/Python
sys.path.append(str(Path(__file__).resolve().parent))

# my custom imorts
from Controllers.Background import * 
from Controllers.Units import * ;
from Controllers.Items import *
from Controllers.Vehicles import * ;
from Controllers.Controls import toggle_main_menu,mini_map_keyboard_controls,mini_map_mouse_controls,player_movement,Trade_menu
from Controllers.Funcs import start
from Controllers.Settings import *

# inits
pg.init()
pg.font.init()
pg.mixer.init()


# Простейший игровой цикл
running = True
clock = pg.time.Clock()

while running:
    start()



    if variables["game_state"] == 'Main_menu':toggle_main_menu()

    if variables["game_state"]  == 'Play' : 
        mini_map_mouse_controls()
        mini_map_keyboard_controls()
        player_movement()
    
    if variables["game_state"] == 'Trade_menu' : Trade_menu()

    pg.display.update()

pg.quit()
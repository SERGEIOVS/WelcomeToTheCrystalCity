import pygame as pg , datetime , time , random , math , sys ; from PIL import Image ; import os ; import logging ; from cv2 import log   #system/python modules
#my custom  files
import pprint
from Settings import * ; from Scripts.Python.Controllers.Background import * ; from Units import * ; from Items import * ; from Vehicles import * ;
from Controls import toggle_main_menu,mini_map_keyboard_controls,mini_map_mouse_controls,player_movement,Trade_menu
from Funcs import start
from Settings import *
pg.init()

# Простейший игровой цикл
running = True
clock = pg.time.Clock()

while running:
    start()



    if game_state == 'Main_menu':toggle_main_menu()

    if game_state == 'Play' : 
        mini_map_mouse_controls()
        mini_map_keyboard_controls()
        player_movement()
    
    if game_state == 'Trade_menu' : Trade_menu()

    pg.display.update()

pg.quit()
import sys , os
import pygame as pg ; from Settings import * ; from PIL import Image ; from Units import * ; import logging ; from Vihicles import * ; import pyautogui ;
from Background import * ; import math;import numpy as np
import time ; from Funcs import * ; from Settings import * ; from Items import *
import pprint
import cv2

import mido

import pyaudio
os.environ["SDL_VIDEODRIVER"] = '1'
pg.init()
pg.joystick.init()
p = pyaudio.PyAudio()

from sys import exit
from pygame.locals import *

#for i in range(p.get_device_count()):
#    info = p.get_device_info_by_index(i)
#    print(i, info["name"])

"""


angle = 60
dots_num = 10
dots = []
rocks = []
rock_size = 70
rock_scale = 2

sea_scale = 2
sea_size =200

for x in range(36):
            dots.append(

(

[300 + sea_size * math.cos(math.radians(x*10)) + random.randint(0,10) , 300 + sea_size// sea_scale * math.sin(math.radians(x*10)) + random.randint(0,10)]

)

)


for x in range(36):
            rocks.append(

(

[300 + rock_size * math.cos(math.radians(x*10)) + random.randint(0,10) , 300 + rock_size//rock_scale * math.sin(math.radians(x*10)) + random.randint(0,10)]

)

)


    screen.fill(BG_COLOR)
    pygame.draw.polygon(screen, BLUE , dots)
    pygame.draw.polygon(screen, (10,60,0) , rocks)

    
    pygame.draw.circle(screen, (10,100,0), (300 ,300), 4)
    
    for x in range(36):
        pygame.draw.circle(screen, (255,0,0), (300 + sea_size * math.cos(math.radians(x*10)) ,300 + sea_size  // 2 * math.sin(math.radians(x*10))), 3)


"""



#directories/folders
mods_dir_path = 'mods'
menus_dir = 'txt/menus/'
obj_dir   = 'Objects/'
MyShapes = []

vector = [ 0 , 0]#cam vectors

if mods_dir_path not in sys.path : sys.path.append(mods_dir_path)
if mods_dir_path in sys.path : print() ; print() ; print('mods folder added ! ')

print(os.listdir(mods_dir_path))

for i in range(10) : MyShapes.append('circle') ; MyShapes.append('square') ; MyShapes.append('triangle') ; MyShapes.append('rectangle')    

        
multiplayer = 1
pressed = pg.mouse.get_pressed() ; pos = pg.mouse.get_pos() ; clock = pg.time.Clock() ; FPS = 60 ; clock.tick(FPS)
hide_nicknames = 0 ; ground = 1 ; floor = 0 ; keys = pg.key.get_pressed()
fuel_bar_width = 100
minimapfontsize = int( 30 / map_scale) ; mini_map_font_size = pg.font.SysFont(font_name , minimapfontsize)

for i in custom_checkpoints_list:
    i = mini_map_font_size.render('Custom checkpoint' + int(i) , False , small_font_color ) 

interface_images = []
game_modes_file = open('txt/menus/Game_modes.txt','r') ; game_modes_file1 = game_modes_file.readlines() ; game_modes  = ['Survival' , 'God mode' , 'Hardcore'] ; game_modes1 = [] ; game_mode_num = 0 ; game_mode = game_modes_file1[game_mode_num]

for i in range(len(game_modes)) : i = big_font.render(game_modes[i].split(',')[0].strip() , False , small_font_color ) ; game_modes1.append(i)     

menu_titles = ['Backpack' , 'Crafting' , 'Quests'] ; menu_titles1 = [] ; menu_title_num = 0 ; menu_title = menu_titles[menu_title_num]
for i in range(len(menu_titles)) : i = small_font.render(menu_titles[i].split(',')[0].strip() , False , small_font_color ) ; menu_titles1.append(i)     

difficulties = ['Peaceful' , 'Easy' , 'Normal' , 'Hard'] ; difficulties1 = [] ; difficulty_num = 0 ; difficulty = difficulties[difficulty_num]
for i in range(len(difficulties)) : i = big_font.render(difficulties[i].split(',')[0].strip() , False , small_font_color ) ; difficulties1.append(i)     
difficulties_modes_file = open('txt/menus/difficulties.txt','r')

necessary_craft_items = [] ; prices_list  = [] ; prices_list1 = [] 

for i in range(len(prices_file1)) : prices_list.append(prices_file1[i])
for i in range(len(prices_list))  : i = big_font.render('Price : ' + prices_file1[i].strip() , False , small_font_color ) ; prices_list1.append(i)     

interface_surf_x   = 0   ; interface_surf_y    = int(screen_height ) - interface_surf.get_width() 
minimap_grid_width = 100 ; minimap_grid_height = 100 ; min_map_size = 3 ; max_map_size = 1.2 ; mini_map_grid_cell_size = meter * map_scale

cursor_types = ['Default' , 'Custom'] ; cursor_num = 0 ; cursor_type = cursor_types[cursor_num]

hero_inventory_types = ['Grid' , 'Circle'] ; hero_inventory_num = 0 ; hero_inventory_type = hero_inventory_types[hero_inventory_num] ; hero_marker_color = (255 , int(255 / 2) , 0)

room_height , room_width = 3 * meter  , 5 * meter ; room_size   = room_height * room_width ; walll_size  = 22

sidewalk_width , sidewalk_height = 3 * meter , 3 * meter

hero_path_lenght  = 90 ; hero_path_angle  = 90 ; hero_path_lenght1 = 90 ; hero_path_angle1 = 90 ; unit_path_lenght = 90 ; unit_path_angle = 90

cam_list = [random.randint(0,100) for i in range(0,10)];print(f'Cam list : {cam_list}')
 
islands_points =list(zip(

[

[int(1000 + int(random.randint(100,1000)) * math.cos(math.radians(i*10))) for i in range(36)],
[int(1000 + int(random.randint(100,1000)) * math.sin(math.radians(i*10))) for i in range(36)]

]
))

#CHARATER_CAMERAS
class cameras:
    def __init__( self , x , y ) :
        if multiplayer == 0:
            self.rect = pg.Rect( hero_path_lenght * -math.cos(hero_path_angle) ,hero_path_lenght * -math.sin(-hero_path_angle) , int(screen_width) , int(screen_height))

        else:#if multiplayer == 1
            self.rect = pg.Rect( hero_path_lenght * -math.cos(hero_path_angle) ,hero_path_lenght * -math.sin(-hero_path_angle) , int(screen_width)  // 2 , int(screen_height) // 2)

    def move( self , vector ) : self.rect[0] += hero_path_lenght * -math.cos(hero_path_angle) / 100 ; self.rect[1] += hero_path_lenght * -math.sin(hero_path_angle) / 100

camera1  = cameras(int(camera_x) + hero_path_lenght * -math.cos(hero_path_angle)                                         , int(camera_x) + hero_path_lenght * -math.sin(hero_path_angle)                                         )
camera2  = cameras(int(camera_x) + hero_path_lenght * -math.cos(hero_path_angle) +int(screen_file1[0].split(',')[0]) /2  , int(camera_x) + hero_path_lenght * -math.sin(hero_path_angle) + int(screen_file1[0].split(',')[1]) /2 )
camera3  = cameras(int(camera_x) + hero_path_lenght * -math.cos(hero_path_angle) +int(screen_file1[0].split(',')[0]) /2  , int(camera_x) + hero_path_lenght * -math.sin(hero_path_angle) + int(screen_file1[0].split(',')[1]) /2 )
camera4  = cameras(int(camera_x) + hero_path_lenght * -math.cos(hero_path_angle) +int(screen_file1[0].split(',')[0]) /2  , int(camera_x) + hero_path_lenght * -math.sin(hero_path_angle) + int(screen_file1[0].split(',')[1]) /2 )


print()
print()
print()

print(f'menus dir files: {os.listdir(menus_dir)}')

print()
print()
print()

print(f'obj dir files : {os.listdir(obj_dir)  }')

print()

for i in os.listdir(menus_dir) : print(f'menus_dir file: {i}')

print()
print()
print()

for i in os.listdir(obj_dir) : print(f'obj_dir : {i}')

print()
print()
print()


def draw_mini_map():
    if show_map == 1:
        for i in range( len ( islands_file1 ) ) :
            for y in range( len ( islands_file1 ) ) :
                pg.draw.rect(mini_map_surf , (100 , 50 , 0) , ( meter * 30 / (meter * map_scale) , meter * 30  / (meter / map_scale) , km * 5 / (meter * map_scale) , km * 5 / (meter * map_scale) ))

        for i in range( len ( buildings_file1 ) ) :
             if show_buildings == 1 : pg.draw.rect(mini_map_surf , (133 , 133 , 133)  , ( int(buildings_file1[ i ].split(',')[0]) / (100 * map_scale) + minimap_border_offset * 2 , int(buildings_file1[ i ].split(',')[1]) / (100 * map_scale) + minimap_object_offset1 * 2 ,  10 / map_scale, 10 / map_scale ))
        
        for i in range( len ( vihicles_file1 ) ) : pg.draw.rect(mini_map_surf , (0 , 0 , 0) , (int(vihicles_file1[i].split(',')[0]) / (100 * map_scale) + minimap_border_offset * minimap_object_offset , int(vihicles_file1[i].split(',')[1]) / (100 * map_scale) + minimap_border_offset * minimap_object_offset1 , 5 / map_scale , 3 / map_scale ))
        
        for i in range( len ( items_file1 ) ) :
            if show_items == 1 : pg.draw.rect(mini_map_surf , (0 , 255 , 0)  , (int(items_file1[i].split(',')[0]) / (100 * map_scale) + minimap_border_offset * minimap_object_offset , int(items_file1[i].split(',')[1]) / (100 * map_scale) + minimap_border_offset * minimap_object_offset1, 1 / map_scale , 1 / map_scale ))
        
        hero_marker = pg.draw.circle(mini_map_surf , ( hero_marker_color )        , ( minimap_border_offset + camera1.rect[0] / (100 * map_scale) + minimap_border_offset * minimap_object_offset ,  camera1.rect[1] / (100 * map_scale) + minimap_border_offset * minimap_object_offset1  ) , 1 / map_scale )        
        
        for i in range(len(custom_checkpoints_list_x)) : pg.draw.circle(mini_map_surf , (255 , 0 , 0) , ( int(custom_checkpoints_list_x[i]) / (100 * map_scale ) , int(custom_checkpoints_list_y[i]) / (100 * map_scale)) , int(1 / map_scale)  , int(1 / map_scale) )

        screen.blit(mini_map_surf , ( minimap_x , minimap_y ) )
        
        pg.draw.rect(screen , (minimap_border_color) , ( 0 , 0 , int(screen_width) / map_size + minimap_border_offset , int(screen_height) / map_size + minimap_border_offset ) , minimap_border_offset , minimap_border_offset)
        

        for i in range(len(MyShapes)):
            if 'circle'in MyShapes:pg.draw.circle(screen  , (255, 255,  255 ), (i * 100 , 500 ),50,1) 

        map_grid = 1 
        if map_grid == 1:
            for x in range(grid_size1):
                for y in range(grid_size2):pg.draw.rect(mini_map_surf , ( cell_color) , ( cell_size * x / map_scale * minimap_object_offset , cell_size * y / map_scale * minimap_object_offset1 , mini_map_grid_cell_size / map_scale , mini_map_grid_cell_size / map_scale) , 1 ) #drawing a inventory cells



def mini_map_keyboard_controls():

    keys = pg.key.get_pressed()
    global map_scale , minimap_x , minimap_y , map_size , minimap_horizontal_offset , minimap_vertical_offset , cancel_icon , cancel_icon_x , cancel_icon_y , mini_map_surf
    global minimap_object_offset , minimap_object_offset1

    if show_map == 1 and game_state == 'Play' :
        
        if keys [pg.K_LEFT ] : minimap_object_offset  -= 1 
        if keys [pg.K_RIGHT] : minimap_object_offset  += 1

        if keys [pg.K_UP   ] : minimap_object_offset1 -= 1
        if keys [pg.K_DOWN ] : minimap_object_offset1 += 1

        if keys [pg.K_KP_PLUS ] : mini_map_surf.fill((minimapBGcolor)) ; map_scale -= 0.01 ; draw_mini_map()
        if keys [pg.K_KP_MINUS] : mini_map_surf.fill((minimapBGcolor)) ; map_scale += 0.01 ; draw_mini_map()

        if map_size == max_map_size : screen.blit( cancel_icon , ( cancel_icon_x , cancel_icon_y))


    
        if keys [pg.K_KP_0] : map_size = min_map_size ; mini_map_surf = pg.Surface(( int(screen_width) / map_size , int(screen_height) / map_size ))
        if keys [pg.K_KP_1] : minimap_x = 0 ; minimap_y = int(screen_height) - int(screen_height) / map_size
        if keys [pg.K_KP_2] : minimap_x = 0 ; minimap_y = int(screen_height) - int(screen_height) / map_size
        if keys [pg.K_KP_3] : minimap_x = int(screen_width) - int(screen_width) / map_size ; minimap_y = int(screen_height) - int(screen_height) / map_size
        if keys [pg.K_KP_4] : minimap_x = int(screen_width) - int(screen_width) / map_size ; minimap_y = int(screen_height) - int(screen_height) / map_size
        if keys [pg.K_KP_5] : map_size = max_map_size ; mini_map_surf = pg.Surface(( int(screen_width) / map_size , int(screen_height) / map_size ))
        if keys [pg.K_KP_6] : minimap_x = int(screen_width) - int(screen_width) / map_size ; minimap_y = 0     
        if keys [pg.K_KP_7] : minimap_x = 0 ; minimap_y = 0
        if keys [pg.K_KP_8] : minimap_x = 0 ; minimap_y = 0
        if keys [pg.K_KP_9] : minimap_x = int(screen_width) - int(screen_width) / map_size ; minimap_y = 0



def mini_map_mouse_controls():
    global cancel_icon
    if game_state == 'Play' : 
        if event.button == 1 and pos[0] >= cancel_icon_x and pos[0] <= cancel_icon_x + cancel_icon.get_width() and pos[1] >= cancel_icon_y and pos[1] <= cancel_icon_y + cancel_icon.get_height() and map_size == max_map_size : map_size = min_map_size

        if event.button == 3 and map_size == max_map_size : spawn_sound.play() ; custom_checkpoints_list_x.append(camera1.rect[0] + pos[0]) ; custom_checkpoints_list_y.append(camera1.rect[1] + pos[1])

changed_keybinds = []

Random_events = []

def toggle_settings():
    if game_state == 'Settings':
        draw_menu()
        for i in range(len(settings_file1)):
            pg.draw.rect(screen , (Button_color) , ( int(screen_width) / 2 - button_width        , int(screen_height) / 2 - int(screen_height) / 4 - bigfont + i * 40 + bigfont / 2 , button_width , bigfont + 5 ), 0 , 0 , button_border_radius , button_border_radius , button_border_radius , button_border_radius)
            pg.draw.rect(screen , (Button_frame_color)  , ( int(screen_width) / 2 - button_width , int(screen_height) / 2 - int(screen_height) / 4 - bigfont + active_button * 40 + bigfont / 2 , button_width , bigfont + 5 ) , 2 , 0 , button_border_radius , button_border_radius , button_border_radius , button_border_radius )            
            screen.blit(settings[i] , ( int(screen_width) / 2 - bigfont * 10 / 2                 , int(screen_height) / 2 - int(screen_height) / 4 - bigfont + i             * 40 + bigfont / 2 , button_width , bigfont + 5 ))
            
            if active_button == 0:
                for i in range(len(resolutions_file1)):
                    Button = pg.draw.rect(screen , (Button_color ) , ( int(screen_width) / 2 + bigfont , int(screen_height) / 2 - int(screen_height) / 4 - bigfont + i              * 40 + bigfont / 2 , button_width , bigfont) , 0 , 0 , button_border_radius , button_border_radius , button_border_radius , button_border_radius)
                    pg.draw.rect(screen , (Button_frame_color)     , ( int(screen_width) / 2 + bigfont , int(screen_height) / 2 - int(screen_height) / 4 - bigfont + active_button1 * 40 + bigfont / 2 , button_width , bigfont) , 2 , 0 , button_border_radius , button_border_radius , button_border_radius , button_border_radius )
                    screen.blit(resolutions_list[i] , ( int(screen_width) / 2 + bigfont                , int(screen_height) / 2 - int(screen_height) / 4 - bigfont + i              * 40 + bigfont / 2))

            if active_button == 1 or active_button == 2:
                pg.draw.line(screen   , (0   , 0  , 0 ) , [ int(screen_width) / 2 + bigfont        , int(screen_height) / 2 - int(screen_height) / 4 - bigfont + 0 * 40 + bigfont ] , [ int(screen_width) / 2 + bigfont + 100 , int(screen_height) /2 - int(screen_height) /4 - bigfont + 0 * 40 + bigfont ] , 1 )
                pg.draw.circle(screen , (255 , 0  , 0 ) , ( int(screen_width) / 2 + bigfont        , int(screen_height) / 2 - int(screen_height) / 4 - bigfont + 0 * 40 + bigfont /2)  , 1)
                pg.draw.circle(screen , (255 , 0  , 0 ) , ( int(screen_width) / 2 + bigfont  + 100 , int(screen_height) / 2 - int(screen_height) / 4 - bigfont + 0 * 40 + bigfont /2)  , 1)
                
                pg.draw.rect(screen   , (Button_frame_color ) , ( int(screen_width) / 2 + bigfont  , int(screen_height) / 2 - int(screen_height) / 4 - bigfont + active_button1 * 40 + bigfont / 2 , button_width , bigfont) , 2 , 0 , button_border_radius , button_border_radius , button_border_radius , button_border_radius)
                screen.blit(ok          , ( int(screen_width) / 2 - bigfont * 10 / 2  + 300        , int(screen_height) / 2 - int(screen_height) / 4 - bigfont + i              * 40 + bigfont / 2 , button_width , bigfont ))
                screen.blit(add         , ( int(screen_width) / 2 + 500     / 4  + 10              , int(screen_height) / 2 - int(screen_height) / 4 - bigfont + i              * 40 + bigfont / 2 , 100 , bigfont ))
                screen.blit(remove      , ( int(screen_width) / 2 + 5                              , int(screen_height) / 2 - int(screen_height) / 4 - bigfont + i              * 40 + bigfont / 2 , 100 , bigfont ))
            
            if active_button == 3:
                for i in range(len(menus_dir)):
                    Button = pg.draw.rect(screen , (Button_color)        , ( int(screen_width) / 2 + bigfont , int(screen_height) / 2 - int(screen_height) / 4 - bigfont + i * 40 + bigfont / 2 , button_width , bigfont), 0 , 0 , button_border_radius , button_border_radius , button_border_radius , button_border_radius)
                    pg.draw.rect(screen          , (Button_frame_color)  , ( int(screen_width) / 2 + bigfont , int(screen_height) / 2 - int(screen_height) / 4 - bigfont + active_button1 * 40 + bigfont / 2 , button_width , bigfont),2 , 0 , button_border_radius , button_border_radius , button_border_radius , button_border_radius)
                    screen.blit(menus_dir[i]                            , ( int(screen_width) / 2 + bigfont , int(screen_height) / 2 - int(screen_height) / 4 - bigfont + i              * 40 + bigfont / 2))


def character_select():
    if game_state == 'character select menu':
        draw_menu()
        for i in range(len(Hero_types)):            
            Button = pg.draw.rect(screen , (Button_color) , ( int(screen_width) /  2 - button_width / 2 , int(screen_height) / 2 - int(screen_height) / 4 - bigfont + i * 40 + bigfont /2 , button_width , bigfont + 5 ) , 0 , 0 , button_border_radius , button_border_radius , button_border_radius , button_border_radius)            
            screen.blit(Hero_types_list[i]    , ( int(screen_width) /  2 - button_width / 2  , int(screen_height) / 2 - int(screen_height) / 4 - bigfont + i * 40 + bigfont / 2 , button_width , bigfont ))
            pg.draw.rect(screen , (Button_frame_color)  ,  ( int(screen_width) /  2 - button_width / 2 , int(screen_height) / 2 - int(screen_height) / 4 - bigfont + active_button * 40 + bigfont / 2 , button_width , bigfont + 5 ) , 2 , 0 , button_border_radius , button_border_radius , button_border_radius , button_border_radius)
            screen.blit(hero_image1 , ( int(screen_width) / 2 + int(screen_width) / 4 - hero_image1.get_width() /2 , hero_image1.get_height() ))


def game_mode_select():
    if game_state == 'game mode select':
        draw_menu()
        for i in range(len(game_modes1)):            
            Button = pg.draw.rect(screen , (Button_color) , ( int(screen_width) /  2 - button_width / 2 , int(screen_height) / 2 - int(screen_height) / 4 - bigfont + i * 40 + bigfont /2 , button_width , bigfont + 5 ) , 0 , 0 , button_border_radius , button_border_radius , button_border_radius , button_border_radius)            
            pg.draw.rect(screen , (Button_frame_color)    , ( int(screen_width) /  2 - button_width / 2 , int(screen_height) / 2 - int(screen_height) / 4 - bigfont + active_button * 40 + bigfont / 2 , button_width , bigfont + 5 ) , 2 , 0 , button_border_radius , button_border_radius , button_border_radius , button_border_radius)
            screen.blit(game_modes1[i]    , ( int(screen_width) /  2 - button_width / 2  , int(screen_height) / 2 - int(screen_height) / 4 - bigfont + i * 40 + bigfont / 2 , button_width , bigfont ))



def Difficulty_select():
    if game_state == 'Select a difficulty':
        draw_menu()
        for i in range(len(difficulties1)):            
            Button = pg.draw.rect(screen , (Button_color) , ( int(screen_width) /  2 - button_width / 2 , int(screen_height) / 2 - int(screen_height) / 4 - bigfont + i * 40 + bigfont /2 , button_width , bigfont + 5 ) , 0 , 0 , button_border_radius , button_border_radius , button_border_radius , button_border_radius)            
            pg.draw.rect(screen , (Button_frame_color)    , ( int(screen_width) /  2 - button_width / 2 , int(screen_height) / 2 - int(screen_height) / 4 - bigfont + active_button * 40 + bigfont / 2 , button_width , bigfont + 5 ) , 2 , 0 , button_border_radius , button_border_radius , button_border_radius , button_border_radius)
            screen.blit(difficulties1[i]                  , ( int(screen_width) /  2 - button_width / 2 , int(screen_height) / 2 - int(screen_height) / 4 - bigfont + i * 40 + bigfont / 2 , button_width , bigfont ))



def Open_backpack():
    if game_state == 'Backpack':
        draw_menu()
        for i in range(len(menu_titles1)):            
            Button = pg.draw.rect(screen , (Button_color) , (int(screen_width) / 2 - button_width - bigfont , int(screen_height) / 4 + cell_size * i , button_width , cell_size) , 0 , 0 , button_border_radius , button_border_radius , button_border_radius , button_border_radius)
            pg.draw.rect(screen , ( Button_frame_color  ) , (int(screen_width) / 2 - button_width - bigfont , int(screen_height) / 4 + cell_size * active_button , button_width , cell_size ) , 2 , 0 , button_border_radius , button_border_radius , button_border_radius , button_border_radius) #drawing a inventory cell_frame for a selected item in inventory
            screen.blit(menu_titles1[i]                   , (int(screen_width) / 2 - button_width - bigfont , int(screen_height) / 4 + cell_size * i , button_width , bigfont ))

            if show_interface == 1:
                if  active_button == 0:
                    for x in range(items_max):
                        for y in range(items_max):
                            pg.draw.rect(screen      , ( cell_color)           , ( int(screen_width) / 2 + cell_size * x , int(screen_height) / 4 + cell_size * y , cell_size , cell_size ) , 2 , 0 , button_border_radius , button_border_radius , button_border_radius , button_border_radius ) #drawing a inventory cells
                            pg.draw.rect(screen      , ( Button_frame_color  ) , ( int(screen_width) / 2 + cell_size * 0 , int(screen_height) / 4 + cell_size * active_button1 , cell_size , cell_size ) , 2 , 0 , button_border_radius , button_border_radius , button_border_radius , button_border_radius) #drawing a inventory cell_frame for a selected item in inventory
                    screen.blit(hero_inventory[item] , (int(screen_width ) / 2 , int(screen_height) - cell_size * 2  )) #drawing a title of the item in inventory            
                
                if active_button == 1 :                
                    for i in range(len(menus_dir) //crafts_on_page):
                            Button = pg.draw.rect(screen  , (Button_color)       , ( int(screen_width) / 2 + bigfont , int(screen_height) / 4 - bigfont + i              * 40 + bigfont / 2 , button_width , bigfont) , 0 , 0 , button_border_radius , button_border_radius , button_border_radius , button_border_radius)
                            pg.draw.rect(screen           , (Button_frame_color) , ( int(screen_width) / 2 + bigfont , int(screen_height) / 4 - bigfont + active_button1 * 40 + bigfont / 2 , button_width , bigfont) , 2 , 0 , button_border_radius , button_border_radius , button_border_radius , button_border_radius )
                            screen.blit(new_craft         , ( int(screen_width) / 2 + bigfont + button_width - cell_size , int(screen_height) / 10 + i * 40 , 100 , bigfont ))



def Open_unit_inventory():
    if vihicle_sit == 1:
        for x in range(items_max):
            for y in range(items_max):
                pg.draw.rect(screen          , ( cell_color)           , ( int(screen_width)  / 4 + cell_size * x , int(screen_height) / 4 + cell_size * y , cell_size , cell_size ) , 2 , 0 , button_border_radius , button_border_radius , button_border_radius , button_border_radius ) #drawing a inventory cells
                pg.draw.rect(screen          , ( Button_frame_color  ) , ( int(screen_width)  / 4 + cell_size * 0 , int(screen_height) / 4 + cell_size * active_button1 , cell_size , cell_size ) , 2 , 0 , button_border_radius , button_border_radius , button_border_radius , button_border_radius) #drawing a inventory cell_frame for a selected item in inventory
            screen.blit(hero_inventory[item] , (int(screen_width ) / 2 ,   int(screen_height) - cell_size     * 2  )) #drawing a title of the item in inventory            
                


def Trade_menu():
    obj_dir = os.listdir('Objects/')
    if game_state      == 'Trade menu':
        menu_titles    = [obj_dir[i] for i in range(len(obj_dir))]
        
        menu_titles1   = []
        menu_title_num = 0
        menu_title     = menu_titles[menu_title_num]
        for i in menu_titles: i = big_font.render(menu_titles[i].split(',')[0].strip() , False , small_font_color ) ; menu_titles1.append(i)   

        draw_menu()
        
        for i in range(len(menu_titles1)):            
            Button = pg.draw.rect(screen , (Button_color) , (int(screen_width) / 2 - button_width - bigfont , int(screen_height) / 4 + cell_size * i , button_width , cell_size) , 0 , 0 , button_border_radius , button_border_radius , button_border_radius , button_border_radius)
            pg.draw.rect(screen , ( Button_frame_color  ) , (int(screen_width) / 2 - button_width - bigfont , int(screen_height) / 4 + cell_size * active_button , button_width , cell_size ) , 2 , 0 , button_border_radius , button_border_radius , button_border_radius , button_border_radius) #drawing a inventory cell_frame for a selected item in inventory
            screen.blit(menu_titles1[i]             ,       (int(screen_width) / 2 - button_width - bigfont , int(screen_height) / 4 + cell_size * i , button_width , bigfont ))
            for i in range(len(menus_dir) //crafts_on_page):
                        Button = pg.draw.rect(screen  , (Button_color)       , ( int(screen_width) / 2 + bigfont , int(screen_height) / 4 - bigfont + i              * 40 + bigfont / 2 , button_width , bigfont) , 0 , 0 , button_border_radius , button_border_radius , button_border_radius , button_border_radius)
                        pg.draw.rect(screen           , (Button_frame_color) , ( int(screen_width) / 2 + bigfont , int(screen_height) / 4 - bigfont + active_button1 * 40 + bigfont / 2 , button_width , bigfont) , 2 , 0 , button_border_radius , button_border_radius , button_border_radius , button_border_radius )
                        screen.blit(new_craft         ,                        ( int(screen_width) / 2 + bigfont , int(screen_height) / 10 + i * 40 , 100 , bigfont ))
            for i in range(len(prices_list1)) : screen.blit(prices_list1[i] ,  ( int(screen_width) / 2 + bigfont + button_width / 2   , int(screen_height) / 2 - int(screen_height) / 4 - bigfont + i * 40 + bigfont / 2 , button_width , bigfont ))



def toggle_main_menu():
    if game_state == 'Main menu':
        draw_menu()
        for i in range(len(os.listdir(menus_dir))):
            pg.draw.rect(screen , (Button_color) , (int(screen_width) /  2 - button_width / 2 , int(screen_height) / 2 - int(screen_height) / 4 - bigfont + i * 40 + bigfont / 2 , button_width , bigfont + 5 ) , 0 , 0 , button_border_radius , button_border_radius , button_border_radius , button_border_radius)            
            pg.draw.rect(screen , (Button_frame_color)    , (int(screen_width) /  2 - button_width / 2 , int(screen_height) / 2 - int(screen_height) / 4 - bigfont + active_button * 40 + bigfont / 2 , button_width , bigfont + 5 ) , 2 , 0 , button_border_radius , button_border_radius , button_border_radius , button_border_radius)
            screen.blit(show_mods_count                   , (int(screen_width) /  2 - button_width / 2 + 75 , int(screen_height) / 2 - int(screen_height) / 4 - bigfont + 3 * 40 + bigfont / 2 , button_width , bigfont ))




def toggle_mods_menu():
    if game_state == 'Mods menu':
        draw_menu()
        for i in range(len(mods_dir_path)):
            Button = pg.draw.rect(screen , (Button_color) , (int(screen_width) /  2 - button_width / 2 , int(screen_height) / 2 - int(screen_height) / 4 - bigfont + i * 40 + bigfont / 2 , button_width , bigfont + 5 ) , 0 , 0 , button_border_radius , button_border_radius , button_border_radius , button_border_radius)            
            screen.blit(mods_dir_path[i]                      , (int(screen_width) /  2 - button_width / 2 , int(screen_height) / 2 - int(screen_height) / 4 - bigfont + i * 40 + bigfont / 2 , button_width , bigfont ))
            pg.draw.rect(screen , (Button_frame_color)    , (int(screen_width) /  2 - button_width / 2 , int(screen_height) / 2 - int(screen_height) / 4 - bigfont + active_button * 40 + bigfont / 2 , button_width , bigfont + 5 ) , 2 , 0 , button_border_radius , button_border_radius , button_border_radius , button_border_radius)



def text_updating(): 
    global new_craft,new_quest,checkpoints_list,achievements_list,hero_inventory_nums,show_game_state,ok
    global apply,cancel,action_counter,checkpoints_file1,dialoge_started,achievements_file1,checkpoint_size,dialoge_num,action,checkpoint_num
    global titles_list,menus_dir
    hero_inventory = [] ; hero_inventory_nums = [] ; hero_inventory_file_name = 'txt/langs/' + str(language) + '/Hero inventory.txt' ; hero_inventory_file_mode = 'r' ; hero_inventory_file = open (hero_inventory_file_name , hero_inventory_file_mode , encoding= "utf-8") ; hero_inventory_file1 = hero_inventory_file.readlines()
    text = "Пример"
    text_surface = big_font.render(text, True, (255, 255, 255))  # белый текст
    rotated_surface = pg.transform.rotate(text_surface, fuel)  # поворот на 45 градусов
    rect = rotated_surface.get_rect(center=(200, 550))
    screen.blit(rotated_surface, rect)

    
    titles_list = []
    for i in os.listdir(menus_dir) :
            i = big_font.render(str(i)  , False , small_font_color ) ; titles_list.append(i)


    

    new_craft = small_font.render('Uus' , False , small_font_color ) ; ok = small_font.render('OK' , False , small_font_color ) ; apply = small_font.render('Apply'  , False , small_font_color) ; cancel = small_font.render('Tagasi'  , False , small_font_color)
    show_game_state = big_font.render('Menüü' , False , small_font_color)




def player_movement():

        global calc_dist,show_distance,hero_checkpoint_offset_x,hero_checkpoint_offset_y,state,hero_x,hero_y,turn,hero_speed,minimap_object_offset,minimap_object_offset1,hero_path_lenght,hero_path_angle,rot_hero,scaled_image
        global original_hero_img_width,original_hero_img_height,new_hero_img_width,new_hero_img_height,scale_factor,rect,new_hero_img_width,new_hero_img_height

        keys = pg.key.get_pressed()
        if game_state == 'Play':

            if keys[pg.K_a]:
                state = 'go'
                turn  = 'left'
                hero_speed = 4
                vector[0] -= hero_path_lenght * math.cos(hero_path_angle) / 100
                vector[1] -= hero_path_lenght * math.sin(hero_path_angle) / 100

                #show_distance = small_font.render(f'Distance : {calc_dist / 100} + m', False, small_font_color)
            
            if keys[pg.K_d]:
                state = 'go'
                turn = 'right'
                hero_speed = 4 
                vector[0] += hero_path_lenght * math.cos(hero_path_angle) / 100
                vector[1] += hero_path_lenght * math.sin(hero_path_angle) / 100

                hero_checkpoint_offset_x += hero_speed

                #show_distance = small_font.render(f'Distance : {calc_dist / 100} + m', False, small_font_color)
                minimap_object_offset -= 1 / (map_scale * hero_speed * 10)  #hero_image =  pg.image.load(hero) ; heroimage = Image.open(hero) ; hero_x , hero_y = int(screen_width) / 2  - heroimage.width / 2 , int(screen_height)  / 2 - heroimage.height / 2
            
            if keys[pg.K_w]:
                hero_path_lenght += 10
                hero_checkpoint_offset_y -= hero_speed

                #show_distance = small_font.render(f'Distance : {calc_dist / 100} + m', False, small_font_color)
                minimap_object_offset1 += 1 / (map_scale * hero_speed * 10)
            
            
            if keys[pg.K_s]:
                hero_path_lenght -= 10
                hero_checkpoint_offset_y += hero_speed
                hero_x , hero_y = int(screen_width) / 2  - heroimage.width / 2 , int(screen_height)  / 2 - heroimage.height / 2
                #show_distance = small_font.render(f'Distance : {calc_dist / 100} + m', False, small_font_color)
                minimap_object_offset -= 1 / (map_scale * hero_speed * 10)
            
            if keys[pg.K_q]: hero_path_angle += 0.1
            if keys[pg.K_e]: hero_path_angle -= 0.1
            
            rot_hero = pg.transform.rotate(hero_image,math.degrees(hero_path_angle))

            rect = rot_hero.get_rect(center=(hero_image.get_width(),hero_image.get_width()))

            scale_factor = 2
            original_hero_img_width = hero_image.get_width() ; original_hero_img_height = hero_image.get_height()



            scaled_image = pg.transform.scale(rot_hero, (hero_image.get_width() * scale_factor, hero_image.get_height() * scale_factor))
                        
            if keys[pg.K_k]:
                scale_factor += 0.1
                print(f'scale factor : {scale_factor}')

                scaled_image = pg.transform.scale(rot_hero, (original_hero_img_width, original_hero_img_height))

                new_hero_img_width  = int(hero_image.get_width()) ; new_hero_img_height = int(hero_image.get_height())


            if keys[pg.K_l]:
                scale_factor -= 0.1
                print(scale_factor)

                scaled_image = pg.transform.scale(rot_hero, (original_hero_img_width, original_hero_img_height))
                
                new_hero_img_width  = int(hero_image.get_width()) ; new_hero_img_height = int(hero_image.get_height())



        if vector != [ 0 , 0 ] : camera1.move(vector) #Если игрок ходил


        
        # Обновление смещения на мини-карте
        minimap_object_offset  += 1 / (map_scale * hero_speed * 10) if vector[0] < 0 else -1 / (map_scale * hero_speed * 10) ; minimap_object_offset1 += 1 / (map_scale * hero_speed * 10) if vector[1] < 0 else -1 / (map_scale * hero_speed * 10)


listen_midi = 0
def start():


    global vol_limit,frame1,frame2
    import pyaudio, numpy as np

    pa = pyaudio.PyAudio()
    stream = pa.open(format=pyaudio.paInt16, channels=1, rate=44100,input=True, frames_per_buffer=1024)

    data = np.frombuffer(stream.read(1024), dtype=np.int16)
    vol_limit = 400
    volume = np.abs(data).mean()
    print(f" Громкость микрофона : {int(volume)}")
    if volume > vol_limit :     print(f" ГРОМКО! : {int(volume)}")

    import cv2
    import pygame
    import numpy as np
        



    global fuel,listen_midi,frame1,frame2
    print("доступные миди устройства: ")
    
    for num,i in enumerate(mido.get_input_names()):
        print(f"устройство {num} : {i}")# можно выбрать по индексу или строке
    print()

    """
        # выбираем устройство
        midi_device = 7 ; port_name = mido.get_input_names()[int(midi_device)]  # можно выбрать по индексу или строке
        with mido.open_input(port_name) as inport:
            print(f"Слушаю {port_name}...")
            # список доступных входов
            print("Доступные устройства MIDI:",mido.get_input_names())
            print()
            if listen_midi == 1:
                for msg in inport:
                    print(msg)
                    if midi_device == 0:
                        if msg.type == "control_change" and msg.control  == 30:
                            fuel += 1
                            print(f"fuel: {fuel}")
                        
                        if msg.type == "note_on" and msg.note == 55:
                                print(f"включаем {port_name}")
                                listen_midi = 1
                                sleep(1)

                        if msg.type == "note_on" and msg.note == 55:
                                print(f"выключаем {port_name}")
                                listen_midi = 0
                                sleep(1)


"""



    if game_state == 'Saves':
        draw_menu()
        draw_mini_map()
        for i in range(len(saves_file1)):
            Button = pg.draw.rect(screen , (Button_color) , ( int(screen_width) /  2 - button_width / 2 , int(screen_height) / 2 - int(screen_height) / 4 - bigfont + i * 40 + bigfont /2 , button_width , bigfont + 5 ) , 0 , 0 , button_border_radius , button_border_radius , button_border_radius , button_border_radius)            
        #screen.blit(saves_list[i]                     , ( int(screen_width) /  2 - button_width / 2 , int(screen_height) / 2 - int(screen_height) / 4 - bigfont + i * 40 + bigfont / 2 , button_width , bigfont ))
        pg.draw.rect(screen , (Button_frame_color)    , ( int(screen_width) /  2 - button_width / 2 , int(screen_height) / 2 - int(screen_height) / 4 - bigfont + active_button * 40 + bigfont / 2 , button_width , bigfont + 5 ) , 2 , 0 , button_border_radius , button_border_radius , button_border_radius , button_border_radius)

    if game_state == 'Crafting':
        draw_menu()
        for i in range(len(menus_dir) // crafts_on_page) :
                
                #drawing a buttons for a crafts menu
                Button = pg.draw.rect(screen , (Button_color)       , ( int(screen_width) / 2 - button_width / 2 , int(screen_height) /10 + i * 40 , 500 , bigfont) , 2 , 0 , button_border_radius , button_border_radius , button_border_radius , button_border_radius)
                pg.draw.rect(screen          , (Button_frame_color) , ( int(screen_width) / 2 - button_width / 2  , int(screen_height) /10 + active_button * 40 , 500 , bigfont) , 2 , 0 , button_border_radius , button_border_radius , button_border_radius , button_border_radius )
                screen.blit(str(i)   , ( int(screen_width) / 2 - button_width / 2 + bigfont , int(screen_height) / 10 + i * 40 , 100 , bigfont ))
                screen.blit(new_craft        , ( int(screen_width) / 2 + - button_width / 2 - cell_size * 2 , int(screen_height) / 10 + i * 40 , 100 , bigfont ))

    toggle_settings() ; toggle_main_menu() ; character_select() ; Trade_menu() ; game_mode_select() ; Open_backpack() ; mini_map_keyboard_controls() ; Difficulty_select() ; toggle_mods_menu()

    if game_state == 'Play':
                
        """        cam_num1 =0

                cap1 = cv2.VideoCapture(cam_num1)
                ret1 ,frame= cap1.read()
                # Считываем кадр с камеры\
                if cap1.isOpened():
                        print("удалось открыть камеру!")
                else:
                    print("камера не  работает!")

                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                frame = cv2.transpose(frame)
                frame = cv2.flip(frame, 0)
                frame_size = 180,180
                frame_location = 0,400    
                frame_surface = pg.surfarray.make_surface(frame)
                frame_surface = pg.transform.scale(frame_surface, (frame_size[0],frame_size[1]))
                screen.blit(frame_surface, (frame_location[0],frame_location[1]))


                cam_num2 =2

                cap2 = cv2.VideoCapture(cam_num2)
                ret2 ,frame2= cap2.read()
                # Считываем кадр с камеры\
                if cap2.isOpened():
                        print("удалось открыть камеру!")
                else:
                    print("камера не  работает!")

                frame2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2RGB)
                frame2 = cv2.transpose(frame2)
                frame2 = cv2.flip(frame2, 0)
                frame2_size = 180,180
                frame2_location = 0,600    
                frame2_surface = pg.surfarray.make_surface(frame2)
                frame2_surface = pg.transform.scale(frame2_surface, (frame2_size[0],frame2_size[1]))
                screen.blit(frame2_surface, (frame2_location[0],frame2_location[1]))

        """

        mouse_visible = False ; mouse_set_visible = pg.mouse.set_visible( mouse_visible )

        if ground == 1:

            world_border = pg.draw.rect(screen , (Button_frame_color) , ( -camera1.rect[ 0 ] + 0 ,-camera1.rect[ 1 ] + 0 , map_width , map_width) , 10 , 0  )

            #islands
            for i in range(len(islands_points)):
                pg.draw.polygon(screen , (100,25,0),islands_points)



            for i in range( len ( vihicles_file1 ) ) : 
                 if camera1.rect[0] + int(screen_width) - fov >= int(vihicles_file1[i].split(',')[0])  and camera1.rect[1] + int(screen_height) - fov >= int(vihicles_file1[i].split(',')[1]) and hero_image != vihicles_images_list[i]:
                    screen.blit( vihicles_images_list[i] , ( -camera1.rect[ 0 ] + int(vihicles_file1[i].split(',')[0]) , -camera1.rect[ 1 ] + int(vihicles_file1[i].split(',')[1]) ) )



            #rooms
            for i in range(len(buildings_file1)) :

                #room_floor
                pg.draw.polygon(screen , (colors[7]) , (       
                    
[-camera1.rect[0] + 1000 + int(buildings_file1[i].split(',')[0])                               , -camera1.rect[1] + 1000 + int(buildings_file1[i].split(',')[1])  ] ,
[-camera1.rect[0] + 1000 + int(buildings_file1[i].split(',')[0]) + meter * 3  * math.cos(fuel) , -camera1.rect[1] + 1000 + int(buildings_file1[i].split(',')[1]) + meter * 3  * math.sin(fuel) ] , 
[-camera1.rect[0] + 1000 + int(buildings_file1[i].split(',')[0]) + meter * 15 * math.cos(fuel) , -camera1.rect[1] + 1000 + int(buildings_file1[i].split(',')[1]) + meter * 3  * math.sin(fuel) ] ,
[-camera1.rect[0] + 1000 + int(buildings_file1[i].split(',')[0]) + meter * 7  * math.cos(fuel) , -camera1.rect[1] + 1000 + int(buildings_file1[i].split(',')[1])  ] , 
                                                                  
))



                #room_celling
                pg.draw.polygon(screen , (colors[5]) ,     (  

[-camera1.rect[0] + 1000 + int(buildings_file1[i].split(',')[0])                               , -camera1.rect[1] + 1000 + int(buildings_file1[i].split(',')[1]) - room_height ] ,
[-camera1.rect[0] + 1000 + int(buildings_file1[i].split(',')[0]) + meter * 3  * math.cos(fuel) , -camera1.rect[1] + 1000 + int(buildings_file1[i].split(',')[1]) + meter * 3 * math.sin(fuel) - room_height ] , 
[-camera1.rect[0] + 1000 + int(buildings_file1[i].split(',')[0]) + meter * 15 * math.cos(fuel) , -camera1.rect[1] + 1000 + int(buildings_file1[i].split(',')[1]) + meter * 3 * math.sin(fuel) - room_height ] ,
[-camera1.rect[0] + 1000 + int(buildings_file1[i].split(',')[0]) + meter * 7  * math.cos(fuel) , -camera1.rect[1] + 1000 + int(buildings_file1[i].split(',')[1])  - room_height  ] ,

[-camera1.rect[0] + 1000 + int(buildings_file1[i].split(',')[0]) + meter * 7  * math.cos(fuel) , -camera1.rect[1] + 1000 + int(buildings_file1[i].split(',')[1]) - room_height + meter / 2 ] ,
[-camera1.rect[0] + 1000 + int(buildings_file1[i].split(',')[0]) + meter * 7  * math.cos(fuel) , -camera1.rect[1] + 1000 + int(buildings_file1[i].split(',')[1]) - room_height + meter / 2 ] ,      
[-camera1.rect[0] + 1000 + int(buildings_file1[i].split(',')[0])                               , -camera1.rect[1] + 1000 + int(buildings_file1[i].split(',')[1]) - room_height + meter / 2 ] ,      

))
                


                #room_walls
                pg.draw.polygon(screen , ( colors[6] ) , (  

[-camera1.rect[0] + 1000 + int(buildings_file1[i].split(',')[0])                               , -camera1.rect[1] + 1000 + int(buildings_file1[i].split(',')[1])   ] ,
[-camera1.rect[0] + 1000 + int(buildings_file1[i].split(',')[0])                               , -camera1.rect[1] + 1000 + int(buildings_file1[i].split(',')[1]) - meter] ,
                                                               
[-camera1.rect[0] + 1000 + int(buildings_file1[i].split(',')[0]) + meter * 7  * math.cos(fuel) , -camera1.rect[1] + 1000 + int(buildings_file1[i].split(',')[1]) - meter ],
[-camera1.rect[0] + 1000 + int(buildings_file1[i].split(',')[0]) + meter * 7  * math.cos(fuel) , -camera1.rect[1] + 1000 + int(buildings_file1[i].split(',')[1]) - meter ],                                                         
                                                               
[-camera1.rect[0] + 1000 + int(buildings_file1[i].split(',')[0]) + meter * 7  * math.cos(fuel) , -camera1.rect[1] + 1000 + int(buildings_file1[i].split(',')[1]) ]

))
                
                

            #for i in range(len(checkpoints_file1)) : pg.draw.circle(screen , (255 , 0 , 0 ) , (-camera.rect[0] + int(checkpoints_file1[i].split(',')[0]) + 50 , -camera.rect[1] + int(checkpoints_file1[i].split(',')[1]) + 180) , 50 , 1 )

        for i in range(len(custom_checkpoints_list_x)):
            if len(custom_checkpoints_list) != 0:
                pg.draw.circle(screen , (255 , 0 , 0)      , ( -camera1.rect[ 0 ] + int(custom_checkpoints_list_x[i]) , -camera1.rect[ 1 ] + int(custom_checkpoints_list_y[i])      ) , 20  , 5 )
                screen.blit(custom_checkpoint_title        , ( -camera1.rect[ 0 ] + int(custom_checkpoints_list_x[i]) , -camera1.rect[ 1 ] + int(custom_checkpoints_list_y[i]) - 50 ))
                mini_map_surf.blit(custom_checkpoint_title , ( -camera1.rect[ 0 ] + int(custom_checkpoints_list_x[i]) , -camera1.rect[ 1 ] + int(custom_checkpoints_list_y[i]) - 50 ))


        #drawing a text for a quests menu
        if len(quests_file1) != 0:
            for i in range(len(quests_file1)) : quests_surf.blit(quests_list[i] , (5 , 5 + bigfont / 2 * i * 1.6 ) ) ; #screen.blit(show_quests_num , (int(screen_width ) - int(screen_width) /3  , int(screen_height ) - int(screen_height) /3 - bigfont ) )

        for i in range(len(Furniture_file1)) :
            for y in range(int(Furniture_file1[i].split(',')[2])):
                if camera1.rect[0] + int(screen_width) - fov >= int(Furniture_file1[i].split(',')[0]) and camera1.rect[1] + int(screen_height) - fov >= int(Furniture_file1[i].split(',')[1]) : screen.blit( Furniture_images_list[ i ] , ( -camera1.rect[ 0 ] + int(Furniture_file1[i].split(',')[0]) + int(Furniture_file1[i].split(',')[2]) * y * 10  , -camera1.rect[ 1 ] + int(Furniture_file1[i].split(',')[1] ) ) )
                
        for i in range(len(items_file1)) :
                if camera1.rect[0] + int(screen_width) - fov >= int(items_file1[i].split(',')[0]) and camera1.rect[1] + int(screen_height) - fov >= int(items_file1[i].split(',')[1]) : screen.blit( items_images[ i ] , ( -camera1.rect[ 0 ] + int(items_file1[i].split(',')[0]) , -camera1.rect[ 1 ] + int(items_file1[i].split(',')[1] ) ) )
        
        for i in range(len(Plants_file1)) :
                if camera1.rect[0] + int(screen_width) - fov >= int(Plants_file1[i].split(',')[0]) and camera1.rect[1] + int(screen_height) - fov >= int(Plants_file1[i].split(',')[1]) : screen.blit( Plants_file1[ i ] , ( -camera1.rect[ 0 ] + int(Plants_file1[i].split(',')[0]) , -camera1.rect[ 1 ] + int(Plants_file1[i].split(',')[1] ) ) )

        interface_surf.set_alpha(50)
        quests_surf.set_colorkey(( 0 , 0 , 0 ))

        screen.blit( hero_image, (hero_x, hero_y ))
        screen.blit(rot_hero, (500,200))

        screen.blit(scaled_image, (550,200 ))

        screen.blit( enemy.image , ( -camera1.rect[0] + enemy.x , -camera1.rect[1] + enemy.y ))
        
        #fuel_bar(green color)
        pg.draw.line( screen , (0 , 255 , 0) , (400 , 400) , ( 400 + fuel_bar_width * -math.cos(fuel) , 400 + fuel_bar_width * -math.sin(-fuel)) , 1)


        if show_interface == 1:
            for i in range(len(hero_inventory_file1)):
                pg.draw.rect(screen , ( cell_color)           , ( int(screen_width) / 2 - cell_size * i     + cell_size , int(screen_height) - cell_size , cell_size , cell_size ) , 2 , 0 , button_border_radius , button_border_radius , button_border_radius , button_border_radius ) #drawing a inventory cells
                pg.draw.rect(screen , ( Button_frame_color  ) , ( int(screen_width) / 2 - cell_size * item  + cell_size , int(screen_height) - cell_size , cell_size , cell_size ) , 2 , 0 , button_border_radius , button_border_radius , button_border_radius , button_border_radius) #drawing a inventory cell_frame for a selected item in inventory
            
            if len(hero_inventory)  != 0 : screen.blit(hero_inventory[item] , (int(screen_width ) / 2 , int(screen_height) - cell_size * 2  )) #drawing a title of the item in inventory
    
            dark_surf.fill(dark_surf_color) ; dialoge_surf.fill((0 , 0 , 0 )) ; dark_surf.set_alpha(dark_level) ; screen.blit(dark_surf , ( 0 , 0 )) 

            screen.blit(hero_shadow_surf  , ( (hero_x) , (hero_y + hero_image1.get_height() ) ))
            
            pg.draw.circle(hero_shadow_surf , (10 , 0 , 0)  , ( 50 , 50 ),50) 

            hero_shadow_surf.set_colorkey((0,0,0))

            hero_shadow_surf.set_alpha(100)
            
            screen.blit(interface_surf , ( interface_surf_x , interface_surf_y ))
            screen.blit(quests_surf   , ( int(screen_width) - quests_surf.get_width() , int(screen_height ) - quests_surf.get_height() ))

            
            quests_surf.fill((quest_surf_color))
                
            #drawing a road to the checkpoint
           # pg.draw.line(screen   , (0   , 0 , 0 ) ,    [ -camera.rect[0] + int(camera_x) + int(screen_width) / 2 + hero_checkpoint_offset_x , -camera.rect[ 1 ] + int(camera_y) + int(screen_height) / 2 + 100 + hero_checkpoint_offset_y ] , [ -camera.rect[ 0 ] + int(checkpoints_file1[0].split(',')[0]) , -camera.rect[ 1 ] + int(checkpoints_file1[0].split(',')[1])] , 1 )
                
            #segmented road to the checkpoint 
            #for i in range(int(calc_dist) // 10 )  : pg.draw.circle(screen , (255 , 0 , 0) , ( -camera.rect[0] + int(checkpoints_file1[0].split(',')[0]) + i * 10 , -camera.rect[1] + int(checkpoints_file1[0].split(',')[1]) - i * 10) , 1)        
                
            #drawing a circle at the hero x and hero y
            #if vihicle_sit == 0 : pg.draw.circle(screen , (255 , 0 , 0) , ( -camera.rect[0] + int(camera_x) + int(screen_width) / 2 + hero_checkpoint_offset_x , -camera.rect[1] + int(camera_y) + int(screen_height) / 2 + 100 + hero_checkpoint_offset_y) , checkpoint_size / 2 , 1 )
                
            #drawing a circle at the checkpoint x and checkpoint y
            #33pg.draw.circle(screen , (255 , 0 , 0)  , ( -camera.rect[0] + int(checkpoints_file1[0].split(',')[0]) , -camera.rect[1] + int(checkpoints_file1[0].split(',')[1])) , checkpoint_size , 1 )
            
            draw_mini_map()

            if map_size == min_map_size  and vihicle_sit == 1 :
                
                pg.draw.line( screen , (0 , 255 , 0) , (400 , 400) , ( 400 + fuel_bar_width * -math.cos(fuel) , 400 + fuel_bar_width * -math.sin(-fuel)) , 1)
                screen.blit(  show_fuel , ( 0 , int(screen_height ) - 250))
                fuel_values = pg.draw.circle(screen , (255 , 0 , 0)  , ( 100 , screen_height - 100 , checkpoint_size , 1 ))
           




            screen.blit( cancel_icon , ( cancel_icon_x , cancel_icon_y))
            
            screen.blit(show_health     , ( bigfont + 10 , int(screen_height ) - bigfont * 6)) , screen.blit(health_icon     , ( 10 , int(screen_height ) - bigfont * 6))
            screen.blit(show_hero_armor , ( bigfont + 10 , int(screen_height ) - bigfont * 5)) , screen.blit(armor_icon      , ( 10 , int(screen_height ) - bigfont * 5))
            screen.blit(show_ammo       , ( bigfont + 10 , int(screen_height ) - bigfont * 4)) , screen.blit(ammo_icon       , ( 10 , int(screen_height ) - bigfont * 4))
            screen.blit(show_radiation  , ( bigfont + 10 , int(screen_height ) - bigfont * 3)) , screen.blit(radiation_icon  , ( 10 , int(screen_height ) - bigfont * 3))
            screen.blit(show_energy     , ( bigfont + 10 , int(screen_height ) - bigfont * 2)) , screen.blit(energy_icon     , ( 10 , int(screen_height ) - bigfont * 2))
            screen.blit(show_money      , ( 10           , int(screen_height ) - bigfont))
            



        

            for x in range( int(map_width / km)) :
                for y in range( int(map_height / km)) : pg.draw.rect(screen , (255,0,0) , (  -camera1.rect[0] + meter * km * x  , -camera1.rect[1] + meter * km * y , km, km),2,0)   

run = True ; logging.info( msg = 'GAME STARTED!' )


for i in screen_file1:
        screen_width , screen_height , camera_x , camera_y = i.split(',')[0] , i.split(',')[1] , i.split(',')[2] , i.split(',')[3]

bg_num     = 1 ; wallpapers_dir = os.listdir('Wallpapers/' + str(screen_width) + '_' + str(screen_height) + '/') ; wallpaper  = wallpapers_dir[bg_num]
hero_x , hero_y     = int(screen_width) / 2  - heroimage.width / 2 , int(screen_height)  / 2 - heroimage.height / 2


while run :

    for i in enumerate(screen_surfs_list):
        print(f"screen surf : {i}")



        
    if dark_level <= max_dark_level : dark_level += 0.01 ; clock.tick(FPS / fps_1)
    
    vector = [ 0 , 0]

    for event in pg.event.get() :
        if event.type == pg.MOUSEMOTION : pos = pg.mouse.get_pos()
        pg.display.update()

        if event.type == pg.MOUSEMOTION :
            pos = pg.mouse.get_pos()
            pg.display.update()


 



        """
                #список доступных джойстиков
                joystick_count = pg.joystick.get_count()
                print(f"Найдено джойстиков: {joystick_count}")

                if joystick_count > 0:
                    joystick = pg.joystick.Joystick(0)
                    joystick.init()
                print(f"Использую: {joystick.get_name()}")


        """
        # кнопки

        if event.type == pg.JOYBUTTONDOWN:
            print(f"{event.button}")
            if event.button == 0:
                if welcome_num  < len(welcome_speech_dir) - 1 :

                    welcome_num += 0.5
                            
                else:
                    welcome_num = 0
                                
                    welcome = pg.mixer.Sound(f'Audio/speech/langs/{language}/welcome/{int(welcome_num)}.mp3')

                welcome.play()



        if event.type == pg.MOUSEBUTTONDOWN:
            
            #shooting
            if event.button == 1 and int(ammo) > 0  and int(ammo) <= max_ammo and game_state == 'Play' and map_size == min_map_size :
                ammo -= 1
                gun_shot = pg.mixer.Sound( 'Audio/sounds/firegun/single/0.mp3' )
                gun_shot.play()
                show_hero_armor = big_font.render('armor : ' + str(armor).strip() + " / " + str( max_armor).strip() , False , ( 250 , 0 , 0 ) )
                show_ammo = big_font.render('ammo : ' + str(ammo).strip() + " / " + str(max_ammo * mags).strip() , False , ( 250 , 0 , 0 ) )
                show_health = big_font.render('health : ' + str(health).strip() + " / " + str(max_health).strip() , False , ( 255 , 0 , 0 ) )
                show_radiation  = big_font.render('radiation : ' + str(radiation).strip() + " / " + str(max_radiation).strip() , False , ( 255 , 0 , 0 ) )
                hero            = 'Objects/Characters/Hero/'     + str(name) + '/' + str(state) + '/' + str(turn) + '/' + str(animation) + '.png'
                hero_x , hero_y = int(screen_width) / 2  - heroimage.width / 2 , int(screen_height)  / 2 - heroimage.height / 2

            if event.button     == 1 and int(ammo) <= 1 and game_state == 'Play' and map_size == min_map_size :
                show_hero_armor = big_font.render('armor : ' + str(armor).strip() + " / " + str( max_armor).strip() , False , ( 250 , 0, 0  ) ) ; show_ammo = big_font.render('ammo : ' + str(ammo).strip() + " / " + str(max_ammo * mags).strip() , False , ( 250 , 0 , 0 ) ) ; show_health = big_font.render('health : ' + str(health).strip() + " / " + str(max_health).strip() , False , ( 255 , 0 , 0 ) ) ; show_radiation  = big_font.render('radiation : ' + str(radiation).strip() + " / " + str(max_radiation).strip() , False , ( 255 , 0 , 0 ) )
                ammo -= 1 ; gun_shot = pg.mixer.Sound( 'Audio/sounds/firegun/single/0.mp3' ) ; gun_shot.play()

            if event.button == 1 and pos[0] >= cancel_icon_x and pos[0] <= cancel_icon_x + cancel_icon.get_width() and pos[1] >= cancel_icon_y and pos[1] <= cancel_icon_y + cancel_icon.get_height() and game_state == 'Play' and vihicle_sit == 1:
                vihicle_sit =  0

            if event.button == 3 and pos[0] >= hero_x and pos[0] <= hero_x + hero_image.get_width() and pos[1] >=  hero_y and pos[1] <= hero_y + hero_image.get_height() and open_backpack == 0 and game_state == 'Play':                
                game_state = 'Backpack'
            

            for i in range(len(Companions_file1)):
                i_pos    = int(Enemies_file1[i].split(',')[0]) , int(Enemies_file1[i].split(',')[1])
                i_hitbox = int(Enemies_file1[i].split(',')[0]) + 100 , int(Enemies_file1[i].split(',')[1]) + 200

                if event.button == 3 and i_pos[0] < i_hitbox[0] and i_pos[1] < i_hitbox[1]  :

                                                
                        if welcome_num  < len(welcome_speech_dir) - 1 :

                            welcome_num += 0.5
                            
                        else:
                                welcome_num = 0
                                
                        welcome = pg.mixer.Sound(f'Audio/speech/langs/{language}/welcome/{int(welcome_num)}.mp3')

                        welcome.play()


            
            enemypos    = int(Enemies_file1[0].split(',')[0]) , int(Enemies_file1[0].split(',')[1])
            enemyhitbox = int(Enemies_file1[0].split(',')[0]) + 100 , int(Enemies_file1[0].split(',')[1]) + 200

            if enemypos[0] < enemyhitbox[0] and enemypos[1] < enemyhitbox[1]  :
                print(f"enemy pos  = {enemypos} ,enemy hitbox = {enemyhitbox}")
                print(f"lower,enemy pos 0 = {Enemies_file1[0].split(',')[0]} ,enemy pos 1 = {Enemies_file1[0].split(',')[1]}")


            for i in range(len(vihicles_file1)):
                if event.button == 3 and  pos[0] >=  -camera1.rect[0] + int(vihicles_file1[i].split(',')[0])  and pos[0] <=  -camera1.rect[0] + int(vihicles_file1[i].split(',')[0]) + vihicles_images_list[i].get_width() and pos[1] >=  -camera1.rect[1] + int(vihicles_file1[i].split(',')[1]) and pos[1] <=  -camera1.rect[1] + int(vihicles_file1[i].split(',')[1]) + vihicles_images_list[i].get_height() and vihicle_sit == 0:
                    vihicle_sit = 1 ; camera1.rect[0] = int(vihicles_file1[i].split(',')[0]) - int(screen_width) / 2 ; camera1.rect[1] = int(vihicles_file1[i].split(',')[1]) - int(screen_height) / 2 ; hero_image = vihicles_images_list[i]
            
            if map_size == min_map_size :  
                if event.button == 4  and item >= 0: item -= 1 ; click_sound.play()
                if event.button == 5  and item <= len(hero_inventory_file1) - 3 : item += 1 ; click_sound.play()

            #button 4 or 5 = mouse_wheel_scrolling button 1 = left mouse button button 3 = right mouse button 
            if game_state == 'Main menu':
                if event.button == 1:
                    if active_button == 0 : spawn_sound.play() ; pg.display.update();game_state = 'Play' 



            if game_state == 'Play' :
                if event.button == 2 : game_state = 'Trade menu' ; print('active buton ', active_button) ; click_sound.play()
                if map_size == max_map_size :  
                        if event.button == 4 : map_scale -= 0.1 ; draw_mini_map()
                        minimapfontsize = int( 30 / map_scale)
                        mini_map_font_size = pg.font.SysFont(font_name , minimapfontsize) 
                        custom_checkpoint_title = mini_map_font_size.render('Custom checkpoint'    , False , small_font_color ) 

                        if event.button == 5 : map_scale += 0.1 ; draw_mini_map()
                        minimapfontsize = int( 30 / map_scale)
                        mini_map_font_size = pg.font.SysFont(font_name , minimapfontsize) 
                        custom_checkpoint_title = mini_map_font_size.render('Custom checkpoint'    , False , small_font_color ) 
                
            #if dialoge_started  == 1 and action_counter == 0 : spawn_sound.play()

            #f event.button == 1:
                        if action_counter == 2 : game_state = 'Trade menu' ;dialoge_started = 0 ; spawn_sound.play() 
                        if action_counter == 3 : game_state = 'Crafting'   ; dialoge_stated = 0 ; spawn_sound.play() 
                        if action_counter == 4 : dialoge_started = 0
                    
            #if event.button == 4  and action_counter >= 1 : action_counter -= 1 ; click_sound.play()
            #if event.button == 5  and action_counter <= len(actions_list)  - 2  : action_counter += 1 ; click_sound.play()



            if game_state == 'character select menu':
                if event.button == 0 : game_state = 'Play' ; print('game state : ', game_state ) ; click_sound.play()
                if event.button == 4 and active_button >= 1 : active_button -= 1 ; click_sound.play() ; print('active buton ', active_button)
                if event.button == 5  and active_button <= len(Hero_types) - 2 : active_button += 1 ; click_sound.play() ; print('active buton ' , active_button)



            if game_state == 'Trade menu':
                if event.button == 4 and pos[0]<= int(screen_width) / 2 and active_button  >= 1 : active_button -= 1 ; click_sound.play() ; print('active buton ', active_button) 
                
                if event.button == 4 and pos[0]>= int(screen_width) / 2 and active_button1 >= 1 : active_button1 -= 1 ; click_sound.play() ; print('active buton ', active_button) 



                if event.button == 5 and pos[0]<= int(screen_width) / 2 and active_button  <= len(menu_titles1) - 2 : active_button += 1 ; click_sound.play() ; print('active buton ' , active_button) 
            
                if event.button == 5 and pos[0]>= int(screen_width) / 2 and active_button1 <= len(menu_titles1) - 2 : active_button1 += 1 ; click_sound.play() ; print('active buton1 ' , active_button1) 
            


            if game_state == 'Saves':
                if event.button == 1 and active_button == 1 : game_state = 'game mode select' ; click_sound.play()
                if event.button == 4 and active_button == 3 and active_button1  >= 1 and pos[0] >= int(screen_width) / 2 : active_button1 -= 1 ; click_sound.play() 
                if event.button == 5 and active_button == 3 and active_button1  <= len(menus_dir) -2 and pos[0] >= int(screen_width) / 2 : active_button1 += 1 ; click_sound.play()
            


            if game_state == 'game mode select':
                if event.button == 1 and active_button   == 0 : game_state = 'Select a difficulty' ; click_sound.play()

                if event.button == 4 and active_button1  >= 1 and pos[0] >= int(screen_width) / 2 : active_button1 -= 1 ; click_sound.play() 

                if event.button == 5 and active_button1  <= len(menus_dir) -2 and pos[0] >= int(screen_width) / 2 : active_button1 += 1 ; click_sound.play()
            


            if game_state == 'Select a difficulty':

                if event.button == 1 and active_button  == 0 : game_state = 'Play' ; click_sound.play()

                if event.button == 4 and active_button1 >= 1 and pos[0] >= int(screen_width) / 2 : active_button1 -= 1 ; click_sound.play() 

                if event.button == 5 and active_button1 <= len(menus_dir) -2 and pos[0] >= int(screen_width) / 2 : active_button1 += 1 ; click_sound.play()



            if game_state == 'Backpack':
                if event.button == 1 and active_button == 1 : game_state = 'Play' ; click_sound.play()
                if event.button == 4 and active_button >= 1 and pos[0] >= int(screen_width) / 2 : active_button -= 1 ; click_sound.play() 
                if event.button == 5 and active_button <= len(menus_dir) -2 and pos[0] >= int(screen_width) / 2 : active_button += 1 ; click_sound.play()



            if game_state == 'Settings':
                if event.button == 1 : click_sound.play()
                
                if event.button == 1 and pos[0] >= int(screen_width) / 2 : text_updating()

                if event.button == 3 : game_state = 'Main menu' ; click_sound.play() ; active_button = 0
                


                if event.button == 4 and active_button  >= 1 and pos[0] <= int(screen_width) / 2 : active_button -= 1 ; click_sound.play()
                
                if event.button == 4 and active_button1 >= 1 and pos[0] >= int(screen_width) / 2 : active_button1 -= 1 ; click_sound.play()
                
                if event.button == 4 and active_button  == 3 and active_button1  >= 1 and pos[0] >= int(screen_width) / 2 : active_button1 -= 1 ; click_sound.play() 



                if event.button == 5 and active_button  <= len(settings_file1) -2 and pos[0] <= int(screen_width) / 2 : active_button += 1 ; click_sound.play()
                
                if event.button == 5 and active_button1  <= len(settings_file1) -2 and pos[0] >= int(screen_width) / 2 : active_button1 += 1 ; click_sound.play()

                if event.button == 5 and active_button == 3 and active_button1  <= len(menus_dir) -2 and pos[0] >= int(screen_width) / 2 : active_button1 += 1 ; click_sound.play()


    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False


    keys = pg.key.get_pressed()
    
    
    player_movement()

    if game_state == 'Play':
        if keys[pg.K_e] and vihicle_sit == 1 : Open_unit_inventory()
        if keys [pg.K_ESCAPE]   and open_backpack == 1: open_backpack  = 0
        if keys [reload_btn] and mags >= 1 : reloadsound = pg.mixer.Sound( 'Audio/sounds/firegun/reload.mp3' ) ; reloadsound.play() ; mags -= 1 ; hero_file_name = 'txt/hero.txt' ; hero_file_mode = 'w' ; hero_file = open (hero_file_name , hero_file_mode) ; hero_file.write(str(mags)) ; hero_file.write(str(health)) ; hero_file.write(str(health)) ; hero_file.write(str(health)) ; hero_file.write(str(mags)) ; hero_file.write(str(mags)) ; hero_file.close() ; ammo = max_ammo ; show_ammo  = big_font.render(str(ammo) + " / "  + str( ammo * mags ) , False , colors[2] ) ; show_armor = big_font.render(str(armor).strip() + " / "  + str( max_armor ).strip() , False , ( 250 , 0, 0 ) ) ; show_health    = big_font.render(str(health).strip()     + " / "  + str( max_health ).strip() , False , ( 255 , 0 , 0 ) ) ; show_radiation = big_font.render(str(radiation ).strip() + " / "  + str( max_radiation ).strip() , False , ( 255 , 0 , 0 ) ) ; cursor = pg.image.load( 'Interface/icons/refresh_icon.png' ) ; pg.display.update()
        if keys [screenshot_btn ] : make_screenshot() ; logging.info( msg = 'SCREENSHOT SAVED!') ; print('Screenshot saved ! ')

        if keys [pg.K_f] : fuel += 0.1 ; show_fuel = big_font.render('Fuel  : ' + str(fuel)    , False , small_font_color ) ; print('Fuel : ' , fuel)
        
        if keys [pg.K_g  ] and keys[pg.K_LCTRL]  : toggle_god_mode() ;  spawn_sound.play() #GOD MODE - no damage , no limit etc
    if keys[back_btn]  : bg_image = bg_images[ random.randint( 0 , len(bg_images) - 1 ) ] ; game_state = 'Main menu'

    mini_map_keyboard_controls()
    
    mini_map_surf.fill((minimapBGcolor))
    screen.fill( (BGcolor) )
    

    start()
    
    mouse_visible = False ; cursor = pg.image.load( 'Interface/icons/Select/0.png' ) ; screen.blit( cursor , ( pos[ 0 ] - mouse_horizontal_offset , pos[ 1 ]  - mouse_vertical_offset )) ; #calc_dist = math.sqrt( (( x_2_list - x_1_list   * hero_checkpoint_offset_x) ** 2 ) +  ( (  y_2_list - y_1_list * hero_checkpoint_offset_y) ** 2 ) /100) ; show_distance = small_font.render('Distance : ' + str(int(calc_dist) /100) + ' m' , False , small_font_color )
    
    if game_state != 'Play' : show_game_state = big_font.render(str(game_state) , False , small_font_color) ; screen.blit( show_game_state ,  (game_state_x , game_state_y))
    
    for i in range(len(main_menu_file1)):
        if game_state == 'Main menu' and pos[0] >= int(screen_width) / 2 - button_width / 2  and pos[0] <= int(screen_width) /  2 + button_width / 4 and pos[1] >= int(screen_height) / 2 - int(screen_height) / 4 - bigfont + i * 40 + bigfont / 2  and pos[1] <= int(screen_height) / 2 - int(screen_height) / 4 - bigfont + i * 40 + bigfont / 2 + button_height : active_button = i
        
    for i in range(len(menus_dir)):
        if game_state == 'Crafting'  and pos[0] >= int(screen_width) / 2 - button_width / 2  and pos[0] <= int(screen_width) /  2 + button_width / 4 and pos[1] >= int(screen_height) / 2 - int(screen_height) / 4 - bigfont + i * 40 + bigfont / 2  and pos[1] <= int(screen_height) / 2 - int(screen_height) / 4 - bigfont + i * 40 + bigfont / 2 + button_height : active_button = i

    for i in range(len(saves_file1)):
        if game_state == 'Saves'     and pos[0] >= int(screen_width) / 2 - button_width / 2  and pos[0] <= int(screen_width) /  2 + button_width / 4 and pos[1] >= int(screen_height) / 2 - int(screen_height) / 4 - bigfont + i * 40 + bigfont / 2  and pos[1] <= int(screen_height) / 2 - int(screen_height) / 4 - bigfont + i * 40 + bigfont / 2 + button_height : active_button = i
        
    for i in range(len(Hero_types)):
        if game_state == 'character select menu' and pos[0] >= int(screen_width) / 2 - button_width / 2  and pos[0] <= int(screen_width) /  2 + button_width / 4 and pos[1] >= int(screen_height) / 2 - int(screen_height) / 4 - bigfont + i * 40 + bigfont / 2  and pos[1] <= int(screen_height) / 2 - int(screen_height) / 4 - bigfont + i * 40 + bigfont / 2 + button_height : active_button = i
        
    for i in range(items_max):    
        if game_state == 'Trade menu' and pos[0] >= int(screen_width) / 2 - button_width and pos[0] <= int(screen_width) /  2 + button_width / 4 and pos[1] >= int(screen_height) / 2 - int(screen_height) / 4 - bigfont + i * 40 + bigfont / 2  and pos[1] <= int(screen_height) / 2 - int(screen_height) / 4 - bigfont + i * 40 + bigfont / 2 + button_height : active_button = i
        
    for i in range(len(game_modes1)):
        if game_state == 'game mode select' and pos[0] >= int(screen_width) / 2 - button_width / 2  and pos[0] <= int(screen_width) /  2 + button_width / 4 and pos[1] >= int(screen_height) / 2 - int(screen_height) / 4 - bigfont + i * 40 + bigfont / 2  and pos[1] <= int(screen_height) / 2 - int(screen_height) / 4 - bigfont + i * 40 + bigfont / 2 + button_height : active_button = i
    
    for x in range(minimap_grid_width):
        for y in range(minimap_grid_height):
            pg.draw.rect(mini_map_surf , (cell_color) , ( cell_size * x , cell_size * y , cell_size , cell_size ) , 2 , 0 , button_border_radius , button_border_radius , button_border_radius , button_border_radius ) #drawing a inventory cells



    pg.display.update()




    """

import mido

# список доступных входов
print("Доступные устройства MIDI:")
print(mido.get_input_names())

# выбираем устройство
port_name = mido.get_input_names()[0]  # можно выбрать по индексу или строке
with mido.open_input(port_name) as inport:
    print(f"Слушаю {port_name}...")
    for msg in inport:
        print(msg)





   import pygame

# инициализация
pygame.init()
pygame.joystick.init()

# список доступных джойстиков
joystick_count = pygame.joystick.get_count()
print(f"Найдено джойстиков: {joystick_count}")

if joystick_count > 0:
    joystick = pygame.joystick.Joystick(0)
    joystick.init()
    print(f"Использую: {joystick.get_name()}")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # кнопки
        if event.type == pygame.JOYBUTTONDOWN:
            print(f"Нажата кнопка {event.button}")
        if event.type == pygame.JOYBUTTONUP:
            print(f"Отпущена кнопка {event.button}")

        # оси (стики, триггеры)
        if event.type == pygame.JOYAXISMOTION:
            print(f"Ось {event.axis} = {event.value:.2f}")

        # крестовина (hat)
        if event.type == pygame.JOYHATMOTION:
            print(f"Крестовина = {event.value}")
     
            
import pyaudio

p = pyaudio.PyAudio()

for i in range(p.get_device_count()):
    info = p.get_device_info_by_index(i)
    print(i, info["name"])


"""




                
                #for i in range(len(menu_titles)) : i = big_font.render(menu_titles[i].split(',')[0].strip() , False , small_font_color ) ; menu_titles1.append(i)   

                #vector[1] -= hero_speed
                #vector[1] += hero_speed
                #calc_dist = math.sqrt( (( x_2_list - x_1_list - hero_checkpoint_offset_x) ** 2) + ((y_2_list - y_1_list - hero_checkpoint_offset_y) ** 2 ))

                #calc_dist = math.sqrt( (( x_2_list - x_1_list - hero_checkpoint_offset_x) ** 2 ) +  ( (  y_2_list - y_1_list - hero_checkpoint_offset_y) ** 2 ))
                #calc_dist = math.sqrt( (( x_2_list - x_1_list - hero_checkpoint_offset_x) ** 2 ) +  ( (  y_2_list - y_1_list - hero_checkpoint_offset_y) ** 2 ))
                #calc_dist = math.sqrt( (( x_2_list - x_1_list - hero_checkpoint_offset_x) ** 2 ) +  ( (  y_2_list - y_1_list - hero_checkpoint_offset_y) ** 2 ))
                

    # Обновление расстояния до цели
    #calc_dist = math.sqrt(((x_2_list - x_1_list - hero_checkpoint_offset_x) ** 2) +((y_2_list - y_1_list - hero_checkpoint_offset_y) ** 2))
    #show_distance = small_font.render(f'Distance : {calc_dist / 100} m', False, small_font_color)
    
    #if blit_distance == 1 and map_size == min_map_size : screen.blit(show_distance , ( hero_x , hero_y - bigfont ) )
    #hero_x and hero_y
    #x_1_list =  -camera.rect[ 0 ] + int(camera_x) + int(screen_width) / 2 + hero_checkpoint_offset_x ; y_1_list =  -camera.rect[ 1 ] + int(camera_y) + int(screen_height) / 2 + 100 + hero_checkpoint_offset_y ; x_2_list =  -camera.rect[ 0 ] + int(checkpoints_file1[checkpoint_num ].split(',')[0]) ; y_2_list =  -camera.rect[ 1 ] + int(checkpoints_file1[checkpoint_num ].split(',')[1]) #checkpoint_x andd checkpoint_y
    #distances = [] ; distance_num = 0 ; calc_dist = math.sqrt( (( x_2_list - x_1_list * hero_checkpoint_offset_x) ** 2) +  ((y_2_list - y_1_list * hero_checkpoint_offset_y) ** 2 ) // meter) ; show_distance  = small_font.render('Distance : ' + str(int(calc_dist) // meter) + ' m' , False , small_font_color ) ; blit_action = 0 ; blit_distance  = 0
    """
    for i in range(len(langs_file1))     : i = big_font.render(langs_file1[i].strip()  , False , small_font_color ) ; langs_list.append(i)
    for i in range(len(dialoges_file1))  : i = small_font.render(dialoges_file1[i].strip() , False , small_font_color ) ; dialoges_list.append(i) 
    for i in range(len(actions_file1))   : i = small_font.render(str(actions_file1[i]).strip()  , False , small_font_color ) ; actions_list.append(i)
    for i in range(len(actions_list))    : i = small_font.render(str(actions_list[i] ).strip()  , False , small_font_color ) ; actions_list.append(i)
    for i in range(len(crafts_file1))    : i = big_font.render(crafts_file1[i].strip()  , False , small_font_color ) ; crafts_list.append(i)
    for i in range(len(quests_file1))    : i = small_font.render(quests_file1[i].split(',')[0].strip()  , False , small_font_color ) ; quests_list.append(i)
    for i in range(len(quests_file1))    : i = small_font.render(quests_file1[i].split(',')[1].strip()  , False , small_font_color ) ; quests_states_list.append(i)
    for i in range(len(main_menu_file1)) : i = big_font.render(main_menu_file1[i].strip()  , False , small_font_color ) ; main_menu.append(i)
    for i in range(len(settings_file1))  : i = big_font.render(settings_file1[i].strip() , False , small_font_color ) ; settings.append(i)
    for i in range(len(hero_inventory_file1)) : i = big_font.render(hero_inventory_file1[i].split(',')[0].strip()          , False , small_font_color ) ; hero_inventory.append(i)     

    """     
        

        
        #if keys [load_game_btn  ] : load_game() #load game
        #if keys [save_game_btn  ] : save_game() #save game
        #for i in range(len(Companions_file1)) :  
    #    if game_state == 'Play' and dialoge_started == 1 and pos[0] >=  -camera.rect[0] + int(Companions_file1[i].split(',')[0])  and \
    #        pos[0] <= -camera.rect[0] + int(Companions_file1[i].split(',')[0]) + Companions_images_list[i].get_width() and\
    #              pos[1] >=  -camera.rect[1] + int(Companions_file1[i].split(',')[1])  and pos[1] <=  -camera.rect[1] + int(Companions_file1[i].split(',')[1]) +  Companions_images_list[i].get_height():
            
    #for i in range(len(actions_file1)) :
    #             dialoge_surf.blit(actions_list[i] , ( 10 , 10 + i * 20  ))
    #             frame = pg.draw.rect(dialoge_surf , ( Button_frame_color ) , (10 , 10 + action_counter  * 20 , 90 , 20 ) , 2 , 2 )
    #             screen.blit(dialoge_surf , (hero_x , hero_y - 150  ))




            
            #if event.button == 3 :
            #    print(enemy.health)
            #    enemy.take_damage(1)
            #    print(enemy.health)
            #    if enemy.health <= 0:
            #        enemy.respawn()
            #        enemy.update_image('Objects/Characters/Enemies/Ghosts/1/idle/right/0.png')


        #screen.blit( hero_image , ( hero_x , hero_y ) )

            #if keys [pg.K_h] : fuel += 0.1 ; show_fuel = big_font.render('Fuel  : ' + str(fuel)    , False , small_font_color ) ; print('Fuel : ' , fuel)

        #if keys [pg.K_f] : fuel_bar_width += 10 ; print('Fuel bar width : ' , fuel_bar_width)
        #if keys [pg.K_g] : fuel_bar_width -= 10 ; print('Fuel bar width : ' , fuel_bar_width)

                    #if keys[pg.K_a] and camera.rect[0] >= 0 and camera.rect[1] >= 0 : state = 'go' ; turn  = 'left'; hero_speed = 4 ; vector[0] -= hero_speed ; hero_checkpoint_offset_x -= hero_speed;calc_dist = math.sqrt( (( x_2_list - x_1_list - hero_checkpoint_offset_x) ** 2 ) +  ( (  y_2_list - y_1_list - hero_checkpoint_offset_y) ** 2 ));show_distance    = small_font.render('Distance : ' + str(int(calc_dist) /100) + ' m' , False , small_font_color ) ; minimap_object_offset += 1 / (map_scale * hero_speed * 10)
            #if keys[pg.K_d] and camera.rect[0] <= map_width and camera.rect[1] >= 0 : state = 'go' ; turn = 'right' ; hero_speed = 4 ;vector[ 0 ]  += hero_speed ; hero_checkpoint_offset_x += hero_speed ; calc_dist = math.sqrt( (( x_2_list - x_1_list - hero_checkpoint_offset_x) ** 2 ) +  ( (  y_2_list - y_1_list - hero_checkpoint_offset_y) ** 2 )) ; show_distance = small_font.render('Distance : ' + str(int(calc_dist) /100) + ' m' , False , small_font_color ) ; minimap_object_offset -= 1 / (map_scale * hero_speed * 10)  #hero_image =  pg.image.load(hero) ; heroimage = Image.open(hero) ; hero_x , hero_y = int(screen_width) / 2  - heroimage.width / 2 , int(screen_height)  / 2 - heroimage.height / 2
            
            #if keys[pg.K_w] and camera.rect[0] >= 0 and camera.rect[1] >= 0 :vector[1] -= hero_speed ; hero_checkpoint_offset_y -= hero_speed ; calc_dist = math.sqrt( (( x_2_list - x_1_list - hero_checkpoint_offset_x) ** 2 ) +  ( (  y_2_list - y_1_list - hero_checkpoint_offset_y) ** 2 )) ; show_distance = small_font.render('Distance : ' + str(int(calc_dist) /100) + ' m' , False , small_font_color ) ; minimap_object_offset1 += 1 / (map_scale * hero_speed * 10)
            #if keys[pg.K_s] and camera.rect[0] >= 0 and camera.rect[1] >= 0 : vector[ 1 ]   += hero_speed ; hero_checkpoint_offset_y += hero_speed; hero_x , hero_y = int(screen_width) / 2  - heroimage.width / 2 , int(screen_height)  / 2 - heroimage.height / 2 ; calc_dist = math.sqrt( (( x_2_list - x_1_list - hero_checkpoint_offset_x) ** 2) + ((y_2_list - y_1_list - hero_checkpoint_offset_y) ** 2 )) ; show_distance = small_font.render('Distance : ' + str(int(calc_dist) /100) + ' m' , False , small_font_color ) ; minimap_object_offset -= 1 / (map_scale * hero_speed * 10)
            

                #pg.draw.rect(screen    , (100 , 50 , 0) , ( -camera.rect[0] + meter * 30 , -camera.rect[1] + meter * 30 , km * 5 , km * 5  ))


                #[ ( 3  * meter) * -math.cos(fuel)  * i / 3 , (3 * meter) + meter * -math.sin(fuel ) * i / 3]
                    #hero_shadow_surf.set_colorkey(( 0 , 0 , 0 ))

        #hero_shadow_surf.set_alpha(50) 

        #hero_shadow = pg.draw.circle(hero_shadow_surf , (0 , 0 , 0)  , (  hero_x + hero_image.get_width() / 2 , hero_y + hero_image.get_height()) , 10)
        
        #print('map width(km) : ' , int(map_width / km) , 'map height(km) : ' , int(map_height / km) , 'map box width  and height: ' , int(map_width / km) , ' , ' , int(map_height / km) )

            
    
                #for i in range( len ( fuel_values_list ) ) :
            #    screen.blit(fuel_values_list1[i] , ( 400 + fuel_bar_width * -math.cos(-fuel)  * i / 3 , 400 + fuel_bar_width * -math.sin(-fuel ) * i / 3 ))
            
            #for i in range(len(hero_belt_inventory_images)) : screen.blit( hero_belt_inventory_images[i] , ( int(screen_width) / 2 - cell_size * i + 10  + cell_size , int(screen_height) - cell_size / 2 - items_images[i].get_height() / 2 ) )
            #pg.draw.rect(screen , (Button_frame_color) , ( 400 + fuel_bar_width * 2  * -math.cos(-fuel) , 400 + fuel_bar_width * 2  * -math.sin(-fuel ), 40 , 40 ))

                    #fog                  = pg.draw.rect(screen   , (Button_color) , (-camera.rect[ 0 ] + int(screen_width) /  2 - button_width / 2 + 600 , -camera.rect[ 1 ] + int(screen_height) / 2 - int(screen_height) / 4 - bigfont + 0 * 40 + bigfont /2 , button_width , bigfont + 5 ) , 0 , 0 , button_border_radius , button_border_radius , button_border_radius , button_border_radius)            
        #acid_cloud           = pg.draw.rect(screen   , (Button_color) , (-camera.rect[ 0 ] + int(screen_width) /  2 - button_width / 2 , -camera.rect[ 1 ] + int(screen_height) / 2 - int(screen_height) / 4 - bigfont + 0 * 40 + bigfont /2 , button_width , bigfont + 5 ) , 0 , 0 , button_border_radius , button_border_radius , button_border_radius , button_border_radius)            
        #burst                = pg.draw.circle(screen , (255 , 0 , 0)  , ( -camera.rect[0] + int(checkpoints_file1[0].split(',')[0]) , -camera.rect[1] + int(checkpoints_file1[0].split(',')[1])) , checkpoint_size , 1 )
        #damage_effect        = pg.draw.circle(screen , (255 , 0 , 0)  , ( -camera.rect[0] + int(checkpoints_file1[0].split(',')[0]) , -camera.rect[1] + int(checkpoints_file1[0].split(',')[1])) , checkpoint_size , 1 )
        #heal_effect          = pg.draw.circle(screen , (255 , 0 , 0)  , ( -camera.rect[0] + int(checkpoints_file1[0].split(',')[0]) , -camera.rect[1] + int(checkpoints_file1[0].split(',')[1])) , checkpoint_size , 1 )
        #death_effect         = pg.draw.circle(screen , (255 , 0 , 0)  , ( -camera.rect[0] + int(checkpoints_file1[0].split(',')[0]) , -camera.rect[1] + int(checkpoints_file1[0].split(',')[1])) , checkpoint_size , 1 )
        #research_effect      = pg.draw.circle(screen , (255 , 0 , 0)  , ( -camera.rect[0] + int(checkpoints_file1[0].split(',')[0]) , -camera.rect[1] + int(checkpoints_file1[0].split(',')[1])) , checkpoint_size , 1 )
        #loading_effect       = pg.draw.circle(screen , (255 , 0 , 0)  , ( -camera.rect[0] + int(checkpoints_file1[0].split(',')[0]) , -camera.rect[1] + int(checkpoints_file1[0].split(',')[1])) , checkpoint_size , 1 )
        #dialoge_effect       = pg.draw.circle(screen , (255 , 0 , 0)  , ( -camera.rect[0] + int(checkpoints_file1[0].split(',')[0]) , -camera.rect[1] + int(checkpoints_file1[0].split(',')[1])) , checkpoint_size , 1 )
        #blood_effect         = pg.draw.circle(screen , (255 , 0 , 0)  , ( -camera.rect[0] + int(checkpoints_file1[0].split(',')[0]) , -camera.rect[1] + int(checkpoints_file1[0].split(',')[1])) , checkpoint_size , 1 )
        #research_complete    = 0
    

    """
            for i in range(len(items_file1)):
                if event.button == 3 and  pos[0] >=  -camera.rect[0] + int(items_file1[i].split(',')[0]) and pos[0] <=  -camera.rect[0] + int(items_file1[i].split(',')[0]) + items_images[i].get_width() \
                    and pos[1] >=  -camera.rect[1] + int(items_file1[i].split(',')[1]) and pos[1] <=  -camera.rect[1] + int(items_file1[i].split(',')[1]) + items_images[i].get_height():
                    hero_belt_inventory_images.append(items_images[i])

                    if pickup_sound_num >= 0 and pickup_sound_num <= len(pickup_sounds_dir) - 1 and len(hero_belt_inventory_images) - 1 <= items_max:
                        pickup_sound.play() ; pickup_sound_num += 0.5 ; pickup_sound = pg.mixer.Sound('Audio/sounds/pickup/' + str(int(pickup_sound_num)) + '.mp3')
            """ 
    
    
    
    """
            for i in range(len(items_file1)):
                if event.button == 3 and  pos[0] >=  -camera.rect[0] + int(items_file1[i].split(',')[0]) and pos[0] <=  -camera.rect[0] + int(items_file1[i].split(',')[0]) + items_images[i].get_width() \
                    and pos[1] >=  -camera.rect[1] + int(items_file1[i].split(',')[1]) and pos[1] <=  -camera.rect[1] + int(items_file1[i].split(',')[1]) + items_images[i].get_height():
                    hero_belt_inventory_images.append(items_images[i])

                    if pickup_sound_num >= 0 and pickup_sound_num <= len(pickup_sounds_dir) - 1 and len(hero_belt_inventory_images) - 1 <= items_max:
                        pickup_sound.play() ; pickup_sound_num += 0.5 ; pickup_sound = pg.mixer.Sound('Audio/sounds/pickup/' + str(int(pickup_sound_num)) + '.mp3')
            """

             
            #for y in range( len ( islands_file1 ) ) : 
                #screen.blit( islands_images[ i ] , (-camera.rect[0] + int(islands_file1[i].split(',')[0]) + i * int(islands_file1[i].split(',')[2]) / 100 , -camera.rect[1] + int(islands_file1[i].split(',')[1]) + y * int(islands_file1[i].split(',')[2]) ,  5 / map_scale ,  5 / map_scale ))
            
            #for i in range( len ( roads_file1 ) ) : 
            #    if camera.rect[0] + int(screen_width) - fov >= int(roads_file1[i].split(',')[0]) and camera.rect[1] + int(screen_height) - fov >= int(roads_file1[i].split(',')[1]):
            #        #pg.draw.line(screen , (20, 20  , 20 ) ,  , 10)
            #        pg.draw.polygon(screen , (20 , 20 , 20) , (  
            #            
            #                                                    [  -camera.rect[ 0 ] + int(roads_file1[i].split(',')[0]) , -camera.rect[ 1 ] + int(roads_file1[i].split(',')[1]) ] ,
            #                                                    
            #                                                    [  -camera.rect[ 0 ] + int(roads_file1[i].split(',')[0]) + meter * -math.sin(-fuel ) , -camera.rect[ 1 ] + int(roads_file1[i].split(',')[1]) + meter * -math.cos(-fuel ) ] ,
            #                                                     
            #                                                    [  -camera.rect[ 0 ] + int(roads_file1[i].split(',')[0])  , -camera.rect[ 1 ] + int(roads_file1[i].split(',')[1]) + meter * 2 ] ,
            #                                                    
            #                                                   [  -camera.rect[ 0 ] + int(roads_file1[i].split(',')[0]) + meter * math.sin(fuel ) , -camera.rect[ 1 ] + int(roads_file1[i].split(',')[1]) + meter * math.cos(fuel ) ] 
            #                                                    
            #                                                    ))

            
    #for i in range(len(items_file1)):
    #        if event.button == 3 and  pos[0] >=  -camera.rect[0] + int(items_file1[i].split(',')[0])  and pos[0] <=  -camera.rect[0] + int(items_file1[i].split(',')[0]) + items_images_list[i].get_width() and pos[1] >=  -camera.rect[1] + int(items_file1[i].split(',')[1]) and pos[1] <=  -camera.rect[1] + int(items_file1[i].split(',')[1]) + items_images_list[i].get_height():
    #            action = 'Pickup'
    #            if pickup_sound_num >= 0 and pickup_sound_num <= len(pickup_sounds_dir) - 1 and len(hero_inventory_images) <= items_max:
    #                pickup_sound.play() ; pickup_sound_num += 0.5 ; pickup_sound = pg.mixer.Sound('Audio/sounds/pickup/' + str(int(pickup_sound_num)) + '.mp3')
    #                hero_inventory_images.append(items_images_list[i])
    #            if pickup_sound_num >= len(pickup_sounds_dir) - 1 and len(hero_inventory_images) - 1: pickup_sound_num = 0
    #            if len(hero_inventory_images) >= items_max : inv_is_full_sound.play()
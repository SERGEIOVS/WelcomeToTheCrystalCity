#Funcs.py imports
from pathlib import Path
import sys
# путь к Scripts/Python
sys.path.append(str(Path(__file__).resolve().parent))


import pygame as pg
import pyautogui
import time 
import logging
import mido
import cv2
import numpy as np


from Controllers.Settings import variables
from Controllers.Units import *
from Controllers.Background import *
from Controllers.Controls import *
from Controllers.Items import items_max,item
from Controllers.Vehicles import vehicle_sit


pg.init()



#sounds
welcome_speech_dir = os.listdir('Audio/sounds/welcome/')
enemy_sounds_dir   = os.listdir('Audio/sounds/roar/')
pickup_sounds_dir = os.listdir('Audio/sounds/pickup/')

sounds_dir = os.listdir('Audio/sounds/')

#music
soundtracks = os.listdir('Audio/enviroment/') ; switch_music = 1 ; music = soundtracks[switch_music] ; show_song_name = small_font.render(str(music) , False , ( 250 , 0 , 0 ) ) ; pg.mixer.music.load('Audio/enviroment/' + str(music))


minimap_border_offset = 10
minimap_object_offset = 0
minimap_object_offset1 = 0



sounds_dict = {
     
"step_sound"        : pg.mixer.Sound('Audio/sounds/steps/grass/'       + str(variables["step_sound_num"])   + '.mp3'),
"rifle_sound"       :pg.mixer.Sound('Audio/sounds/firegun/automatic/'  + str(variables["rifle_sound_num"])  + '.mp3'),
"spawn_sound"       : pg.mixer.Sound('Audio/sounds/spawn/'             + str(variables["spawn_sound_num"])  + '.mp3'),
"scream_sound"      : pg.mixer.Sound('Audio/sounds/screams/far/'       + str(variables["scream_sound_num"]) + '.mp3'),
"death_sound"       : pg.mixer.Sound('Audio/sounds/death/'             + str(variables["death_sound_num"])  + '.mp3'),
"pickup_sound"      : pg.mixer.Sound('Audio/sounds/pickup/'            + str(variables["pickup_sound_num"]) + '.mp3'),
"enemy_sound"       : pg.mixer.Sound('Audio/sounds/roar/'              + str(variables["enemy_sound_num"])  + '.mp3'),
"click_sound"       : pg.mixer.Sound('Audio/sounds/clicks/'            + str(variables["click_sound_num"])  + '.mp3'),
"welcome"           : pg.mixer.Sound('Audio/speech/langs/'             + str(variables["language"])         + '/welcome/' + str(int(variables["welcome_num"])) + '.mp3'),
"inv_is_full_sound" : pg.mixer.Sound('Audio/sounds/massages/Full inventory/' + str(variables["nums"]["inv_full_sound_num"]) +'.mp3')

}

bg_images   = []
for i in range(len(variables["wallpapers_dir"])) :
     if i not in bg_images : bg_images.append(pg.image.load( 'Wallpapers/' + str(screen_width) + '_' + str(screen_height) + '/' + str(i) + '.png'))

Icons_dir = os.listdir('Interface/Icons/')

for i in range(len(Icons_dir)) : pass



icons_dict = {



"pics":{

"health_icon"    : pg.image.load('Interface/Icons/Health/'          + str(variables["health_icon_num"])    + '.png'),
"ammo_icon"      : pg.image.load('Interface/Icons/Ammo/'            + str(variables["ammo_icon_num"])      + '.png'), 
"armor_icon"     : pg.image.load('Interface/Icons/Armor/'           + str(variables["armor_icon_num"])     + '.png'),
"radiation_icon" : pg.image.load('Interface/Icons/Radiation/'       + str(variables["radiation_icon_num"]) + '.png'),
"energy_icon"    : pg.image.load('Interface/Icons/Energy/'          + str(variables["energy_icon_num"])    + '.png'),
"sound_icon"     : pg.image.load('Interface/Icons/Music/'           + str(variables["sound_icon_num"])     + '.png'),
"cancel_icon"    : pg.image.load('Interface/buttons/cancel/'        + str(variables["cancel_icon_num"])    + '.png'),
"cursor"         : pg.image.load( 'Interface/icons/Select/0.png')

},



"coords":{
     
"cancel_icon_x"  :  int(variables["screen_width"] ) - 50,
"cancel_icon_y" : 50

}

}

Button_color = (45 , 45 , 45) ; minimap_border_color = (45 , 45 , 45) ; Button_frame_color = (255 , 0 , 0) ; cell_color = ( 45  , 45 , 45 )



def make_screenshot() :
    screenshots = 1  ; screenshot = pyautogui.screenshot() 
    for i in range(screenshots)  : screenshot.save( 'screenshots/' + str(d1.year) + ' - ' + str(d1.month) + ' - ' + str(d1.day) + ' - ' + str(d1.hour) + ' - ' +  str(d1.minute) + ' - ' + str(d1.second) + '.png' )

#def save_game_and_quit() :saves_file_mode = 'w' ; saves_file = open (saves_file_name , saves_file_mode) ; saves_file.write( str(screen_width) + ',' + str(screen_height) + ',' + str(camera.rect[0]) + ',' + str(camera.rect[1])) ; saves_file.close() ; logging.info(msg = 'GAME SAVED!' ) ; pg.quit() ; logging.info(msg = 'QUIT GAME!' )
def toggle_god_mode() : global print_god_mode , god_mode ; god_mode = 0 ; print_god_mode = print('GOD MODE ACTIVATED!')

def load_game() : saves_file_mode = 'r' ; saves_file = open (files_dict["saves_file_name"] , saves_file_mode) ; saves_file.close() ; logging.info(msg = 'GAME LOADED!' ) ; print('Game loaded!')
def save_game() : saves_file_mode = 'w' ; saves_file = open (files_dict["saves_file_name"] , saves_file_mode) ; saves_file.write( str(screen_width) + ',' + str(screen_height) + ',' + str(variables["camera"].rect[0]) + ',' + str(variables["camera"].rect[1])  );saves_file.close() ; logging.info(msg = 'GAME SAVED!' ) ; print('GAME SAVED!')


def draw_menu():
        screen.blit( bg_images[variables["bg_num"]] , ( 0   , 0  ))
        screen.blit(show_game_title    , ( int(variables["screen_width"] )  /  2 - len(Game_title)  * variables["smallfont"] / 2  , 10))
        screen.blit( show_update       , ( int(variables["screen_width"] )  /  2 - len(variables["update_name"]) * variables["smallfont"] / 2  , 50))    
        screen.blit(show_game_version  , (  10 , int(screen_height) - variables["bigfont"]))
        screen.blit( show_author       , (  0  , 10 ))
        screen.blit( show_created_date , (  0  , 35 ))
        screen.blit( icons_dict["cancel_icon"] , ( icons_dict['cancel_icon_x'], icons_dict['cancel_icon_y']))
        game_state_x = int(variables["screen_width"] ) / 2 - int(len(game_state) * variables["bigfont"] / 3) ; game_state_y = 100



def start():
    global variables

    if game_state == 'Saves':
        for i in range(len(files_dict["saves_file1"])):
            Button = pg.draw.rect(screen , (variables["Button_color"]) , ( int(variables["screen_width"]) /  2 - variables["button_width"] / 2 , int(screen_height) / 2 - int(variables["screen_height"])) / 4 -(variables["bigfont"] + i * 40 +(variables["bigfont"] /2) ,variables["button_width"],(variables["bigfont"] + 5  , 0 , 0 , variables["button_border_radius"] , variables["button_border_radius"] , variables["button_border_radius"] , variables["button_border_radius"])))
        #screen.blit(saves_list[i]                     , ( int(variables["screen_width"] ) /  2 -variables["button_width"]/ 2 , int(screen_height) / 2 - int(screen_height) / 4 -(variables["bigfont"] + i * 40 +(variables["bigfont"] / 2 ,variables["button_width"],(variables["bigfont"] ))
            pg.draw.rect(screen , (Button_frame_color)    , ( int(variables["screen_width"] ) /  2 - variables["button_width"] / 2 , int(screen_height) / 2 - int(screen_height) / 4 -(variables["bigfont"] + variables["active_button"] * 40 +(variables["bigfont"] / 2 ,variables["button_width"],(variables["bigfont"] + 5 )) , 2 , 0 ,(variables["button_border_radius"] ,(variables["button_border_radius"] ,(variables["button_border_radius"] ,variables["button_border_radius"]))))))



    if game_state == 'Crafting':
        for i in range(len(variables["menus_dir"]) // variables["crafts_on_page"]) :
                
                #drawing a buttons for a crafts menu
                Button = pg.draw.rect(screen , (Button_color)       , ( int(variables["screen_width"] ) / 2 -variables["button_width"]/ 2 , int(screen_height) /10 + i * 40 , 500 , variables["bigfont"]) , 2 , 0 ,(variables["button_border_radius"] ,(variables["button_border_radius"] ,(variables["button_border_radius"] , variables["button_border_radius"]))))
                pg.draw.rect(screen          , (Button_frame_color) , ( int(variables["screen_width"] ) / 2 -variables["button_width"]/ 2  , int(screen_height) /10 +variables["screen_width"] * 40 , 500 , variables["bigfont"]) , 2 , 0 ,(variables["button_border_radius"] ,(variables["button_border_radius"] ,(variables["button_border_radius"] ,(variables["button_border_radius"] )))))
                screen.blit(str(i)   , ( int(variables["screen_width"] ) / 2 - variables["button_width"] / 2 +(variables["bigfont"] , int(screen_height) / 10 + i * 40 , 100 ,(variables["bigfont"] ))))
                screen.blit(new_craft        , ( int(variables["screen_width"] ) / 2 + -variables["button_width"]/ 2 -(variables["cell_size"] * 2 , int(screen_height) / 10 + i * 40 , 100 ,(variables["bigfont"] ))))


    if game_state == 'Play':
        if variables["ground"] == 1:

            world_border = pg.draw.rect(screen , (Button_frame_color) , ( -variables["camera1"].rect[ 0 ] + 0 ,-variables["camera1"].rect[ 1 ] + 0 , variables["map_width"] , variables["map_width"]) , 10 , 0  )

            #islands
            for i in range(len(variables["dots"])):
                pg.draw.polygon(screen, variables["land_color"] , variables["dots"])
                pg.draw.polygon(screen, (10,60,0) ,variables["rocks"])



            for i in range( len ( vihicles_file1 ) ) : 
                 if variables["camera1"].rect[0] + int(variables["screen_width"] ) -variables["fov"]>= int(vihicles_file1[i].split(',')[0])  and variables["camera1"].rect[1] + int(screen_height) -variables["fov"]>= int(vihicles_file1[i].split(',')[1]) and hero_image != vihicles_images_list[i]:
                    screen.blit( vihicles_images_list[i] , ( -variables["camera1"].rect[ 0 ] + int(vihicles_file1[i].split(',')[0]) , -variables["camera1"].rect[ 1 ] + int(vihicles_file1[i].split(',')[1]) ) )



            #rooms
            for i in range(len(buildings_file1)) :

                #room_floor
                pg.draw.polygon(screen , (lists["colors"][7]) , (       




[-variables["camera1"].rect[0] + 1000 + int(buildings_file1[i].split(',')[0])                               , -variables["camera1"].rect[1] + 1000 + int(buildings_file1[i].split(',')[1])  ] ,
[-variables["camera1"].rect[0] + 1000 + int(buildings_file1[i].split(',')[0]) +variables["measure_units"]["meter"] * 3  * math.cos(variables["fuel"]) , -variables["camera1"].rect[1] + 1000 + int(buildings_file1[i].split(',')[1]) +variables["measure_units"]["meter"] * 3  * math.sin(variables["fuel"]) ] , 
[-variables["camera1"].rect[0] + 1000 + int(buildings_file1[i].split(',')[0]) +variables["measure_units"]["meter"] * 15 * math.cos(variables["fuel"]) , -variables["camera1"].rect[1] + 1000 + int(buildings_file1[i].split(',')[1]) +variables["measure_units"]["meter"] * 3  * math.sin(variables["fuel"]) ] ,
[-variables["camera1"].rect[0] + 1000 + int(buildings_file1[i].split(',')[0]) +variables["measure_units"]["meter"] * 7  * math.cos(variables["fuel"]) , -variables["camera1"].rect[1] + 1000 + int(buildings_file1[i].split(',')[1])  ] , 
                                                                  
))
                funcs_dir = {
                     
                make_screenshot : make_screenshot,
                start           : start,
                toggle_god_mode :  toggle_god_mode,
                save_game       : save_game,
                load_game       : load_game

                }


                #room_celling
                pg.draw.polygon(screen , variables["lists"]["colors"][5] ,     (  

[-variables["camera1"].rect[0] + 1000 + int(buildings_file1[i].split(',')[0])                               , -variables["camera1"].rect[1] + 1000 + int(buildings_file1[i].split(',')[1]) - variables["room_height"] ] ,
[-variables["camera1"].rect[0] + 1000 + int(buildings_file1[i].split(',')[0]) +variables["measure_units"]["meter"] * 3  * math.cos(variables["fuel"]) , -variables["camera1"].rect[1] + 1000 + int(buildings_file1[i].split(',')[1]) +variables["measure_units"]["meter"] * 3 * math.sin(variables["fuel"]) - variables["room_height"] ] , 
[-variables["camera1"].rect[0] + 1000 + int(buildings_file1[i].split(',')[0]) +variables["measure_units"]["meter"] * 15 * math.cos(variables["fuel"]) , -variables["camera1"].rect[1] + 1000 + int(buildings_file1[i].split(',')[1]) +variables["measure_units"]["meter"] * 3 * math.sin(variables["fuel"]) - variables["room_height"] ] ,
[-variables["camera1"].rect[0] + 1000 + int(buildings_file1[i].split(',')[0]) +variables["measure_units"]["meter"] * 7  * math.cos(variables["fuel"]) , -variables["camera1"].rect[1] + 1000 + int(buildings_file1[i].split(',')[1])  - variables["room_height"]  ] ,

[-variables["camera1"].rect[0] + 1000 + int(buildings_file1[i].split(',')[0]) +variables["measure_units"]["meter"] * 7  * math.cos(variables["fuel"]) , -variables["camera1"].rect[1] + 1000 + int(buildings_file1[i].split(',')[1]) - variables["room_height"] +variables["measure_units"]["meter"] / 2 ] ,
[-variables["camera1"].rect[0] + 1000 + int(buildings_file1[i].split(',')[0]) +variables["measure_units"]["meter"] * 7  * math.cos(variables["fuel"]) , -variables["camera1"].rect[1] + 1000 + int(buildings_file1[i].split(',')[1]) - variables["room_height"] +variables["measure_units"]["meter"] / 2 ] ,      
[-variables["camera1"].rect[0] + 1000 + int(buildings_file1[i].split(',')[0])                               , -variables["camera1"].rect[1] + 1000 + int(buildings_file1[i].split(',')[1]) - variables["room_height"] +variables["measure_units"]["meter"] / 2 ] ,      

)) 
               


                #room_walls
                pg.draw.polygon(screen , ( variables["measure_units"]["colors"][6] ) , (  

[-variables["camera1"].rect[0] + 1000 + int(buildings_file1[i].split(',')[0])                               , -variables["camera1"].rect[1] + 1000 + int(buildings_file1[i].split(',')[1])   ] ,
[-variables["camera1"].rect[0] + 1000 + int(buildings_file1[i].split(',')[0])                               , -variables["camera1"].rect[1] + 1000 + int(buildings_file1[i].split(',')[1]) -variables["meter"]] ,
                                                               
[-variables["camera1"].rect[0] + 1000 + int(buildings_file1[i].split(',')[0]) + variables["measure_units"]["meter"] * 7  * math.cos(variables["fuel"]) , -variables["camera1"].rect[1] + 1000 + int(buildings_file1[i].split(',')[1]) -variables["measure_units"]["meter"] ],
[-variables["camera1"].rect[0] + 1000 + int(buildings_file1[i].split(',')[0]) + variables["measure_units"]["meter"] * 7  * math.cos(variables["fuel"]) , -variables["camera1"].rect[1] + 1000 + int(buildings_file1[i].split(',')[1]) -variables["measure_units"]["meter"] ],                                                         
                                                               
[-variables["camera1"].rect[0] + 1000 + int(buildings_file1[i].split(',')[0]) + variables["measure_units"]["meter"] * 7  * math.cos(variables["fuel"]) , -variables["camera1"].rect[1] + 1000 + int(buildings_file1[i].split(',')[1]) ]

))
                

        #drawing a text for a quests menu
        if len(variables["quests_file1"]) != 0:
            for i in range(len(variables["quests_file1"])) : variables["quests_surf"].blit(variables["quests_list"][i] , (5 , 5 +(variables["bigfont"] / 2 * i * 1.6 ) ) ) #screen.blit(show_quests_num , (int(screen_width ) - int(variables["screen_width"] ) /3  , int(screen_height ) - int(screen_height) /3 -(variables["bigfont"] ) )

        for i in range(len(Furniture_file1)) :
            for y in range(int(Furniture_file1[i].split(',')[2])):
                if variables["camera1"].rect[0] + int(variables["screen_width"] ) -variables["fov"] >= int(Furniture_file1[i].split(',')[0]) and variables["camera1"].rect[1] + int(screen_height) -variables["fov"] >= int(Furniture_file1[i].split(',')[1]) : screen.blit( Furniture_images_list[ i ] , ( -variables["camera1"].rect[ 0 ] + int(Furniture_file1[i].split(',')[0]) + int(Furniture_file1[i].split(',')[2]) * y * 10  , -variables["camera1"].rect[ 1 ] + int(Furniture_file1[i].split(',')[1] ) ) )
                

        for i in range(len(Plants_file1)) :
                if variables["camera1"].rect[0] + int(variables["screen_width"] ) -variables["fov"]>= int(Plants_file1[i].split(',')[0]) and variables["camera1"].rect[1] + int(screen_height) -variables["fov"]>= int(Plants_file1[i].split(',')[1]) : screen.blit( Plants_file1[ i ] , ( -variables["camera1"].rect[ 0 ] + int(Plants_file1[i].split(',')[0]) , -variables["camera1"].rect[ 1 ] + int(Plants_file1[i].split(',')[1] ) ) )

        variables["interface_surf"].set_alpha(50)
        variables["quests_surf"].set_colorkey(( 0 , 0 , 0 ))

        screen.blit( hero_image, (hero_x, hero_y ))
        screen.blit(variables["rot_hero"], (500,200))

        screen.blit(scaled_image, (550,200 ))

        screen.blit( enemy.image , ( -variables["camera1"].rect[0] + enemy.x , -variables["camera1"].rect[1] + enemy.y ))
        
        #variables["fuel"]_bar(green color)
        #pg.draw.line( screen , (0 , 255 , 0) , (400 , 400) , ( 400 + variables["fuel"]_bar_width * -math.cos(variables["fuel"]) , 400 + variables["fuel"]_bar_width * -math.sin(-variables["fuel"])) , 1)


if variables["show_interface"] == 1:

            if len(variables["hero_inventory"]) != 0:
                screen.blit(
                    variables["hero_inventory"][item],
                    (
                        int(screen_width) / 2,
                        int(screen_height) - (variables["cell_size"] * 2)
                    )
                )

            variables["dark_surf"].fill(variables["dark_surf_color"])
            variables["dialoge_surf"].fill((0, 0, 0))
            variables["dark_surf"].set_alpha(variables["dark_level"])
            screen.blit(variables["dark_surf"], (0, 0))

            screen.blit(
                variables["hero_shadow_surf"],
                (
                    hero_x,
                    hero_y + hero_image1.get_height()
                )
            )

            pg.draw.circle(
                variables["hero_shadow_surf"],
                (10, 0, 0),
                (50, 50),
                50
            )

            variables["hero_shadow_surf"].set_colorkey((0, 0, 0))
            variables["hero_shadow_surf"].set_alpha(100)
            variables["quests_surf"].fill((variables["quest_surf_color"]))
                


            screen.blit(variables["show_hero_armor"], ( variables["big_font"] + 10 , int(screen_height ) - variables["big_font"] * 5))
            
            
            
            
            
            
            screen.blit(variables["show_ammo"]       , ( variables["big_font"] + 10 , int(screen_height ) - variables["big_font"] * 4))
            screen.blit(variables["show_health"]     , ( variables["big_font"] + 10 , int(screen_height ) - variables["big_font"] * 6))
            screen.blit(variables["show_radiation"]  , ( variables["big_font"] + 10 , int(screen_height ) - variables["big_font"] * 3))
            screen.blit(variables["show_energy"]     , ( variables["big_font"] + 10 , int(screen_height ) - variables["big_font"] * 2))
            screen.blit(variables["show_money"]      , ( 10           , int(screen_height ) - variables["big_font"]))



            screen.blit( icons_dict['pics']['ammo_icon']      , ( icons_dict['cancel_icon_x'] , icons_dict['cancel_icon_y']))
            screen.blit(icons_dict['pics']["energy_icon"]     , ( 10 , int(screen_height ) - variables["big_font"] * 2))
            screen.blit(icons_dict['pics']["radiation_icon"]  , ( 10 , int(screen_height ) - variables["big_font"] * 3))
            screen.blit(icons_dict['pics']["ammo_icon"]       , ( 10 , int(screen_height ) - variables["big_font"] * 4))
            screen.blit(icons_dict['pics']["armor_icon"]      , ( 10 , int(screen_height ) - variables["big_font"] * 5))
            screen.blit(icons_dict['pics']['health'])         , ( 10 , int(screen_height ) - variables["big_font"] * 6)

            

            for x in range( int(variables["map_width"] / variables["km"])) :
                for y in range( int(variables["map_height"] / variables["measure_units"]["km"])) : pg.draw.rect(screen , (255,0,0) , (  -variables["camera1"].rect[0] +variables["measure_units"]["meter"] * measure_units["km"] * x  , -variables["camera1"].rect[1] +variables["measure_units"]["meter"] * measure_units["km"] * y , measure_units["km"], measure_units["km"]),2,0)   



bg_num = 1 ; wallpapers_dir = os.listdir('Wallpapers/' + str(screen_width) + '_' + str(screen_height) + '/') ; wallpaper  = wallpapers_dir[bg_num]

for i in enumerate(surfs_dict["screen_surfs_list"]):
        print(f"screen surf : {i}")

if variables["dark_level"] <= variables["max_dark_level"] : variables["dark_level"] += 0.01
    
for event in pg.event.get() :
    variables["mini_map_surf"].fill((minimapBGcolor))
screen.fill( (BGcolor) )
    
#start()

"""
if game_state != 'Play' : show_game_state = big_font.render(str(game_state) , False , small_font_color) ; screen.blit( show_game_state ,  (game_state_x , game_state_y))
    
for i in range(len(main_menu_file1)):
        if game_state == 'Main_menu' and pos[0] >= int(variables["screen_width"] ) / 2 -variables["button_width"]/ 2  and pos[0] <= int(variables["screen_width"] ) /  2 +variables["button_width"]/ 4 and pos[1] >= int(screen_height) / 2 - int(screen_height) / 4 -(variables["bigfont"] + i * 40 +(variables["bigfont"] / 2  and pos[1] <= int(screen_height) / 2 - int(screen_height) / 4 -(variables["bigfont"] + i * 40 +(variables["bigfont"] / 2 + button_height :variables["screen_width"] = i
        
for i in range(len(variables["menus_dir"])):
        if game_state == 'Crafting'  and pos[0] >= int(variables["screen_width"] ) / 2 -variables["button_width"]/ 2  and pos[0] <= int(variables["screen_width"] ) /  2 +variables["button_width"]/ 4 and pos[1] >= int(screen_height) / 2 - int(screen_height) / 4 -(variables["bigfont"] + i * 40 +(variables["bigfont"] / 2  and pos[1] <= int(screen_height) / 2 - int(screen_height) / 4 -(variables["bigfont"] + i * 40 +(variables["bigfont"] / 2 + button_height :variables["screen_width"] = i

for i in range(len(saves_file1)):
        if game_state == 'Saves'     and pos[0] >= int(variables["screen_width"] ) / 2 -variables["button_width"]/ 2  and pos[0] <= int(variables["screen_width"] ) /  2 +variables["button_width"]/ 4 and pos[1] >= int(screen_height) / 2 - int(screen_height) / 4 -(variables["bigfont"] + i * 40 +(variables["bigfont"] / 2  and pos[1] <= int(screen_height) / 2 - int(screen_height) / 4 -(variables["bigfont"] + i * 40 +(variables["bigfont"] / 2 + button_height :variables["screen_width"] = i
        
for i in range(len(Hero_types)):
        if game_state == 'character_select_menu' and pos[0] >= int(variables["screen_width"] ) / 2 -variables["button_width"]/ 2  and pos[0] <= int(variables["screen_width"] ) /  2 +variables["button_width"]/ 4 and pos[1] >= int(screen_height) / 2 - int(screen_height) / 4 -(variables["bigfont"] + i * 40 +(variables["bigfont"] / 2  and pos[1] <= int(screen_height) / 2 - int(screen_height) / 4 -(variables["bigfont"] + i * 40 +(variables["bigfont"] / 2 + button_height :variables["screen_width"] = i)))))))
        
for i in range(items_max):    
        if game_state == 'Trade_menu' and pos[0] >= int(variables["screen_width"] ) / 2 -variables["button_width"]and pos[0] <= int(variables["screen_width"] ) /  2 +variables["button_width"]/ 4 and pos[1] >= int(screen_height) / 2 - int(screen_height) / 4 -(variables["bigfont"] + i * 40 +(variables["bigfont"] / 2  and pos[1] <= int(screen_height) / 2 - int(screen_height) / 4 -(variables["bigfont"] + i * 40 +(variables["bigfont"] / 2 + button_height :variables["screen_width"] )))))))
        
for i in range(len(game_modes1)):
        if game_state == 'game_mode_select' and pos[0] >= int(variables["screen_width"] ) / 2 -variables["button_width"]/ 2  and pos[0] <= int(variables["screen_width"] ) /  2 +variables["button_width"]/ 4 and pos[1] >= int(screen_height) / 2 - int(screen_height) / 4 -(variables["bigfont"] + i * 40 +(variables["bigfont"] / 2  and pos[1] <= int(screen_height) / 2 - int(screen_height) / 4 -(variables["bigfont"] + i * 40 +(variables["bigfont"] / 2 + button_height :variables["screen_width"] = i))))))
    
for x in range(minimap_grid_width):
        for y in range(minimap_grid_height):
            pg.draw.rect(variables["mini_map_surf"] , (cell_color) , (variables["cell_size"] * x ,(variables["cell_size"] * y ,(variables["cell_size"] ,(variables["cell_size"] ) , 2 , 0 ,(variables["button_border_radius"] ,(variables["button_border_radius"] ,(variables["button_border_radius"] ,(variables["button_border_radius"] )))))))) #drawing a inventory cells

"""

def draw_mini_map():
    if variables["show_map"] == 1:
        for i in range( len ( files_dict["islands_file1"] ) ) :
            for y in range( len (files_dict["islands_file1"] ) ) :
                pg.draw.rect(variables["mini_map_surf"] , (100 , 50 , 0) , (["measure_units"]["meter"] * 30 / (measure_units["meter"] * map_scale) ,variables["measure_units"]["meter"] * 30  / (measure_units["meter"] / variables["map_scale"]) , measure_units["km"] * 5 / (measure_units["meter"] * variables["map_scale"]) , measure_units["km"] * 5 / (measure_units["meter"] * variables["map_scale"]) ))

        for i in range( len ( buildings_file1 ) ) :
             if variables["show_buildings"]== 1 : pg.draw.rect(variables["mini_map_surf"] , (133 , 133 , 133)  , ( int(buildings_file1[ i ].split(',')[0]) / (100 * map_scale) + minimap_border_offset * 2 , int(buildings_file1[ i ].split(',')[1]) / (100 * map_scale) + minimap_object_offset1 * 2 ,  10 / map_scale, 10 / map_scale ))
        
        for i in range( len ( vihicles_file1 ) ) : pg.draw.rect(variables["mini_map_surf"] , (0 , 0 , 0) , (int(vihicles_file1[i].split(',')[0]) / (100 * map_scale) + minimap_border_offset * minimap_object_offset , int(vihicles_file1[i].split(',')[1]) / (100 * map_scale) + minimap_border_offset * minimap_object_offset1 , 5 / map_scale , 3 / map_scale ))
        

        hero_marker = pg.draw.circle(variables["mini_map_surf"] , ( hero_marker_color )        , ( minimap_border_offset + variables["camera1"].rect[0] / (100 * map_scale) + minimap_border_offset * minimap_object_offset ,  variables["camera1"].rect[1] / (100 * map_scale) + minimap_border_offset * minimap_object_offset1  ) , 1 / map_scale )        
        
        for i in range(len(lists["custom_checkpoints_list_x"])) : pg.draw.circle(variables["mini_map_surf"] , (255 , 0 , 0) , ( int(lists["custom_checkpoints_list_x"[i]]) / (100 * map_scale ) , int(lists["custom_checkpoints_list_y"][i]) / (100 * map_scale)) , int(1 / map_scale)  , int(1 / map_scale) )

        screen.blit(variables["mini_map_surf"] , ( minimap_x , minimap_y ) )
        
        pg.draw.rect(screen , (minimap_border_color) , ( 0 , 0 , int(variables["screen_width"] ) / map_size + minimap_border_offset , int(screen_height) / map_size + minimap_border_offset ) , minimap_border_offset , minimap_border_offset)
        



        map_grid = 0
        if map_grid == 1:
            for x in range(variables["grid_size1"]):
                for y in range(variables["grid_size2"]):pg.draw.rect(variables["mini_map_surf"] , ( cell_color) , ((variables["cell_size"] * x / map_scale * minimap_object_offset ,(variables["cell_size"] * y / map_scale * minimap_object_offset1 , mini_map_grid_cell_size / map_scale , mini_map_grid_cell_size / map_scale) , 1 ))) #drawing a inventory cells






def mini_map_mouse_controls():
    global cancel_icon
    if event.button == 1 and pos[0] >= cancel_icon_x and pos[0] <= cancel_icon_x + cancel_icon.get_width() and pos[1] >= cancel_icon_y and pos[1] <= cancel_icon_y + cancel_icon.get_height() and map_size == max_map_size : map_size = min_map_size

    if event.button == 3 and map_size == max_map_size : spawn_sound.play() ; lists["custom_checkpoints_list_x"].append(variables["camera1"].rect[0] + pos[0]) ; lists["custom_checkpoints_list_y"].append(variables["camera1"].rect[1] + pos[1])

changed_keybinds = []

Random_events = []

def toggle_settings():
    Button_color,variables["button_width"]
    if game_state == 'Settings':
        for i in range(len(files_dict["settings_file1"])):
            pg.draw.rect(screen , (Button_color) , ( int(variables["screen_width"] ) / 2 -variables["button_width"]       , int(screen_height) / 2 - int(screen_height) / 4 -(variables["bigfont"] + i * 40 +(variables["bigfont"] / 2 ,variables["button_width"],(variables["bigfont"] + 5 ), 0 , 0 ,(variables["button_border_radius"] ,(variables["button_border_radius"] ,(variables["button_border_radius"] , variables["button_border_radius"])))))))
            pg.draw.rect(screen , (Button_frame_color)  , ( int(variables["screen_width"] ) / 2 -variables["button_width"], int(screen_height) / 2 - int(screen_height) / 4 -(variables["bigfont"] +variables["screen_width"] * 40 +(variables["bigfont"] / 2 ,variables["button_width"],(variables["bigfont"] + 5 ) , 2 , 0 ,(variables["button_border_radius"] ,(variables["button_border_radius"] ,(variables["button_border_radius"] ,(variables["button_border_radius"] )  )))))))

            screen.blit(variables["settings"][i] , ( int(variables["screen_width"] ) / 2 -(variables["bigfont"] * 10 / 2                 , int(screen_height) / 2 - int(screen_height) / 4 -(variables["bigfont"] + i             * 40 +(variables["bigfont"] / 2 ,variables["button_width"],(variables["bigfont"] + 5 ))))))
            
            if variables["screen_width"] == 0:
                for i in range(len(files_dict["resolutions_file1"])):
                    Button = pg.draw.rect(screen, (Button_color), (int(variables["screen_width"]) / 2 + variables["bigfont"], int(screen_height) / 2 - int(screen_height) / 4 - (variables["bigfont"] + i * 40 + variables["bigfont"] / 2), variables["button_width"], variables["bigfont"]), variables["button_border_radius"])                   
                                
            pg.draw.rect(screen, Button_frame_color, (int(variables["screen_width"]) / 2 + variables["bigfont"], int(screen_height) / 2 - int(screen_height) / 4 - (variables["bigfont"] + active_button1 * 40 + variables["bigfont"] / 2), variables["button_width"], variables["bigfont"]), variables["button_border_radius"])

        
            screen.blit(lists["resolutions_list"][i], (int(variables["screen_width"]) / 2 + variables["bigfont"], int(screen_height) / 2 - int(screen_height) / 4 - (variables["bigfont"] + i * 40 + variables["bigfont"] / 2)))




            if variables["screen_width"] == 1 or variables["screen_width"] == 2:
                pg.draw.line(screen   , (0   , 0  , 0 ) , [ int(variables["screen_width"] ) / 2 + variables["bigfont"]        , int(screen_height) / 2 - int(screen_height) / 4 -(variables["bigfont"] + 0 * 40) +variables["bigfont"] ] , [ int(variables["screen_width"] ) / 2 +variables["bigfont"] + 100 , int(screen_height /2) - int(screen_height) /4 - variables["bigfont"] + 0 * 40 + variables["bigfont"]  ], 1 )
                
                
                
                pg.draw.circle(screen , (255 , 0  , 0 ) , ( int(variables["screen_width"] ) / 2 + variables["bigfont"], int(screen_height) / 2 - int(screen_height) / 4 -(variables["bigfont"] + 0 * 40 + variables["bigfont"] /2)  , 1))
                
                pg.draw.circle(screen , (255 , 0  , 0 ) ,( int(variables["screen_width"] ) / 2 + variables["bigfont"]  + 100, int(screen_height) / 2 - int(screen_height) / 4 -(variables["bigfont"] + 0 * 40 +(variables["bigfont"] /2)  , 1)))
                
                pg.draw.rect(screen   , (Button_frame_color ), (int(variables["screen_width"] ) / 2 +(variables["bigfont"], int(screen_height) / 2 - int(screen_height) / 4 -(variables["bigfont"] + active_button1 * 40 +(variables["bigfont"] / 2 ,variables["button_width"], variables["bigfont"]) , 2 , 0 ,(variables["button_border_radius"] ,(variables["button_border_radius"], (variables["button_border_radius"] , variables["button_border_radius"])))))))
                
                
                
                screen.blit(ok, (int(variables["screen_width"] ) / 2 -(variables["bigfont"] * 10 / 2  + 300, int(screen_height) / 2 - int(screen_height) / 4 -(variables["bigfont"] + i * 40 +(variables["bigfont"] / 2 ,variables["button_width"],(variables["bigfont"] ))))))
                
                screen.blit(add, (int(variables["screen_width"] ) / 2 + 500 / 4  + 10, int(screen_height) / 2 - int(screen_height) / 4 -(variables["bigfont"] + i * 40 +(variables["bigfont"] / 2 , 100 ,(variables["bigfont"] )))))
                
                screen.blit(remove, ( int(variables["screen_width"] ) / 2 + 5                              , int(screen_height) / 2 - int(screen_height) / 4 -(variables["bigfont"] + i              * 40 +(variables["bigfont"] / 2 , 100 ,(variables["bigfont"] )))))
            
            if variables["screen_width"] == 3:
                for i in range(len(variables["menus_dir"])):
                    Button = pg.draw.rect(screen , (Button_color)        , ( int(variables["screen_width"] ) / 2 +(variables["bigfont"] , int(screen_height) / 2 - int(screen_height) / 4 -(variables["bigfont"] + i * 40 +(variables["bigfont"] / 2 ,variables["button_width"], variables["bigfont"]), 0 , 0 ,(variables["button_border_radius"] ,(variables["button_border_radius"], (variables["button_border_radius"], variables["button_border_radius"])))))))
                    pg.draw.rect(screen,(Button_frame_color), ( int(variables["screen_width"] ) / 2 +(variables["bigfont"] , int(screen_height) / 2 - int(screen_height) / 4 -(variables["bigfont"] + active_button1 * 40 +(variables["bigfont"] / 2 ,variables["button_width"], variables["bigfont"]),2 , 0  ,(variables["button_border_radius"] ,(variables["button_border_radius"], (variables["button_border_radius"], variables["button_border_radius"])))))))
        
        
        
        
        screen.blit(variables["menus_dir"][i],(int(variables["screen_width"] ) / 2 +(variables["bigfont"],int(screen_height) / 2 - int(screen_height) / 4 -(variables["bigfont"] + i * 40 +(variables["bigfont"] / 2)))))


def character_select():
    if game_state == 'character_select_menu':
        for i in range(len(Hero_types)):            
            Button = pg.draw.rect(screen , (Button_color) , ( int(variables["screen_width"] ) /  2 -variables["button_width"]/ 2 , int(screen_height) / 2 - int(screen_height) / 4 -(variables["bigfont"] + i * 40 +(variables["bigfont"] /2 ,variables["button_width"],(variables["bigfont"] + 5 ) , 0 , 0 ,(variables["button_border_radius"] ,(variables["button_border_radius"] ,(variables["button_border_radius"] , variables["button_border_radius"])))))))
            screen.blit(Hero_types_list[i], (int(variables["screen_width"] ) /  2 -variables["button_width"]/ 2  , int(screen_height) / 2 - int(screen_height) / 4 -(variables["bigfont"] + i * 40 +(variables["bigfont"] / 2 ,variables["button_width"],(variables["bigfont"] )))))
            
            pg.draw.rect(screen , (Button_frame_color)  ,  ( int(variables["screen_width"] ) /  2 -variables["button_width"]/ 2 , int(screen_height) / 2 - int(screen_height) / 4 -(variables["bigfont"] +variables["screen_width"] * 40 +(variables["bigfont"] / 2 ,variables["button_width"],(variables["bigfont"] + 5 ) , 2 , 0 ,(variables["button_border_radius"] ,(variables["button_border_radius"] ,(variables["button_border_radius"] , variables["button_border_radius"])))))))
            
            #остановился тут!
            screen.blit(hero_image1, ( int(variables["screen_width"] ) / 2 + int(variables["screen_width"] ) / 4 - hero_image1.get_width() /2 , hero_image1.get_height() ))


def game_mode_select():
    if game_state == 'game_mode_select':
        for i in range(len(game_modes1)):            
            Button = pg.draw.rect(screen, (Button_color), (int(variables["screen_width"] ) /  2 -variables["button_width"]/ 2, int(variables["button screen_height"]) / 2 - int(screen_height) / 4 -(variables["bigfont"] + i * 40 +(variables["bigfont"] /2 ,variables["button_width"],(variables["bigfont"] + 5 ) , 0 , 0 ,(variables["button_border_radius"] ,(variables["button_border_radius"] ,(variables["button_border_radius"] , variables["button_border_radius"])))))))



            pg.draw.rect(screen, (Button_frame_color), (int(variables["screen_width"] ) / 2 - variables["button_width"]/ 2,int(screen_height) / 2 - int(screen_height) / 4 -(variables["bigfont"] +variables["screen_width"] * 40 +(variables["bigfont"] / 2 ,variables["button_width"],(variables["bigfont"] + 5 ) , 2 , 0 ,(variables["button_border_radius"] ,(variables["button_border_radius"] ,(variables["button_border_radius"] , variables["button_border_radius"])))))))


            screen.blit(game_modes1[i], (int(variables["screen_width"] ) /  2 -variables["button_width"]/ 2  , int(screen_height) / 2 - int(screen_height) / 4 -(variables["bigfont"] + i * 40 +(variables["bigfont"] / 2 ,variables["button_width"],(variables["bigfont"] )))))



def Difficulty_select():
    if game_state == 'Select_a_difficulty':
        for i in range(len(difficulties1)):            
            Button = pg.draw.rect(screen, (Button_color), (int(variables["screen_width"] ) /  2 -variables["button_width"] / 2, int(screen_height) / 2 - int(screen_height) / 4 - (variables["bigfont"] + i * 40 + (variables["bigfont"] / 2, variables["button_width"], (variables["bigfont"] + 5 ), 0, 0, (variables["button_border_radius"], (variables["button_border_radius"], (variables["button_border_radius"], variables["button_border_radius"])))))))
            
            
            
            pg.draw.rect(screen , (Button_frame_color), (int(variables["screen_width"] ) /  2 - variables["button_width"] / 2, int(screen_height) / 2 - int(screen_height) / 4 -(variables["bigfont"] + variables["screen_width"] * 40 + (variables["bigfont"] / 2, variables["button_width"], (variables["bigfont"] + 5 ), 2, 0, (variables["button_border_radius"], (variables["button_border_radius"], (variables["button_border_radius"], variables["button_border_radius"])))))))
            screen.blit(difficulties1[i], (int(variables["screen_width"]) /  2 -variables["button_width"] / 2, int(screen_height) / 2 - int(screen_height) / 4 - (variables["bigfont"] + i * 40 + (variables["bigfont"] / 2, variables["button_width"], (variables["bigfont"] )))))



def Open_backpack():
    if game_state == 'Backpack':
        for i in range(len(menu_titles1)):            
            Button = pg.draw.rect(screen, (Button_color),       (int(variables["screen_width"] ) / 2 - variables["button_width"] - (variables["bigfont"], int(screen_height) / 4 + (variables["cell_size"] * i, variables["button_width"], variables["cell_size"]), 0, 0, (variables["button_border_radius"], (variables["button_border_radius"], (variables["button_border_radius"], variables["button_border_radius"]))))))
            pg.draw.rect(screen, (Button_frame_color), (int(variables["screen_width"] ) / 2 - variables["button_width"] - (variables["bigfont"], int(screen_height) / 4 + (variables["cell_size"] *    variables["screen_width"], variables["button_width"], (variables["cell_size"] ), 2, 0, (variables["button_border_radius"] ,(variables["button_border_radius"] ,(variables["button_border_radius"] , variables["button_border_radius"]))))))) #drawing a inventory cell_frame for a selected item in inventory
            screen.blit(menu_titles1[i],(int(variables["screen_width"] ) / 2 -variables["button_width"] - (variables["bigfont"], int(screen_height) / 4 + (variables["cell_size"] * i, variables["button_width"], (variables["bigfont"] )))))

            if variables["show_interface"] == 1:
                if variables["screen_width"] == 0:
                    for x in range(items_max):
                        for y in range(items_max): pg.draw.rect(screen, (cell_color), (int(variables["screen_width"] ) / 2 + (variables["cell_size"] * x, int(screen_height) / 4 + (variables["cell_size"] * y, (variables["cell_size"], (variables["cell_size"] ), 2, 0, (variables["button_border_radius"], (variables["button_border_radius"], (variables["button_border_radius"], (variables["button_border_radius"] ))))))))) #drawing a inventory cells
                               
                    pg.draw.rect(screen      , ( Button_frame_color  ) , ( int(variables["screen_width"] ) / 2 +(variables["cell_size"] * 0 , int(screen_height) / 4 +(variables["cell_size"] * active_button1 ,(variables["cell_size"] ,(variables["cell_size"] ) , 2 , 0 ,(variables["button_border_radius"] ,(variables["button_border_radius"] ,(variables["button_border_radius"] , variables["button_border_radius"])))))))) #drawing a inventory cell_frame for a selected item in inventory
                
                    screen.blit(lists["hero_inventory"][item], (int(screen_width) / 2, int(screen_height) - (variables["cell_size"] * 2))) #drawing a title of the item in inventory            
                
                if variables["screen_width"] == 1:                
                    for i in range(len(variables["menus_dir"]) // variables["crafts_on_page"]):
                            Button = pg.draw.rect(screen, (Button_color), (int(variables["screen_width"] ) / 2 + (variables["bigfont"], int(screen_height) / 4 - (variables["bigfont"] + i * 40 +(variables["bigfont"] / 2, variables["button_width"], variables["bigfont"]), 0, 0, (variables["button_border_radius"] ,(variables["button_border_radius"] ,(variables["button_border_radius"] , variables["button_border_radius"])))))))
                            
                            pg.draw.rect(screen, (Button_frame_color), (int(variables["screen_width"] ) / 2 + (variables["bigfont"], int(screen_height) / 4 - (variables["bigfont"] + active_button1 * 40 +(variables["bigfont"] / 2 ,variables["button_width"], variables["bigfont"]), 2, 0, (variables["button_border_radius"], (variables["button_border_radius"], (variables["button_border_radius"], (variables["button_border_radius"]))))))))
                            screen.blit(new_craft, (int(variables["screen_width"] ) / 2 + (variables["bigfont"] + variables["button_width"] - (variables["cell_size"], int(screen_height) / 10 + i * 40 , 100 ,(variables["bigfont"] )))))



def Open_unit_inventory():
    if vihicle_sit == 1:
        for x in range(items_max):
            for y in range(items_max):
                pg.draw.rect(screen, (cell_color),(int(variables["screen_width"])  / 4 + (variables["cell_size"] * x, int(screen_height) / 4 + (variables["cell_size"] * y, (variables["cell_size"] ,(variables["cell_size"]), 2, 0, (variables["button_border_radius"], (variables["button_border_radius"], (variables["button_border_radius"], (variables["button_border_radius"] ))))))))) #drawing a inventory cells
                pg.draw.rect(screen, (Button_frame_color),(
                     int(variables["screen_width"] )  / 4 +(variables["cell_size"] * 0,
                     int(screen_height) / 4 +(variables["cell_size"] * active_button1 ,(variables["cell_size"] ,(variables["cell_size"] ) , 2 , 0 ,(variables["button_border_radius"] ,(variables["button_border_radius"] ,(variables["button_border_radius"] , variables["button_border_radius"]))))))))#drawing a inventory cell_frame for a selected item in inventory
            screen.blit(lists["hero_inventory"][item] , (int(screen_width ) / 2 ,   int(screen_height) -(variables["cell_size"]     * 2  ))) #drawing a title of the item in inventory            
                


def Trade_menu():
    obj_dir = os.listdir('Objects/')
    menu_titles    = [obj_dir[i] for i in range(len(obj_dir))]
        
    menu_titles1   = []
    menu_title_num = 0
    menu_title     = menu_titles[menu_title_num]
    for i in menu_titles: i = big_font.render(menu_titles[i].split(',')[0].strip() , False , small_font_color ) ; menu_titles1.append(i)   

        
    for i in range(len(menu_titles1)):            
            Button = pg.draw.rect(screen, (Button_color), (int(variables["screen_width"]) / 2 - variables["button_width"] - (variables["bigfont"], int(screen_height) / 4 + (variables["cell_size"] * i, variables["button_width"], variables["cell_size"]), 0, 0, (variables["button_border_radius"], (variables["button_border_radius"], (variables["button_border_radius"], variables["button_border_radius"]))))))
            pg.draw.rect(screen, (Button_frame_color), (int(variables["screen_width"] ) / 2 -variables["button_width"] - (variables["bigfont"], int(screen_height) / 4 + (variables["cell_size"] *variables["screen_width"], variables["button_width"], (variables["cell_size"]), 2, 0, (variables["button_border_radius"], (variables["button_border_radius"] ,(variables["button_border_radius"] , variables["button_border_radius"]))))))) #drawing a inventory cell_frame for a selected item in inventory
            
            screen.blit(menu_titles1[i], (int(variables["screen_width"] ) / 2 - variables["button_width"] - (variables["bigfont"], int(screen_height) / 4 + (variables["cell_size"] * i, variables["button_width"], (variables["bigfont"])))))
    
    for i in range(len(variables["menus_dir"]) // variables["crafts_on_page"]):
                        Button = pg.draw.rect(screen, (Button_color), (int(variables["screen_width"] ) / 2 +(variables["bigfont"], int(screen_height) / 4 - (variables["bigfont"] + i * 40 + (variables["bigfont"] / 2 ,variables["button_width"], variables["bigfont"]), 0, 0, (variables["button_border_radius"] ,(variables["button_border_radius"] ,(variables["button_border_radius"] , variables["button_border_radius"])))))))
                        
                        pg.draw.rect(screen, (Button_frame_color), (int(variables["screen_width"] ) / 2 + (variables["bigfont"], int(screen_height) / 4 - (variables["bigfont"] + active_button1 * 40 + (variables["bigfont"] / 2, variables["button_width"], variables["bigfont"]), 2, 0, (variables["button_border_radius"], (variables["button_border_radius"] ,(variables["button_border_radius"] ,(variables["button_border_radius"] ))))))))
                        
                        screen.blit(new_craft,(int(variables["screen_width"]  / 2 + variables["bigfont"]),int(screen_height / 10 + i * 40)))


    for i in range(len(prices_list1)) :screen.blit(prices_list1[i], (int(variables["screen_width"]) / 2 + int(variables["bigfont"]) + variables["button_width"] / 2,int(screen_height) / 2 - int(screen_height) / 4 - variables["bigfont"] + i * 40 + variables["bigfont"] / 2))

def toggle_main_menu():
        draw_menu()
        for i in range(len(os.listdir(variables["menus_dir"]))):
            pg.draw.rect(screen , (Button_color), (int(variables["screen_width"] ) /  2 -variables["button_width"] / 2, int(screen_height) / 2 - int(screen_height) / 4 - (variables["bigfont"] + i * 40 + (variables["bigfont"] / 2, variables["button_width"], (variables["bigfont"] + 5 ), 0, 0, (variables["button_border_radius"], (variables["button_border_radius"], (variables["button_border_radius"], variables["button_border_radius"])))))))
            pg.draw.rect(screen , (Button_frame_color), (
            int(variables["screen_width"] ) /  2 -variables["button_width"]/ 2, 
            int(screen_height) / 2 - int(screen_height) / 4 -(variables["bigfont"] +variables["screen_width"] * 40 +(variables["bigfont"] / 2 ,variables["button_width"], 
            (variables["bigfont"] + 5 ), 2, 0, (variables["button_border_radius"], (variables["button_border_radius"], (variables["button_border_radius"] , variables["button_border_radius"])))))))    
            screen.blit(show_mods_count, (int(variables["screen_width"] ) /  2 -variables["button_width"] / 2 + 75, int(screen_height) / 2 - int(screen_height) / 4 -(variables["bigfont"] + 3 * 40 +(variables["bigfont"] / 2 ,variables["button_width"],(variables["bigfont"] )))))


def toggle_mods_menu():
    if game_state == 'toggle_mods_menu':
        for i in range(len(dirs_dict["mods_dir_path"])):
            Button = pg.draw.rect(screen, (Button_color), (int(variables["screen_width"]) /  2 - variables["button_width"] / 2, int(screen_height) / 2 - int(screen_height) / 4 - (variables["bigfont"] + i * 40 + (variables["bigfont"] / 2 , variables["button_width"],(variables["bigfont"] + 5 ) , 0 , 0 ,(variables["button_border_radius"] ,(variables["button_border_radius"], (variables["button_border_radius"], variables["button_border_radius"])))))))            
            screen.blit(dirs_dict["mods_dir_path"][i], (int(variables["screen_width"] ) /  2 -variables["button_width"]/ 2, int(screen_height) / 2 - int(screen_height) / 4 - (variables["bigfont"] + i * 40 + (variables["bigfont"] / 2 ,variables["button_width"],(variables["bigfont"] )))))
            pg.draw.rect(screen, (Button_frame_color), (int(variables["screen_width"] ) /  2 -variables["button_width"] / 2, int(screen_height) / 2 - int(screen_height) / 4 - (variables["bigfont"] + variables["screen_width"] * 40 + (variables["bigfont"] / 2, variables["button_width"],(variables["bigfont"] + 5 ) , 2 , 0 , (variables["button_border_radius"] ,(variables["button_border_radius"] ,(variables["button_border_radius"] , variables["button_border_radius"])))))))


def text_updating(): 
    global new_craft,new_quest,checkpoints_list,achievements_list,hero_inventory_nums,show_game_state,ok
    global apply,cancel,action_counter,checkpoints_file1,dialoge_started,achievements_file1,checkpoint_size,dialoge_num,action,checkpoint_num
    global titles_list,menus_dir
    global vol_limit,frame1,frame2
    global fuel,listen_midi,frame1,frame2


    hero_inventory = [] ; hero_inventory_nums = [] ; hero_inventory_file_name = 'txt/langs/' + str(variables["language"]) + '/Hero inventory.txt' ; hero_inventory_file_mode = 'r' ; hero_inventory_file = open (hero_inventory_file_name , hero_inventory_file_mode , encoding= "utf-8") ; hero_inventory_file1 = hero_inventory_file.readlines()
    
    
    text = "Пример"
    text_surface = big_font.render(text, True, (255, 255, 255))  # белый текст
    rotated_surface = pg.transform.rotate(text_surface, variables["fuel"])  # поворот на 45 градусов
    rect = rotated_surface.get_rect(center=(200, 550))
    screen.blit(rotated_surface, rect)

    titles_list = []
    for i in os.listdir(variables["menus_dir"]) :
            i = big_font.render(str(i)  , False , small_font_color ) ; titles_list.append(i)

    new_craft = small_font.render('Uus' , False , small_font_color ) ; ok = small_font.render('OK' , False , small_font_color ) ; apply = small_font.render('Apply'  , False , small_font_color) ; cancel = small_font.render('Tagasi'  , False , small_font_color)
    show_game_state = big_font.render('Menüü' , False , small_font_color)

    import pyaudio, numpy as np

    pa = pyaudio.PyAudio()
    stream = pa.open(format=pyaudio.paInt16, channels=1, rate=44100,input=True, frames_per_buffer=1024)

    data = np.frombuffer(stream.read(1024), dtype=np.int16)
    vol_limit = 400
    volume = np.abs(data).mean()
    print(f" Громкость микрофона : int({volume})")
    if volume > vol_limit :
        print(f" ГРОМКО! : int({volume})")


        print("доступные миди устройства: ")
        
        for num, i in enumerate(mido.get_input_names()):
            print(f"устройство {num} : {i}")# можно выбрать по индексу или строке
        print()

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
                            variables["fuel"] += 1
                            print(f"variables['fuel']: {variables["fuel"]}")
                        
                        if msg.type == "note_on" and msg.note == 55:
                                print(f"включаем {port_name}")
                                listen_midi = 1
                                time.sleep(1)

                        if msg.type == "note_on" and msg.note == 55:
                                print(f"выключаем {port_name}")
                                listen_midi = 0
                                time.sleep(1)






"""        


            #for i in range(len(checkpoints_file1)) : pg.draw.circle(screen , (255 , 0 , 0 ) , (-camera.rect[0] + int(checkpoints_file1[i].split(',')[0]) + 50 , -camera.rect[1] + int(checkpoints_file1[i].split(',')[1]) + 180) , 50 , 1 )

        #for i in range(len(custom_checkpoints_list_x)):
        #    if len(custom_checkpoints_list) != 0:
        #        pg.draw.circle(screen , (255 , 0 , 0)      , ( -variables["camera1"].rect[ 0 ] + int(custom_checkpoints_list_x[i]) , -variables["camera1"].rect[ 1 ] + int(custom_checkpoints_list_y[i])      ) , 20  , 5 )
        #        screen.blit(custom_checkpoint_title        , ( -variables["camera1"].rect[ 0 ] + int(custom_checkpoints_list_x[i]) , -variables["camera1"].rect[ 1 ] + int(custom_checkpoints_list_y[i]) - 50 ))
        #        mini_map_surf.blit(custom_checkpoint_title , ( -variables["camera1"].rect[ 0 ] + int(custom_checkpoints_list_x[i]) , -variables["camera1"].rect[ 1 ] + int(custom_checkpoints_list_y[i]) - 50 ))









cam_num1 =0

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
#Settings.py imports
import pygame as pg , datetime ; import os , math , logging ;import sys ; import sqlite3 
import  getpass ;import random
from pathlib import Path

#custom modules import
import LogsManager

# path to Scripts/Python
sys.path.append(str(Path(__file__).resolve().parent))

pg.init() ; pg.font.init()





pos = pg.mouse.get_pos()

dirs_dict = {

"mods_dir_path" : 'mods',

"menus_dir" : 'txt/menus/',

"obj_dir"   : 'Objects/',

"MyShapes" : [],

#"Wallpapers_dir" : os.listdir('Wallpapers/' + str("screen_width") + '_' + str("screen_height") + '/'),

"languages"      : os.listdir('txt/langs/'),

}



#measure_units
measure_units = { 

                "meter" : 100 ,
                "km" : 100 * 1000, 
                "cm" : 1,
                "inch" : 2.54,
                "feet" : 30.48,
                "mile_in_km" : 1000 * 1.60934

                }


variables = {

"switchers":{

                "show_interface"    : 1,
                "open_backpack"     : 0,
                "show_hero_stats"   : 1, 
                "show_units"        : 1,
                "show_map"          : 1 ,
                "show_buildings"    : 1, 
                "show_items"        : 1,
                "show_islands"      : 0,

                "dark_level"        : 0,
                "max_dark_level"    : 100,

                "volume_levels"     : 10,
                "settings_values"   : 5,
                "bg_num"            : 1,
                "mags"              : 3,

                "map_scale"         : 1, 
                "map_size"          : 3,

                "show_hero_stats"   : 1,

                "unit_moving"       : 1,
                "unit_speed"        : 0,
                "unit_speed1"       : 0,
                "max_unit_speed"    : 4,

                "max_dark_level"    : 100,
                "volume_levels"     : 10,
                "settings_values"   : 5,
                "fuel"              : 50,
                "gas"               : 0,

                "cell_size"         : 50,
                "cells"             : 5,


                "font_name"         :'arial',

                "scrensurfs"        : 4

},

"nums":{

            "health_icon_num"    : 0,
            "cancel_icon_num"    : 0,
            "sound_icon_num"     : 0,
            "ammo_icon_num"      : 0,
            "armor_icon_num"     : 0,
            "radiation_icon_num" : 0,
            "energy_icon_num"    : 0,    

},

"bg_num" : 1,

"land_color" : (162, 101, 62),

"BG_COLOR" : (0, 0, 200),

"dots_num"   : 36,
"rocks_num"  : 36,


"rock_size"  : 70,

"rock_scale" : 2,

"sea_scale" : 2,
"sea_size"  : 200,

"map_width" :  measure_units["meter"] * measure_units["km"],
"map_height" : measure_units["meter"] * measure_units["km"],


"lang_num"         : 2 ,

"dark_surf_color"  : "colors"[1] ,
"quest_surf_color" : "colors"[1],

"bigfont"          : 30,
"smallfont"        : 15,

"custom_checkpoint_size" : 100,
"custom_checkpoint_num"  : 0,

"vector" : [ 0 , 0],#cam vectors

"multiplayer"  : 1,
"hide_nicknames" : 0,

"ground" : 1,
"floor" : 0 ,

"fuel_bar_width" : 100,

"mouse_horizontal_offset" :5,
"mouse_vertical_offset" : 5 ,
"mouse_visible" : False ,

"mods_dir_path" : 'mods',
"saving_type" : 'Default',
"game_state" : 'Main_menu',

"lang_num" : 2,
#"language": dirs_dict["languages"]["lang_num"],
"update_name"  : 'Fear in the dark',
"author" : 'Thunderman98',
"subtitles" : 0,

"map_scale" : 1,
"map_size" : 3 ,
"keys" : pg.key.get_pressed(),

"minimap_grid_width"  : 100,
"minimap_grid_height" : 100,
"min_map_size"       : 3 ,
"max_map_size"       : 1.2, 
"map_scale" : 1,

"mini_map_grid_cell_size" : measure_units["meter"] *" map_scale",

"cursor_types" : ['Default' , 'Custom'], 
"cursor_num" : 0 ,
#"cursor_type" : "cursor_types"[cursor_num],

"hero_inventory_types" : ['Grid' , 'Circle'] , 
"hero_inventory_num" : 0 , 
#"hero_inventory_type" : "hero_inventory_types"[hero_inventory_num] ,
"hero_marker_color" :(255 , int(255 / 2) , 0),

"room_height" : 3 * measure_units["meter"],
"room_width" : 3 *measure_units["meter"]  , 
"room_size" : room_height * "room_width" ,
"walll_size"  : 22,

"sidewalk_width" : 3 * 100, 
"sidewalk_height": 3 * ["measure_units"]["meter"],


"font_name" : 'arial' ,
"bigfont" : 30,
"big_font_color" : ( 250 , 0 , 0 ) , "change_font_color" : ( 0 , 250 , 0 ) ,"big_font" :pg.font.SysFont("font_name" , "bigfont"),

"smallfont" : 15,
"small_font_color"  : ( 250 , 0 , 0 ) , "small_font" : pg.font.SysFont("font_name" , "smallfont"),

"cursor_x"             : pos[0],
"cursor_y"             : pos[1],

"item_offset"          : 0,
"active_button"        : 0,
"active_button1"       : 0,
"crafts_on_page"       : 10,
"characters_on_page"   : 10,
"players_on_page"      : 10,
"button_width"         : 250,
"button_height"        : "bigfont",
"button_border_radius" : 5,


"minimap_horizontal_offset" : 0,
"minimap_vertical_offset"   : 0,
"fov"                       : 100,
"minimap_opacity"           : 0,
"interface_opacity"         : 0,

"game_state_x"        : int("screen_width") / 2 - int(len("game_state") * "bigfont" / 3),
"game_state_y"        : 100,
"game_title_x"        : 100 ,
"game_title_y"        : 100,
"Game_version_x"      : 10,
"Game_version_y"     : int("screen_height") - "bigfont",
"Game_Author_x"       : 10,
"Game_Author_y"       : int("screen_height") - "bigfont", 
"Game_created_date_x" : 10,
"Game_created_date_y" : 10 ,
"Game_update_x"       : 10,
"Game_update_y"       : 10 ,
"wallpaper"      : dirs_dict["wallpapers_dir"]["bg_num"],   

}



lists = {
"colors" : [ 
                       
                       (0, 0, 255), 
                       (0, 0, 0 ),
                       (250, 0, 0), 
                       (255, 255, 255), 
                       (45, 45, 45), 
                       (133, 133, 133), 
                       (100, 100, 100), 
                       (75, 75, 75) 
                       
],

"Colors_list"         : [],
"Colors_Coords_x_1"   : [],
"Colors_Coords_x_2"   : [],
"Colors_Coords_y_1"   : [],
"Colors_Coords_y_2"   : [],

"MyShapes"            : [],
"main_menu"           : [],
"actions_list"        : [], 
"settings"            : [],

"dots"                : [],
"rocks"               : [],

"cam_list"            : [random.randint(0,100) for i in range(0,10)],

"custom_checkpoints_list"   : [],
"custom_checkpoints_list_x" : [],
"custom_checkpoints_list_y" : [],

"islands_list"              : [],
"islands_images"            : [],

"roads_list"                : [],
"saves_list"                : [],

"quests_list"                 : [],
"quests_states_list"          : [],

"fuel_values_list"  : [],
"fuel_values_list1" : [],

"interface_images" : [],

"necessary_craft_items" : [],

"prices_list"  : [],
"prices_list1" : [] ,

"screen_surfs_list" :[ pg.Surface(( int(screen_width) / 2 , int(screen_height) / 2 )) for screensurf in range("scrensurfs")],

"hero_inventory"    : [] ,
"hero_inventory_nums" :[] ,

"game_modes" : ['Survival' , 'God mode' , 'Hardcore'],
"game_modes1" : [] 

}

back_btn       = pg.K_ESCAPE
save_game_btn  = pg.K_F5
backpack_btn   = pg.K_b
load_game_btn  = pg.K_F3
screenshot_btn = pg.K_F1
reload_btn     = pg.K_r

bindings_list = {

"custom": {},

"default": {

back_btn       : pg.K_ESCAPE,
save_game_btn  : pg.K_F5,
backpack_btn   : pg.K_b,
load_game_btn  : pg.K_F3,
screenshot_btn : pg.K_F1,
reload_btn     : pg.K_r    

}

}





files_dict = {

    "screen_file_name"         : 'txt/screen.txt',

    "islands_file_name"        : 'txt/Objects/' + str("saving_type") + '/Islands.txt',
    "quests_file_name"         : 'txt/langs/'   + str("language")     + '/Quests.txt', 
    "actions_file_name"        : 'txt/langs/' + str("language") + '/Actions.txt',


    "hero_file_name"           : 'txt/Objects/'+ str("saving_type") +'/characters/Hero.txt', 
    "roads_file_name"          : 'txt/Objects/' + str("saving_type") + '/Roads.txt',
    "settings_file_name"       : 'txt/langs/' + str("language") + '/Settings.txt' , 
    "hero_inventory_file_name" : 'txt/langs/' + str("language") + '/Hero inventory.txt',

    "Colors_file_name"         : 'txt/Colors.txt',
    "main_menu_file_name"      : 'txt/langs/' + str("language") + '/Main menu.txt', 
    "prices_file_name"         : 'txt/Prices.txt',
    "saves_file_name"          : 'txt/saves/' + str("saving_type") + '/2023 - 8 - 10/0.txt',

    "game_modes_file"          : open('txt/menus/Game_modes.txt','r'),
    "difficulties_modes_file"  : open('txt/menus/difficulties.txt','r'),

    "Colors_file_mode"         : 'r' ,
    "islands_file_mode"        : 'r',
    "roads_file_mode"          : 'r',
    "saves_file_mode"          : 'r',
    "hero_file_mode"           : 'r',
    "actions_file_mode"        : 'r',
    "main_menu_file_mode"      : 'r' ,
    "settings_file_mode"       : 'r',
    "hero_inventory_file_mode" : 'r',
    "hero_file"                : open ("hero_file_name , hero_file_mode"), 
    "prices_file_mode"         : 'r'  ,
    "quests_file_mode"         : 'r',
    "screen_file_mode"         : 'r',


    "Colors_file"              : open ("Colors_file_name"    , "Colors_file_mode"),
    "islands_file"             : open ("islands_file_name"   , "islands_file_mode"),
    "roads_file"               : open ("roads_file_name"     , "roads_file_mode"),
    "saves_file"               : open ("saves_file_name"     , "saves_file_mode"),
    "actions_file"             : open ("actions_file_name"   , "actions_file_mode"   , encoding= "utf-8"),
    "main_menu_file"           : open ("main_menu_file_name" , "main_menu_file_mode" , encoding = "utf-8"),
    "settings_file"            : open ("settings_file_name"  , "settings_file_mode"  , encoding = "utf-8"),
    "quests_file"              : open ("quests_file_name"    , "quests_file_mode"    , encoding = "utf-8"),

    "islands_file1"            : "islands_file".readlines(),
    "Colors_file1"             : "Colors_file".readlines(),

    "roads_file1"              : "roads_file".readlines(),
    "saves_file1"              : "saves_file".readlines(),
    "game_modes_file1"         : "game_modes_file".readlines(),
    "actions_file1"            : "actions_file".readlines() ,
    "main_menu_file1"          : "main_menu_file".readlines(),
    "quests_file1"             : "quests_file".readlines(),
    "hero_file1"               : "hero_file".readlines(),
    "settings_file1"           : "settings_file".readlines(),
    "hero_inventory_file1"     : "hero_inventory_file".readlines(),
    "screen_file1"             : "screen_file".readlines(),
    "prices_file1"             : "prices_file".readlines(),


    "hero_inventory_file"      : open ("hero_inventory_file_name" , "hero_inventory_file_mode" , encoding= "utf-8"),
    "prices_file"              : open("prices_file_name" , "prices_file_mode" , encoding= "utf-8"),

    "screen_file"              : open ("screen_file_name" , "screen_file_mode") ,


"config":{}, "db_querries":{}   }

fonts={"defalt":{},"custom":{}}

for i in files_dict["screen_file1"]: screen_width , screen_height , camera_x , camera_y = i.split(',')[0],i.split(',')[1],i.split(',')[2],i.split(',')[3]
for i in files_dict["saves_file1"]:  screen_width , screen_height , camera_x , camera_y = i.split(',')[0],i.split(',')[1],i.split(',')[2],i.split(',')[3]

surfs_dict={

"checkpoints_surf" : pg.Surface(( int(screen_width) / "map_size" , int(screen_height) / "map_size" )),
"hero_shadow_surf" : pg.Surface(( 100 , 100 )),
"mini_map_surf"    : pg.Surface(( int(screen_width) / "map_size" , int(screen_height) / "map_size" )), 
"quests_surf"      : pg.Surface(( 200 , 200 )),
"dark_surf"        : pg.Surface(( int(screen_width) , int(screen_height) )), 
"interface_surf"   : pg.Surface(( 200 , 200 )),
"dialoge_surf"     : pg.Surface((  100 , "bigfont" * len("actions_list") - "bigfont"))

}


screen  = pg.display.set_mode((int( screen_width) , int(screen_height)),pg.RESIZABLE)

#Game directory
cwd = os.getcwd()
game_icon = pg.display.set_icon(pg.image.load("Interface/icons/Game icons/Game_icon.png"))
d1 =  datetime.datetime.today()
d1 += datetime.timedelta( hours = 0 )

Game_title = os.path.basename(cwd)
Game_version = d1.date()
pg.display.set_caption(Game_title)


if "mods_dir_path" not in sys.path : sys.path.append("mods_dir_path")
if "mods_dir_path" in sys.path : print() ; print() ; print('mods folder added ! ')



big_font   = pg.font.SysFont("font_name" , "bigfont")
small_font = pg.font.SysFont("font_name" , "smallfont")
big_font   = pg.font.Font( None , 30)
small_font = pg.font.Font( None , 15)

interface_surf_x   = 0   ; interface_surf_y    = int("screen_height" ) - "interface_surf".get_width() 
interface_surf_x   = 0   ; interface_surf_y    = int("screen_height" ) - "interface_surf".get_width()

hero_checkpoint_offset_x = 0 ; hero_checkpoint_offset_y = 0 ; toggle_checkpoints = 1

big_font_color = ( 250 , 0 , 0 ) ; small_font_color  = ( 250 , 0 , 0 ) ; change_font_color = ( 0 , 250 , 0 )

#actions_list.append(i)

#action_num = 0 ; action_counter = 0 ; action = actions_list[action_num]

for i in range(variables["switchers"]) :
    show_game_title           = big_font.render(str(Game_title) , False , big_font_color)
    show_game_version         = small_font.render('Version : ' + str(Game_version) , False , small_font_color)
    show_update               = small_font.render(str(variables["update_name"]) , False , small_font_color)
    show_game_state           = big_font.render(str(variables["switchers"]["game_state"]) , False , small_font_color)
    show_author               = small_font.render('Author : ' + str(variables["author"]) , False , small_font_color)
    show_created_date         = small_font.render('Created : 25 oktober 2019' , False , small_font_color)
    show_action               = big_font.render(str(variables["action"]) , False , ( 250 , 0 , 0 ) )
    show_action1              = big_font.render('Trade' , False , ( 250 , 0 , 0 ) )
    show_action2              = big_font.render('Repair' , False , ( 250 , 0 , 0 ))
    #show_gas                 = big_font.render('Gas   : ' + str(gas)            , False , small_font_color )
    show_fuel          = big_font.render('Fuel  : ' + str(variables["switchers"]["fuel"]) , False , small_font_color ) 
    show_mods_count = big_font.render("(" + str(len(os.listdir(variables["switchers"]["mods_dir_path"])) ) + ")" , False , small_font_color )

    custom_checkpoint_title1  = big_font.render('Custom checkpoint' , False , small_font_color ) 
    add = big_font.render('+' , False , small_font_color )
    remove = big_font.render('-' , False , small_font_color )
    new_craft = small_font.render('Create' , False , small_font_color )
    ok = small_font.render('OK' , False , small_font_color )
    apply = small_font.render('Apply' , False , small_font_color)
    cancel = small_font.render('Cancel' , False , small_font_color)
    new_quest  = big_font.render('!'   , False , small_font_color ) 
    buy        = big_font.render('Buy' , False , small_font_color )
    x          = big_font.render('x'   , False , small_font_color )
    for i in range(variables["switchers"]["variables"]["volume_levels"]):
        i += 1
        i = variables["switchers"]["lists"]["Colors_Coords_x_1"].append( i * 100)
        i = variables["switchers"]["lists"]["Colors_Coords_y_1"].append(400)

    for i in range(variables["switchers"]) :
        i += 1
        i = "Colors_Coords_x_2".append( i * 100)
        i = "Colors_Coords_y_2".append(500)


    #for i in range(len(resolutions_file1)) : i = big_font.render(resolutions_file1[i].strip() , False , small_font_color ) ; resolutions_list.append(i)
    for i in range(1000):"fuel_values_list".append(i)
    for i in range(len("fuel_values_list")) : 
        i = big_font.render(str("fuel_values_list[i]") , False , small_font_color )
        lists["fuel_values_list1"].append(i)


#for i in range(len(prices_list))  : i = big_font.render('Price : ' + prices_file1[i].strip() , False , small_font_color ) ; prices_list1.append(i)     
#for i in range(len(prices_file1)) : prices_list.append(prices_file1[i])


screen.blit("cursor" , ( "pos[ 0 ]" - "mouse_horizontal_offset" , "pos[ 1 ]"  - "mouse_vertical_offset" )) ; #calc_dist = math.sqrt( (( x_2_list - x_1_list   * hero_checkpoint_offset_x) ** 2 ) +  ( (  y_2_list - y_1_list * hero_checkpoint_offset_y) ** 2 ) /100) ; show_distance = small_font.render('Distance : ' + str(int(calc_dist) /100) + ' m' , False , small_font_color )

#surfs


#for i in range(10) : "MyShapes".append('circle') ; "MyShapes".append('square') ; "MyShapes".append('triangle') ; "MyShapes".append('rectangle')    

clock = pg.time.Clock() ; FPS = 60 ; clock.tick(FPS)

minimapfontsize = int( 30 / "map_scale") ; mini_map_font_size = pg.font.SysFont("font_name" , minimapfontsize)

#for i in custom_checkpoints_list:
#    i = mini_map_font_size.render('Custom checkpoint' + int(i) , False , small_font_color ) 

screen.blit("interface_surf" , ( interface_surf_x , interface_surf_y ))
screen.blit("quests_surf"   , ( int(screen_width) - "quests_surf".get_width() , int(screen_height ) - "quests_surf".get_height()))

game_mode_num = 0 ; game_mode = "game_modes_file1"[game_mode_num]
for i in range(len("game_modes")) : i = big_font.render("game_modes"[i].split(',')[0].strip() , False , small_font_color ) ; "game_modes1".append(i) 

menu_titles = ['Backpack' , 'Crafting' , 'Quests'] ; menu_titles1 = [] ; menu_title_num = 0 ; menu_title = menu_titles[menu_title_num]
for i in range(len(menu_titles)) : i = small_font.render(menu_titles[i].split(',')[0].strip() , False , small_font_color ) ; menu_titles1.append(i)     

difficulties = ['Peaceful' , 'Easy' , 'Normal' , 'Hard'] ; difficulties1 = [] ; difficulty_num = 0 ; difficulty = difficulties[difficulty_num]
for i in range(len(difficulties)) : i = big_font.render(difficulties[i].split(',')[0].strip() , False , small_font_color ) ; difficulties1.append(i)     


cam_list = [random.randint(0,100) for i in range(0,10)];print(f'Cam list : {cam_list}')



#print(os.listdir("mods_dir_path"))

minimap_location    =  'right_up'  ; minimap_x = 15 / 2 ; minimap_y = 15 / 2
if minimap_location == 'left_up'   : minimap_x = 0      ; minimap_y = 0
minimap_location    =  'left_up'   ; minimap_x = 15 / 2 ; minimap_y = 15 / 2
if minimap_location == 'left_down' : minimap_x = 0      ; minimap_y = 0

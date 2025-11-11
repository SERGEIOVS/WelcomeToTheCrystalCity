import pygame as pg , datetime ; from Units import * ; from Items import * ; import os , math , logging ;import sys ; import sqlite3 
import  getpass ;
pg.init() ; pg.font.init()

#Game directory
cwd = os.getcwd()
d1 =  datetime.datetime.today() ; d1 += datetime.timedelta( hours = 0 ) ; pos = pg.mouse.get_pos()
mods_dir_path = 'mods'
saving_type = 'Default' ; game_state = 'Main menu'

Game_title = os.path.basename(cwd) ; Game_version = d1.date() ; update_name  = 'Fear in the dark' ; author = 'Thunderman98' ; subtitles = 0 ; cursor_x = pos[0] ; cursor_y = pos[1] ; pg.display.set_caption(Game_title)
bigfont    = 30 ; smallfont = 15 ; font_name = 'arial' ; big_font_color = ( 250 , 0 , 0 ) ; small_font_color  = ( 250 , 0 , 0 ) ; change_font_color = ( 0 , 250 , 0 ) ; big_font = pg.font.SysFont(font_name , bigfont) ; small_font = pg.font.SysFont(font_name , smallfont)
languages  = os.listdir('txt/langs/') ; lang_num = 2 ; language = languages[lang_num]

logpaths    = ['logs/info_log.txt' , 'logs/debug_log.txt' , 'logs/warning_log.txt' , 'logs/critical_log.txt' , 'logs/error_log.txt']
log_levels  = [ logging.INFO , logging.WARNING , logging.ERROR , logging.CRITICAL , logging.DEBUG ]
log_formats = ['%(asctime)s - %(levelname)s - %(message)s' , '%(levelname)s - %(asctime)s - %(message)s']
logging.basicConfig(filename = logpaths[0] , level = log_levels[0] , format = log_formats[0])    #отключить протоколирование - logging.disable()
colors = [ ( 0 , 0 , 255 ) , ( 0 , 0 , 0 ) , (250 , 0 , 0)  , (255 , 255 , 255) , (45 , 45 , 45 ) , (133 , 133 , 133) , (100 , 100 , 100) , (75 , 75 , 75) ]

mags       = 3
map_scale  = 1 ; map_size = 3 ; show_map = 1 ; show_units = 1 ; show_buildings = 1 ; show_items = 1 ; show_interface = 1 ; open_backpack = 0 ; show_hero_stats = 1 ; unit_moving = 1 ; unit_speed = 0 ; unit_speed1 = 0 ; max_unit_speed = 4
dark_level = 0 ; max_dark_level  = 100 ; volume_levels = 10 ; settings_values = 5
fuel       = 50
gas        = 0
Colors_Coords_x_1 = [] ; Colors_Coords_y_1 = [] ; Colors_Coords_x_2 = [] ; Colors_Coords_y_2 = []
cell_size = 50
cells = 5
grid_size1 = int(100 / map_scale)
grid_size2 = int(100 / map_scale)

for i in range(volume_levels)   : i += 1 ; i = Colors_Coords_x_1.append( i * 100) ; i = Colors_Coords_y_1.append(400)
for i in range(settings_values) : i += 1 ; i = Colors_Coords_x_2.append( i * 100) ; i = Colors_Coords_y_2.append(500)

islands_file_name = 'txt/Objects/' + str(saving_type) + '/Islands.txt' ; islands_file_mode = 'r' ; islands_file = open (islands_file_name , islands_file_mode) ; islands_file1 = islands_file.readlines() ; islands_list = [] ; islands_images = []
roads_file_name   = 'txt/Objects/' + str(saving_type) + '/Roads.txt' ; roads_file_mode = 'r' ; roads_file = open (roads_file_name , roads_file_mode) ; roads_file1 = roads_file.readlines() ; roads_list = []
Colors_list       = [] ; Colors_file_name = 'txt/Colors.txt' ; Colors_file_mode = 'r' ; Colors_file = open (Colors_file_name , Colors_file_mode) ; Colors_file1 = Colors_file.readlines()
resolutions_list  = [] ; resolutions_file_name = 'txt/menus/Resolutions.txt' ; resolutions_file_mode = 'r' ; resolutions_file = open (resolutions_file_name , resolutions_file_mode) ; resolutions_file1 = resolutions_file.readlines()
saves_list        = [] ; saves_file_name = 'txt/saves/' + str(saving_type) + '/2023 - 8 - 10/0.txt' ; saves_file_mode = 'r' ; saves_file = open (saves_file_name , saves_file_mode) ; saves_file1 = saves_file.readlines()
custom_checkpoints_list = [] ; custom_checkpoints_list_x = [] ; custom_checkpoints_list_y = [] ; custom_checkpoint_size = 100 ; custom_checkpoint_num = 0

actions_list      = [] ; actions_file_name      = 'txt/langs/' + str(language) + '/Actions.txt' ; actions_file_mode = 'r' ; actions_file = open (actions_file_name , actions_file_mode , encoding= "utf-8") ; actions_file1 = actions_file.readlines() ; actions_list.append(i) ; action_num = 0 ; action_counter = 0 ; action = actions_list[action_num]
quests_list       = [] ; quests_states_list = [] ; quests_file_name = 'txt/langs/' + str(language) + '/Quests.txt' ; quests_file_mode = 'r' ; quests_file = open (quests_file_name , quests_file_mode , encoding = "utf-8") ; quests_file1 = quests_file.readlines()
main_menu         = [] ; main_menu_file_name = 'txt/langs/' + str(language) + '/Main menu.txt' ; main_menu_file_mode = 'r' ; main_menu_file = open (main_menu_file_name , main_menu_file_mode , encoding = "utf-8") ; main_menu_file1 = main_menu_file.readlines()
settings          = [] ; settings_file_name = 'txt/langs/' + str(language) + '/Settings.txt' ; settings_file_mode = 'r' ; settings_file = open (settings_file_name , settings_file_mode , encoding = "utf-8") ; settings_file1 = settings_file.readlines()
hero_file_name    = 'txt/Objects/'+ str(saving_type) +'/characters/Hero.txt' ; hero_file_mode = 'r' ; hero_file = open (hero_file_name , hero_file_mode) ; hero_file1 = hero_file.readlines()
hero_inventory    = [] ; hero_inventory_nums = [] ; hero_inventory_file_name = 'txt/langs/' + str(language) + '/Hero inventory.txt' ; hero_inventory_file_mode = 'r' ; hero_inventory_file = open (hero_inventory_file_name , hero_inventory_file_mode , encoding= "utf-8") ; hero_inventory_file1 = hero_inventory_file.readlines()
prices_file_name = 'txt/Prices.txt' ; prices_file_mode = 'r' ; prices_file = open(prices_file_name , prices_file_mode , encoding= "utf-8") ; prices_file1 = prices_file.readlines()



for i in range(len(resolutions_file1)) : i = big_font.render(resolutions_file1[i].strip() , False , small_font_color ) ; resolutions_list.append(i)

for i in saves_file1 : screen_width , screen_height , camera_x , camera_y = i.split(',')[0] , i.split(',')[1] , i.split(',')[2] , i.split(',')[3]
        
scrensurfs = 4
screen_surfs_list = [ pg.Surface(( int(screen_width) / 2 , int(screen_height) / 2 )) for screensurf in range(scrensurfs)]

screen  = pg.display.set_mode((int( screen_width) , int(screen_height)),pg.FULLSCREEN)




game_icon = pg.display.set_icon(pg.image.load("Interface/icons/Game icons/Game_icon.png"))

new_quest  = big_font.render('!'   , False , small_font_color ) ; add = big_font.render('+' , False , small_font_color ) ; remove = big_font.render('-' , False , small_font_color ) ; new_craft = small_font.render('Create' , False , small_font_color ) ; ok = small_font.render('OK' , False , small_font_color ) ; apply = small_font.render('Apply' , False , small_font_color) ; cancel = small_font.render('Cancel' , False , small_font_color)
buy        = big_font.render('Buy' , False , small_font_color ) ; add = big_font.render('+' , False , small_font_color ) ; remove = big_font.render('-' , False , small_font_color ) ; new_craft = small_font.render('Create' , False , small_font_color ) ; ok = small_font.render('OK' , False , small_font_color ) ; apply = small_font.render('Apply' , False , small_font_color) ; cancel = small_font.render('Cancel' , False , small_font_color)
x          = big_font.render('x'   , False , small_font_color ) ; add = big_font.render('+' , False , small_font_color ) ; remove = big_font.render('-' , False , small_font_color ) ; new_craft = small_font.render('Create' , False , small_font_color ) ; ok = small_font.render('OK' , False , small_font_color ) ; apply = small_font.render('Apply' , False , small_font_color) ; cancel = small_font.render('Cancel' , False , small_font_color)

show_fuel          = big_font.render('Fuel  : ' + str(fuel) , False , small_font_color ) ; add = big_font.render('+', False , small_font_color ) ; remove = big_font.render('-' , False , small_font_color ) ; new_craft = small_font.render('Create' , False , small_font_color ) ; ok = small_font.render('OK' , False , small_font_color ) ; apply = small_font.render('Apply' , False , small_font_color) ; cancel = small_font.render('Cancel' , False , small_font_color)
fuel_values_list  = []
fuel_values_list1 = []

for i in range(1000):fuel_values_list.append(i)
for i in range(len(fuel_values_list)) : 
    i = big_font.render(str(fuel_values_list[i]) , False , small_font_color )
    fuel_values_list1.append(i)

show_speed  = big_font.render('Speed : ' + str(hero_speed)     , False , small_font_color ) ; add = big_font.render('+', False , small_font_color ) ; remove = big_font.render('-' , False , small_font_color ) ; new_craft = small_font.render('Create' , False , small_font_color ) ; ok = small_font.render('OK' , False , small_font_color ) ; apply = small_font.render('Apply' , False , small_font_color) ; cancel = small_font.render('Cancel' , False , small_font_color)
show_gas    = big_font.render('Gas   : ' + str(gas)            , False , small_font_color )
custom_checkpoint_title1 = big_font.render('Custom checkpoint' , False , small_font_color ) 

show_mods_count = big_font.render("(" + str(len(os.listdir(mods_dir_path))) + ")" , False , small_font_color ) 

#measure units . linear measure . inch = 25,4 mm (2,54 cm) foot = 0,3048 m (or 12 inches) ; 
bg_num = 1 ; wallpapers_dir = os.listdir('wallpapers/' + str(screen_width) + '_' + str(screen_height) + '/') ; wallpaper = wallpapers_dir[bg_num] ;  dark_level = 0 ; show_interface = 1 ; open_backpack = 0 ; show_hero_stats = 1 ; meter = 100 ; cm = 1 ; km = meter * 1000 ; inch = 2.54 ; map_width , map_height = meter * km , meter * km ; map_scale = 1 ; map_size = 3 ; show_map = 1 ; show_units = 1 ; show_buildings = 1 ; show_items = 1 ; show_islands = 0 

#surfs
checkpoints_surf = pg.Surface(( int(screen_width) / map_size , int(screen_height) / map_size )) ; hero_shadow_surf = pg.Surface(( 100 , 100 )) ; mini_map_surf = pg.Surface(( int(screen_width) / map_size , int(screen_height) / map_size )) ; quests_surf = pg.Surface(( 200 , 200 )) ; dark_surf = pg.Surface(( int(screen_width) , int(screen_height) )) ; interface_surf = pg.Surface(( 200 , 200 )) ; dark_surf_color = ((0 , 0 , 0)) ; dialoge_surf = pg.Surface((  100 , bigfont * len(actions_list) - bigfont))


quest_surf_color = colors[1]
show_game_title = big_font.render(str(Game_title) , False , big_font_color) ; show_game_version = small_font.render('Version : ' + str(Game_version) , False , small_font_color) ; show_update = small_font.render(str(update_name) , False , small_font_color) ; show_game_state = big_font.render(str(game_state) , False , small_font_color) ; show_author = small_font.render('Author : ' + str(author) , False , small_font_color) ; show_created_date = small_font.render('Created : 25 oktober 2019' , False , small_font_color) ; show_money = small_font.render('$ : ' + str(hero_money) , False , ( 250 , 0 , 0 ) ) ; show_action = big_font.render(str(action) , False , ( 250 , 0 , 0 ) ) ; show_action1 = big_font.render('Trade' , False , ( 250 , 0 , 0 ) ) ; show_action2 = big_font.render('Repair' , False , ( 250 , 0 , 0 ))
hero_checkpoint_offset_x = 0 ; hero_checkpoint_offset_y = 0 ; toggle_checkpoints = 1

minimap_location    =  'right_up'  ; minimap_x = 15 / 2 ; minimap_y = 15 / 2
if minimap_location == 'left_up'   : minimap_x = 0      ; minimap_y = 0
minimap_location    =  'left_up'   ; minimap_x = 15 / 2 ; minimap_y = 15 / 2
if minimap_location == 'left_down' : minimap_x = 0      ; minimap_y = 0

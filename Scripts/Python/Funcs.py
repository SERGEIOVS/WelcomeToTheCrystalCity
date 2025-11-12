import pygame as pg
from Settings import *
import pyautogui
from time import *
import logging
from Units import *
from Vehicles import *
from Background import *
from Controls import room_height,scaled_image,rot_hero,fuel_bar_width,interface_surf_x,interface_surf_y,min_map_size,checkpoint_size,max_map_size,game_modes1,menus_dir,camera1,vihicles_file1,player_movement,menu_titles1,text_updating,Open_unit_inventory,minimap_grid_width,minimap_grid_height,hero_marker_color,mini_map_grid_cell_size,difficulties1,prices_file1,prices_list1,vector
pg.init()






#sounds
welcome_speech_dir = os.listdir('Audio/sounds/welcome/') ; enemy_sounds_dir = os.listdir('Audio/sounds/roar/') ; pickup_sounds_dir = os.listdir('Audio/sounds/pickup/')

sounds_dir = os.listdir('Audio/sounds/')

#music
soundtracks = os.listdir('Audio/enviroment/') ; switch_music = 1 ; music = soundtracks[switch_music] ; show_song_name = small_font.render(str(music) , False , ( 250 , 0 , 0 ) ) ; pg.mixer.music.load('Audio/enviroment/' + str(music)) ; minimap_border_offset = 10 ; minimap_object_offset = 0 ; minimap_object_offset1 = 0

step_sound_num     = 1 ; step_sound   = pg.mixer.Sound('Audio/sounds/steps/grass/'       + str(step_sound_num)   + '.mp3')
rifle_sound_num    = 0 ; rifle_sound  = pg.mixer.Sound('Audio/sounds/firegun/automatic/' + str(rifle_sound_num)  + '.mp3')
spawn_sound_num    = 0 ; spawn_sound  = pg.mixer.Sound('Audio/sounds/spawn/'             + str(spawn_sound_num)  + '.mp3')
scream_sound_num   = 0 ; scream_sound = pg.mixer.Sound('Audio/sounds/screams/far/'       + str(scream_sound_num) + '.mp3')
death_sound_num    = 0 ; death_sound  = pg.mixer.Sound('Audio/sounds/death/'             + str(death_sound_num)  + '.mp3')
pickup_sound_num   = 0 ; pickup_sound = pg.mixer.Sound('Audio/sounds/pickup/'            + str(pickup_sound_num) + '.mp3')
enemy_sound_num    = 0 ; enemy_sound  = pg.mixer.Sound('Audio/sounds/roar/'              + str(enemy_sound_num)  + '.mp3')
click_sound_num    = 0 ; click_sound  = pg.mixer.Sound('Audio/sounds/clicks/'            + str(click_sound_num)  + '.mp3')
welcome_num        = 0 ; welcome           = pg.mixer.Sound('Audio/speech/langs/'                   + str(language)           + '/welcome/' + str(int(welcome_num)) + '.mp3')
inv_full_sound_num = 0 ; inv_is_full_sound = pg.mixer.Sound('Audio/sounds/massages/Full inventory/' + str(inv_full_sound_num) +'.mp3')

bg_images   = []
for i in range(len(wallpapers_dir)) :
     if i not in bg_images : bg_images.append(pg.image.load( 'Wallpapers/' + str(screen_width) + '_' + str(screen_height) + '/' + str(i) + '.png'))

Icons_dir = os.listdir('Interface/Icons/')

for i in range(len(Icons_dir)) : pass

#icons
health_icon_num    = 0 ; health_icon    = pg.image.load('Interface/Icons/Health/'          + str(health_icon_num)    + '.png')
ammo_icon_num      = 0 ; ammo_icon      = pg.image.load('Interface/Icons/Ammo/'            + str(ammo_icon_num)      + '.png') 
armor_icon_num     = 0 ; armor_icon     = pg.image.load('Interface/Icons/Armor/'           + str(armor_icon_num)     + '.png')
radiation_icon_num = 0 ; radiation_icon = pg.image.load('Interface/Icons/Radiation/'       + str(radiation_icon_num) + '.png')
energy_icon_num    = 0 ; energy_icon    = pg.image.load('Interface/Icons/Energy/'          + str(radiation_icon_num) + '.png')
sound_icon_num     = 0 ; sound_icon     = pg.image.load('Interface/Icons/Music/'           + str(sound_icon_num)     + '.png')
cancel_icon_num    = 0 ; cancel_icon    = pg.image.load('Interface/buttons/cancel/'        + str(cancel_icon_num)    + '.png')

cancel_icon_x , cancel_icon_y = int(screen_width) - 50 , 50


item_offset = 0 ; active_button = 0 ; active_button1 = 0 ; crafts_on_page = 10 ; characters_on_page = 10 ; players_on_page = 10 ; button_width = 250 ; button_height = bigfont ; button_border_radius = 5


minimap_horizontal_offset = 0 ; minimap_vertical_offset = 0 ; fov = 100 ; minimap_opacity = 0 ; interface_opacity = 0 

Button_color = (45 , 45 , 45) ; minimap_border_color = (45 , 45 , 45) ; Button_frame_color = (255 , 0 , 0) ; cell_color = ( 45  , 45 , 45 )

game_state_x   = int(screen_width) / 2 - int(len(game_state) * bigfont / 3) ; game_state_y = 100
game_title_x   = 100      ; game_title_y        = 100
Game_version_x = 10       ; Game_version_y      = int(screen_height) - bigfont
Game_Author_x  = 10       ; Game_Author_y       = int(screen_height) - bigfont 
Game_created_date_x  = 10 ; Game_created_date_y = 10 
Game_update_x  = 10       ; Game_update_y       = 10 

back_btn = pg.K_ESCAPE ; save_game_btn = pg.K_F5 ; backpack_btn1 = pg.K_b ; backpack_btn2 = pg.K_b ; load_game_btn = pg.K_F3 ; screenshot_btn = pg.K_F1
reload_btn = pg.K_r

change_settings_value = 0 ; fps_1 = 4 ; 

def make_screenshot() :
    screenshots = 1 ; screenshot = pyautogui.screenshot() 
    for i in range(screenshots)  : screenshot.save( 'screenshots/' + str(d1.year) + ' - ' + str(d1.month) + ' - ' + str(d1.day) + ' - ' + str(d1.hour) + ' - ' +  str(d1.minute) + ' - ' + str(d1.second) + '.png' )

#def save_game_and_quit() :saves_file_mode = 'w' ; saves_file = open (saves_file_name , saves_file_mode) ; saves_file.write( str(screen_width) + ',' + str(screen_height) + ',' + str(camera.rect[0]) + ',' + str(camera.rect[1])) ; saves_file.close() ; logging.info(msg = 'GAME SAVED!' ) ; pg.quit() ; logging.info(msg = 'QUIT GAME!' )
def toggle_god_mode() : global print_god_mode , god_mode ; god_mode = 0 ; print_god_mode = print('GOD MODE ACTIVATED!')

#def load_game() : saves_file_mode = 'r' ; saves_file = open (saves_file_name , saves_file_mode) ; saves_file.close() ; logging.info(msg = 'GAME LOADED!' ) ; print('Game loaded!')
#def save_game() : saves_file_mode = 'w' ; saves_file = open (saves_file_name , saves_file_mode) ; saves_file.write( str(screen_width) + ',' + str(screen_height) + ',' + str(camera.rect[0]) + ',' + str(camera.rect[1])  );saves_file.close() ; logging.info(msg = 'GAME SAVED!' ) ; print('GAME SAVED!')

def draw_menu():
        screen.blit( bg_images[bg_num] , ( 0   , 0  ))
        screen.blit(show_game_title    , ( int(screen_width)  /  2 - len(Game_title)  * smallfont / 2  , 10))
        screen.blit( show_update       , ( int(screen_width)  /  2 - len(update_name) * smallfont / 2  , 50))    
        screen.blit(show_game_version  , (  10 , int(screen_height) - bigfont))
        screen.blit( show_author       , (  0  , 10 ))
        screen.blit( show_created_date , (  0  , 35 ))
        screen.blit( cancel_icon , ( cancel_icon_x,cancel_icon_y))
        game_state_x = int(screen_width) / 2 - int(len(game_state) * bigfont / 3) ; game_state_y = 100

vehicle_sit = 0


def start():
    global menus_dir,ground,land_color,dots,rocks


    if game_state == 'Saves':
        for i in range(len(saves_file1)):
            Button = pg.draw.rect(screen , (Button_color) , ( int(screen_width) /  2 - button_width / 2 , int(screen_height) / 2 - int(screen_height) / 4 - bigfont + i * 40 + bigfont /2 , button_width , bigfont + 5 ) , 0 , 0 , button_border_radius , button_border_radius , button_border_radius , button_border_radius)            
        #screen.blit(saves_list[i]                     , ( int(screen_width) /  2 - button_width / 2 , int(screen_height) / 2 - int(screen_height) / 4 - bigfont + i * 40 + bigfont / 2 , button_width , bigfont ))
        pg.draw.rect(screen , (Button_frame_color)    , ( int(screen_width) /  2 - button_width / 2 , int(screen_height) / 2 - int(screen_height) / 4 - bigfont + active_button * 40 + bigfont / 2 , button_width , bigfont + 5 ) , 2 , 0 , button_border_radius , button_border_radius , button_border_radius , button_border_radius)

    if game_state == 'Crafting':
        for i in range(len(menus_dir) // crafts_on_page) :
                
                #drawing a buttons for a crafts menu
                Button = pg.draw.rect(screen , (Button_color)       , ( int(screen_width) / 2 - button_width / 2 , int(screen_height) /10 + i * 40 , 500 , bigfont) , 2 , 0 , button_border_radius , button_border_radius , button_border_radius , button_border_radius)
                pg.draw.rect(screen          , (Button_frame_color) , ( int(screen_width) / 2 - button_width / 2  , int(screen_height) /10 + active_button * 40 , 500 , bigfont) , 2 , 0 , button_border_radius , button_border_radius , button_border_radius , button_border_radius )
                screen.blit(str(i)   , ( int(screen_width) / 2 - button_width / 2 + bigfont , int(screen_height) / 10 + i * 40 , 100 , bigfont ))
                screen.blit(new_craft        , ( int(screen_width) / 2 + - button_width / 2 - cell_size * 2 , int(screen_height) / 10 + i * 40 , 100 , bigfont ))


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

        if ground == 1:

            world_border = pg.draw.rect(screen , (Button_frame_color) , ( -camera1.rect[ 0 ] + 0 ,-camera1.rect[ 1 ] + 0 , map_width , map_width) , 10 , 0  )

            #islands
            for i in range(len(dots)):
                pg.draw.polygon(screen, land_color , dots)
                pg.draw.polygon(screen, (10,60,0) , rocks)



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
            

            
            quests_surf.fill((quest_surf_color))
                
            #drawing a road to the checkpoint
           # pg.draw.line(screen   , (0   , 0 , 0 ) ,    [ -camera.rect[0] + int(camera_x) + int(screen_width) / 2 + hero_checkpoint_offset_x , -camera.rect[ 1 ] + int(camera_y) + int(screen_height) / 2 + 100 + hero_checkpoint_offset_y ] , [ -camera.rect[ 0 ] + int(checkpoints_file1[0].split(',')[0]) , -camera.rect[ 1 ] + int(checkpoints_file1[0].split(',')[1])] , 1 )
                
            #segmented road to the checkpoint 
            #for i in range(int(calc_dist) // 10 )  : pg.draw.circle(screen , (255 , 0 , 0) , ( -camera.rect[0] + int(checkpoints_file1[0].split(',')[0]) + i * 10 , -camera.rect[1] + int(checkpoints_file1[0].split(',')[1]) - i * 10) , 1)        
                
            #drawing a circle at the hero x and hero y
            #if vihicle_sit == 0 : pg.draw.circle(screen , (255 , 0 , 0) , ( -camera.rect[0] + int(camera_x) + int(screen_width) / 2 + hero_checkpoint_offset_x , -camera.rect[1] + int(camera_y) + int(screen_height) / 2 + 100 + hero_checkpoint_offset_y) , checkpoint_size / 2 , 1 )
                
            #drawing a circle at the checkpoint x and checkpoint y
            #33pg.draw.circle(screen , (255 , 0 , 0)  , ( -camera.rect[0] + int(checkpoints_file1[0].split(',')[0]) , -camera.rect[1] + int(checkpoints_file1[0].split(',')[1])) , checkpoint_size , 1 )
            
            #draw_mini_map()

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

#run = True ; logging.info( msg = 'GAME STARTED!' )



bg_num     = 1 ; wallpapers_dir = os.listdir('Wallpapers/' + str(screen_width) + '_' + str(screen_height) + '/') ; wallpaper  = wallpapers_dir[bg_num]


#while run :

for i in enumerate(screen_surfs_list):
        print(f"screen surf : {i}")


if dark_level <= max_dark_level : dark_level += 0.01
    

for event in pg.event.get() :

        """
                #список доступных джойстиков
                joystick_count = pg.joystick.get_count()
                print(f"Найдено джойстиков: {joystick_count}")

                if joystick_count > 0:
                    joystick = pg.joystick.Joystick(0)
                    joystick.init()
                print(f"Использую: {joystick.get_name()}")

        if event.type == pg.JOYBUTTONDOWN:
            print(f"{event.button}")
            if event.button == 0:
                if welcome_num  < len(welcome_speech_dir) - 1 :

                    welcome_num += 0.5
                            
                else:
                    welcome_num = 0
                                
                    welcome = pg.mixer.Sound(f'Audio/speech/langs/{language}/welcome/{int(welcome_num)}.mp3')

                welcome.play()
        """
        # кнопки



        
    
    
mini_map_surf.fill((minimapBGcolor))
screen.fill( (BGcolor) )
    

#start()

    
if game_state != 'Play' : show_game_state = big_font.render(str(game_state) , False , small_font_color) ; screen.blit( show_game_state ,  (game_state_x , game_state_y))
    
for i in range(len(main_menu_file1)):
        if game_state == 'Main_menu' and pos[0] >= int(screen_width) / 2 - button_width / 2  and pos[0] <= int(screen_width) /  2 + button_width / 4 and pos[1] >= int(screen_height) / 2 - int(screen_height) / 4 - bigfont + i * 40 + bigfont / 2  and pos[1] <= int(screen_height) / 2 - int(screen_height) / 4 - bigfont + i * 40 + bigfont / 2 + button_height : active_button = i
        
for i in range(len(menus_dir)):
        if game_state == 'Crafting'  and pos[0] >= int(screen_width) / 2 - button_width / 2  and pos[0] <= int(screen_width) /  2 + button_width / 4 and pos[1] >= int(screen_height) / 2 - int(screen_height) / 4 - bigfont + i * 40 + bigfont / 2  and pos[1] <= int(screen_height) / 2 - int(screen_height) / 4 - bigfont + i * 40 + bigfont / 2 + button_height : active_button = i

for i in range(len(saves_file1)):
        if game_state == 'Saves'     and pos[0] >= int(screen_width) / 2 - button_width / 2  and pos[0] <= int(screen_width) /  2 + button_width / 4 and pos[1] >= int(screen_height) / 2 - int(screen_height) / 4 - bigfont + i * 40 + bigfont / 2  and pos[1] <= int(screen_height) / 2 - int(screen_height) / 4 - bigfont + i * 40 + bigfont / 2 + button_height : active_button = i
        
for i in range(len(Hero_types)):
        if game_state == 'character_select_menu' and pos[0] >= int(screen_width) / 2 - button_width / 2  and pos[0] <= int(screen_width) /  2 + button_width / 4 and pos[1] >= int(screen_height) / 2 - int(screen_height) / 4 - bigfont + i * 40 + bigfont / 2  and pos[1] <= int(screen_height) / 2 - int(screen_height) / 4 - bigfont + i * 40 + bigfont / 2 + button_height : active_button = i
        
for i in range(items_max):    
        if game_state == 'Trade_menu' and pos[0] >= int(screen_width) / 2 - button_width and pos[0] <= int(screen_width) /  2 + button_width / 4 and pos[1] >= int(screen_height) / 2 - int(screen_height) / 4 - bigfont + i * 40 + bigfont / 2  and pos[1] <= int(screen_height) / 2 - int(screen_height) / 4 - bigfont + i * 40 + bigfont / 2 + button_height : active_button = i
        
for i in range(len(game_modes1)):
        if game_state == 'game_mode_select' and pos[0] >= int(screen_width) / 2 - button_width / 2  and pos[0] <= int(screen_width) /  2 + button_width / 4 and pos[1] >= int(screen_height) / 2 - int(screen_height) / 4 - bigfont + i * 40 + bigfont / 2  and pos[1] <= int(screen_height) / 2 - int(screen_height) / 4 - bigfont + i * 40 + bigfont / 2 + button_height : active_button = i
    
for x in range(minimap_grid_width):
        for y in range(minimap_grid_height):
            pg.draw.rect(mini_map_surf , (cell_color) , ( cell_size * x , cell_size * y , cell_size , cell_size ) , 2 , 0 , button_border_radius , button_border_radius , button_border_radius , button_border_radius ) #drawing a inventory cells



def draw_mini_map():
    if show_map == 1:
        for i in range( len ( islands_file1 ) ) :
            for y in range( len ( islands_file1 ) ) :
                pg.draw.rect(mini_map_surf , (100 , 50 , 0) , ( meter * 30 / (meter * map_scale) , meter * 30  / (meter / map_scale) , km * 5 / (meter * map_scale) , km * 5 / (meter * map_scale) ))

        for i in range( len ( buildings_file1 ) ) :
             if show_buildings == 1 : pg.draw.rect(mini_map_surf , (133 , 133 , 133)  , ( int(buildings_file1[ i ].split(',')[0]) / (100 * map_scale) + minimap_border_offset * 2 , int(buildings_file1[ i ].split(',')[1]) / (100 * map_scale) + minimap_object_offset1 * 2 ,  10 / map_scale, 10 / map_scale ))
        
        for i in range( len ( vihicles_file1 ) ) : pg.draw.rect(mini_map_surf , (0 , 0 , 0) , (int(vihicles_file1[i].split(',')[0]) / (100 * map_scale) + minimap_border_offset * minimap_object_offset , int(vihicles_file1[i].split(',')[1]) / (100 * map_scale) + minimap_border_offset * minimap_object_offset1 , 5 / map_scale , 3 / map_scale ))
        

        hero_marker = pg.draw.circle(mini_map_surf , ( hero_marker_color )        , ( minimap_border_offset + camera1.rect[0] / (100 * map_scale) + minimap_border_offset * minimap_object_offset ,  camera1.rect[1] / (100 * map_scale) + minimap_border_offset * minimap_object_offset1  ) , 1 / map_scale )        
        
        for i in range(len(custom_checkpoints_list_x)) : pg.draw.circle(mini_map_surf , (255 , 0 , 0) , ( int(custom_checkpoints_list_x[i]) / (100 * map_scale ) , int(custom_checkpoints_list_y[i]) / (100 * map_scale)) , int(1 / map_scale)  , int(1 / map_scale) )

        screen.blit(mini_map_surf , ( minimap_x , minimap_y ) )
        
        pg.draw.rect(screen , (minimap_border_color) , ( 0 , 0 , int(screen_width) / map_size + minimap_border_offset , int(screen_height) / map_size + minimap_border_offset ) , minimap_border_offset , minimap_border_offset)
        

        #for i in range(len(MyShapes)):
        #    if 'circle'in MyShapes:pg.draw.circle(screen  , (255, 255,  255 ), (i * 100 , 500 ),50,1) 

        map_grid = 0
        if map_grid == 1:
            for x in range(grid_size1):
                for y in range(grid_size2):pg.draw.rect(mini_map_surf , ( cell_color) , ( cell_size * x / map_scale * minimap_object_offset , cell_size * y / map_scale * minimap_object_offset1 , mini_map_grid_cell_size / map_scale , mini_map_grid_cell_size / map_scale) , 1 ) #drawing a inventory cells






def mini_map_mouse_controls():
    global cancel_icon
    if event.button == 1 and pos[0] >= cancel_icon_x and pos[0] <= cancel_icon_x + cancel_icon.get_width() and pos[1] >= cancel_icon_y and pos[1] <= cancel_icon_y + cancel_icon.get_height() and map_size == max_map_size : map_size = min_map_size

    if event.button == 3 and map_size == max_map_size : spawn_sound.play() ; custom_checkpoints_list_x.append(camera1.rect[0] + pos[0]) ; custom_checkpoints_list_y.append(camera1.rect[1] + pos[1])

changed_keybinds = []

Random_events = []

def toggle_settings():
    Button_color,button_width
    if game_state == 'Settings':
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
    if game_state == 'character_select_menu':
        for i in range(len(Hero_types)):            
            Button = pg.draw.rect(screen , (Button_color) , ( int(screen_width) /  2 - button_width / 2 , int(screen_height) / 2 - int(screen_height) / 4 - bigfont + i * 40 + bigfont /2 , button_width , bigfont + 5 ) , 0 , 0 , button_border_radius , button_border_radius , button_border_radius , button_border_radius)            
            screen.blit(Hero_types_list[i]    , ( int(screen_width) /  2 - button_width / 2  , int(screen_height) / 2 - int(screen_height) / 4 - bigfont + i * 40 + bigfont / 2 , button_width , bigfont ))
            pg.draw.rect(screen , (Button_frame_color)  ,  ( int(screen_width) /  2 - button_width / 2 , int(screen_height) / 2 - int(screen_height) / 4 - bigfont + active_button * 40 + bigfont / 2 , button_width , bigfont + 5 ) , 2 , 0 , button_border_radius , button_border_radius , button_border_radius , button_border_radius)
            screen.blit(hero_image1 , ( int(screen_width) / 2 + int(screen_width) / 4 - hero_image1.get_width() /2 , hero_image1.get_height() ))


def game_mode_select():
    if game_state == 'game_mode_select':
        for i in range(len(game_modes1)):            
            Button = pg.draw.rect(screen , (Button_color) , ( int(screen_width) /  2 - button_width / 2 , int(screen_height) / 2 - int(screen_height) / 4 - bigfont + i * 40 + bigfont /2 , button_width , bigfont + 5 ) , 0 , 0 , button_border_radius , button_border_radius , button_border_radius , button_border_radius)            
            pg.draw.rect(screen , (Button_frame_color)    , ( int(screen_width) /  2 - button_width / 2 , int(screen_height) / 2 - int(screen_height) / 4 - bigfont + active_button * 40 + bigfont / 2 , button_width , bigfont + 5 ) , 2 , 0 , button_border_radius , button_border_radius , button_border_radius , button_border_radius)
            screen.blit(game_modes1[i]    , ( int(screen_width) /  2 - button_width / 2  , int(screen_height) / 2 - int(screen_height) / 4 - bigfont + i * 40 + bigfont / 2 , button_width , bigfont ))



def Difficulty_select():
    if game_state == 'Select_a_difficulty':
        for i in range(len(difficulties1)):            
            Button = pg.draw.rect(screen , (Button_color) , ( int(screen_width) /  2 - button_width / 2 , int(screen_height) / 2 - int(screen_height) / 4 - bigfont + i * 40 + bigfont /2 , button_width , bigfont + 5 ) , 0 , 0 , button_border_radius , button_border_radius , button_border_radius , button_border_radius)            
            pg.draw.rect(screen , (Button_frame_color)    , ( int(screen_width) /  2 - button_width / 2 , int(screen_height) / 2 - int(screen_height) / 4 - bigfont + active_button * 40 + bigfont / 2 , button_width , bigfont + 5 ) , 2 , 0 , button_border_radius , button_border_radius , button_border_radius , button_border_radius)
            screen.blit(difficulties1[i]                  , ( int(screen_width) /  2 - button_width / 2 , int(screen_height) / 2 - int(screen_height) / 4 - bigfont + i * 40 + bigfont / 2 , button_width , bigfont ))



def Open_backpack():
    if game_state == 'Backpack':
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
    menu_titles    = [obj_dir[i] for i in range(len(obj_dir))]
        
    menu_titles1   = []
    menu_title_num = 0
    menu_title     = menu_titles[menu_title_num]
    for i in menu_titles: i = big_font.render(menu_titles[i].split(',')[0].strip() , False , small_font_color ) ; menu_titles1.append(i)   

        
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
        draw_menu()
        for i in range(len(os.listdir(menus_dir))):
            pg.draw.rect(screen , (Button_color) , (int(screen_width) /  2 - button_width / 2 , int(screen_height) / 2 - int(screen_height) / 4 - bigfont + i * 40 + bigfont / 2 , button_width , bigfont + 5 ) , 0 , 0 , button_border_radius , button_border_radius , button_border_radius , button_border_radius)            
            pg.draw.rect(screen , (Button_frame_color)    , (int(screen_width) /  2 - button_width / 2 , int(screen_height) / 2 - int(screen_height) / 4 - bigfont + active_button * 40 + bigfont / 2 , button_width , bigfont + 5 ) , 2 , 0 , button_border_radius , button_border_radius , button_border_radius , button_border_radius)
            screen.blit(show_mods_count                   , (int(screen_width) /  2 - button_width / 2 + 75 , int(screen_height) / 2 - int(screen_height) / 4 - bigfont + 3 * 40 + bigfont / 2 , button_width , bigfont ))





def toggle_mods_menu():
    if game_state == 'toggle_mods_menu':
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






"""
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
        print()"""

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


import sys , os
import pygame as pg ; from PIL import Image ; from Units import * ; from logging import *; 
from Vehicles import * ; import pyautogui ;
from Background import * ; import math;import numpy as np
import time ; from Items import *
import pprint
import cv2
import mido
from pygame.locals import *
import pyaudio
from Settings import *

os.environ["SDL_VIDEODRIVER"] = '1'
pg.init()
pg.joystick.init()
p = pyaudio.PyAudio()

keys = pg.key.get_pressed()

# Цвета
land_color = (162, 101, 62)

BG_COLOR = (0, 0, 200)

dots_num   = 36
rocks_num  = 36
dots       = []
rocks      = []
rock_size  = 70
rock_scale = 2

sea_scale = 2
sea_size  = 200

for x in range(dots_num):
            dots.append(

(

[400 + sea_size * math.cos(math.radians(x*10)) + random.randint(0,10) , 400 + sea_size// sea_scale * math.sin(math.radians(x*10)) + random.randint(0,10)]

)

)




for x in range(rocks_num):
            rocks.append(

(

[400 + rock_size * math.cos(math.radians(x*10)) + random.randint(0,10) , 400 + rock_size//rock_scale * math.sin(math.radians(x*10)) + random.randint(0,10)]

)

)

def mini_map_keyboard_controls():

    global map_scale , minimap_x , minimap_y , map_size , minimap_horizontal_offset , minimap_vertical_offset , cancel_icon , cancel_icon_x , cancel_icon_y , mini_map_surf
    global minimap_object_offset , minimap_object_offset1

    if show_map == 1 and game_state == 'Play' :
        
        if keys [pg.K_LEFT ] : minimap_object_offset  -= 1 
        if keys [pg.K_RIGHT] : minimap_object_offset  += 1

        if keys [pg.K_UP   ] : minimap_object_offset1 -= 1
        if keys [pg.K_DOWN ] : minimap_object_offset1 += 1

        if keys [pg.K_KP_PLUS ] : mini_map_surf.fill((minimapBGcolor)) ; map_scale -= 0.01 ; #draw_mini_map()
        if keys [pg.K_KP_MINUS] : mini_map_surf.fill((minimapBGcolor)) ; map_scale += 0.01 ; #draw_mini_map()

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
            if game_state == 'Main_menu':
                if event.button == 1:
                    if active_button == 0 : spawn_sound.play() ; pg.display.update();game_state = 'Play' 

            if game_state == 'Play' :
                if event.button == 2 : game_state = 'Trade_menu' ; print('active buton ', active_button) ; click_sound.play()
                if map_size == max_map_size :  
                        if event.button == 4 : map_scale -= 0.1 ; #draw_mini_map()
                        minimapfontsize = int( 30 / map_scale)
                        mini_map_font_size = pg.font.SysFont(font_name , minimapfontsize) 
                        custom_checkpoint_title = mini_map_font_size.render('Custom checkpoint'    , False , small_font_color ) 

                        if event.button == 5 : map_scale += 0.1 ; #draw_mini_map()
                        minimapfontsize = int( 30 / map_scale)
                        mini_map_font_size = pg.font.SysFont(font_name , minimapfontsize) 
                        custom_checkpoint_title = mini_map_font_size.render('Custom checkpoint'    , False , small_font_color ) 
                

                        #if event.button == 1:
                        if action_counter == 2 : game_state = 'Trade_menu' ;dialoge_started = 0 ; spawn_sound.play() 
                        if action_counter == 3 : game_state = 'Crafting'   ; dialoge_stated = 0 ; spawn_sound.play() 
                        if action_counter == 4 : dialoge_started = 0
                    



            if game_state == 'character_select':
                if event.button == 0 : game_state = 'Play' ; print('game state : ', game_state ) ; click_sound.play()
                if event.button == 4 and active_button >= 1 : active_button -= 1 ; click_sound.play() ; print('active buton ', active_button)
                if event.button == 5  and active_button <= len(Hero_types) - 2 : active_button += 1 ; click_sound.play() ; print('active buton ' , active_button)



            if game_state == 'Trade_menu':
                if event.button == 4 and pos[0]<= int(screen_width) / 2 and active_button  >= 1 : active_button -= 1 ; click_sound.play() ; print('active buton ', active_button) 
                
                if event.button == 4 and pos[0]>= int(screen_width) / 2 and active_button1 >= 1 : active_button1 -= 1 ; click_sound.play() ; print('active buton ', active_button) 



                if event.button == 5 and pos[0]<= int(screen_width) / 2 and active_button  <= len(menu_titles1) - 2 : active_button += 1 ; click_sound.play() ; print('active buton ' , active_button) 
            
                if event.button == 5 and pos[0]>= int(screen_width) / 2 and active_button1 <= len(menu_titles1) - 2 : active_button1 += 1 ; click_sound.play() ; print('active buton1 ' , active_button1) 
            


            if game_state == 'Saves':
                if event.button == 1 and active_button == 1 : game_state = 'game_mode_select' ; click_sound.play()
                if event.button == 4 and active_button == 3 and active_button1  >= 1 and pos[0] >= int(screen_width) / 2 : active_button1 -= 1 ; click_sound.play() 
                if event.button == 5 and active_button == 3 and active_button1  <= len(menus_dir) -2 and pos[0] >= int(screen_width) / 2 : active_button1 += 1 ; click_sound.play()
            


            if game_state == 'game_mode_select':
                if event.button == 1 and active_button   == 0 : game_state = 'Select_a_difficulty' ; click_sound.play()

                if event.button == 4 and active_button1  >= 1 and pos[0] >= int(screen_width) / 2 : active_button1 -= 1 ; click_sound.play() 

                if event.button == 5 and active_button1  <= len(menus_dir) -2 and pos[0] >= int(screen_width) / 2 : active_button1 += 1 ; click_sound.play()
            


            if game_state == 'Select_a_difficulty':

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

                if event.button == 3 : game_state = 'Main_menu' ; click_sound.play() ; active_button = 0
                


                if event.button == 4 and active_button  >= 1 and pos[0] <= int(screen_width) / 2 : active_button -= 1 ; click_sound.play()
                
                if event.button == 4 and active_button1 >= 1 and pos[0] >= int(screen_width) / 2 : active_button1 -= 1 ; click_sound.play()
                
                if event.button == 4 and active_button  == 3 and active_button1  >= 1 and pos[0] >= int(screen_width) / 2 : active_button1 -= 1 ; click_sound.play() 



                if event.button == 5 and active_button  <= len(settings_file1) -2 and pos[0] <= int(screen_width) / 2 : active_button += 1 ; click_sound.play()
                
                if event.button == 5 and active_button1  <= len(settings_file1) -2 and pos[0] >= int(screen_width) / 2 : active_button1 += 1 ; click_sound.play()

                if event.button == 5 and active_button == 3 and active_button1  <= len(menus_dir) -2 and pos[0] >= int(screen_width) / 2 : active_button1 += 1 ; click_sound.play()
    

if game_state == 'Play':
        player_movement()
        keys = pg.key.get_pressed()
        if keys[pg.K_e] and vihicle_sit == 1 : Open_unit_inventory()
        if keys [pg.K_ESCAPE]   and open_backpack == 1: open_backpack  = 0
        if keys [reload_btn] and mags >= 1 : reloadsound = pg.mixer.Sound( 'Audio/sounds/firegun/reload.mp3' ) ; reloadsound.play() ; mags -= 1 ; hero_file_name = 'txt/hero.txt' ; hero_file_mode = 'w' ; hero_file = open (hero_file_name , hero_file_mode) ; hero_file.write(str(mags)) ; hero_file.write(str(health)) ; hero_file.write(str(health)) ; hero_file.write(str(health)) ; hero_file.write(str(mags)) ; hero_file.write(str(mags)) ; hero_file.close() ; ammo = max_ammo ; show_ammo  = big_font.render(str(ammo) + " / "  + str( ammo * mags ) , False , colors[2] ) ; show_armor = big_font.render(str(armor).strip() + " / "  + str( max_armor ).strip() , False , ( 250 , 0, 0 ) ) ; show_health    = big_font.render(str(health).strip()     + " / "  + str( max_health ).strip() , False , ( 255 , 0 , 0 ) ) ; show_radiation = big_font.render(str(radiation ).strip() + " / "  + str( max_radiation ).strip() , False , ( 255 , 0 , 0 ) ) ; cursor = pg.image.load( 'Interface/icons/refresh_icon.png' )
        if keys [screenshot_btn ] : make_screenshot() ; logging.info( msg = 'SCREENSHOT SAVED!') ; print('Screenshot saved ! ')

        if keys [pg.K_f] : fuel += 0.1 ; show_fuel = big_font.render('Fuel  : ' + str(fuel)    , False , small_font_color ) ; print('Fuel : ' , fuel)
        
        if keys [pg.K_g  ] and keys[pg.K_LCTRL]  : toggle_god_mode() ;  spawn_sound.play() #GOD MODE - no damage , no limit etc
        if keys[back_btn]  : bg_image = bg_images[ random.randint( 0 , len(bg_images) - 1 ) ] ; game_state = 'Main_menu'

    #mini_map_keyboard_controls()
        


def player_movement():

        global keys,calc_dist,show_distance,hero_checkpoint_offset_x,hero_checkpoint_offset_y,state,hero_x,hero_y,turn,hero_speed,minimap_object_offset,minimap_object_offset1,hero_path_lenght,hero_path_angle,rot_hero,scaled_image
        global original_hero_img_width,original_hero_img_height,new_hero_img_width,new_hero_img_height,scale_factor,rect,new_hero_img_width,new_hero_img_height

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



listen_midi = 0


vector = [ 0 , 0]#cam vectors

if mods_dir_path not in sys.path : sys.path.append(mods_dir_path)
if mods_dir_path in sys.path : print() ; print() ; print('mods folder added ! ')

print(os.listdir(mods_dir_path))

for i in range(10) : MyShapes.append('circle') ; MyShapes.append('square') ; MyShapes.append('triangle') ; MyShapes.append('rectangle')    

        
multiplayer = 1
clock = pg.time.Clock() ; FPS = 60 ; clock.tick(FPS)
hide_nicknames = 0 ; ground = 1 ; floor = 0 
fuel_bar_width = 100

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

minimap_grid_width = 100 ; minimap_grid_height = 100 ; min_map_size = 3 ; max_map_size = 1.2 ; mini_map_grid_cell_size = meter * map_scale

cursor_types = ['Default' , 'Custom'] ; cursor_num = 0 ; cursor_type = cursor_types[cursor_num]

hero_inventory_types = ['Grid' , 'Circle'] ; hero_inventory_num = 0 ; hero_inventory_type = hero_inventory_types[hero_inventory_num] ; hero_marker_color = (255 , int(255 / 2) , 0)

room_height , room_width = 3 * meter  , 5 * meter ; room_size   = room_height * room_width ; walll_size  = 22

sidewalk_width , sidewalk_height = 3 * meter , 3 * meter

hero_path_lenght  = 90 ; hero_path_angle  = 90 ; hero_path_lenght1 = 90 ; hero_path_angle1 = 90 ; unit_path_lenght = 90 ; unit_path_angle = 90

 


pg.display.update()

#pg.quit()


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
import pygame as pg , os
from Settings import mini_map_surf,show_items,map_scale,map_size,screen_width,screen_height
from Controls import camera1,fov,screen
from Funcs import saving_type,minimap_border_offset,minimap_object_offset,minimap_object_offset1
items_list = []
items_file_name = 'txt/Objects/' + str(saving_type) + '/Items.txt'
items_file_mode = 'r'
items_file = open (items_file_name , items_file_mode)
items_file1 = items_file.readlines()
items_images = []
items_categories = os.listdir('Objects/Items/')

class Items:
    def __init__( self , x , y , image) :
        self.x     = x
        self.y     = y
        self.image = image

for i in range( len ( items_file1 ) ) :
    items_images.append(pg.image.load('Objects/Items/' + str(items_categories[i]) + '/0/0.png'))
    i = Items( items_file1[i].split(',')[0] , items_file1[i].split(',')[1] , items_images[i])
    items_list.append( i )
    if show_items == 1 : pg.draw.rect(mini_map_surf , (0 , 255 , 0)  , (int(items_file1[i].split(',')[0]) / (100 * map_scale) + minimap_border_offset * minimap_object_offset , int(items_file1[i].split(',')[1]) / (100 * map_scale) + minimap_border_offset * minimap_object_offset1, 1 / map_scale , 1 / map_scale ))

for i in range(len(items_file1)) :
    if camera1.rect[0] + int(screen_width) - fov >= int(items_file1[i].split(',')[0]) and camera1.rect[1] + int(screen_height) - fov >= int(items_file1[i].split(',')[1]) : screen.blit( items_images[ i ] , ( -camera1.rect[ 0 ] + int(items_file1[i].split(',')[0]) , -camera1.rect[ 1 ] + int(items_file1[i].split(',')[1] ) ) )
        